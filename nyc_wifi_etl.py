import pandas as pd # type: ignore # For data manipulation and cleaning (e.g., converting types, removing missing values)
import requests # type: ignore # To send HTTP requests and fetch data from the NYC Open Data API
import folium # type: ignore # To generate interactive maps in HTML format
from folium.plugins import MarkerCluster # type: ignore # For grouping nearby map markers into clusters
import webbrowser # To automatically open the generated HTML map in the default browser
import os # For file operations, like checking if the map file exists or deleting it
import signal # To catch interrupt signals (e.g., Ctrl+C) for graceful program termination
import sys # To exit the program after cleanup
import time # To keep the script running (idle loop) until interrupted by the user

# --- CONFIGURATION ---
API_ENDPOINT = "https://data.cityofnewyork.us/resource/yjub-udmw.json"
LIMIT = 4000 # Should be higher than the number of records in the dataset
OUTPUT_HTML = "nyc_wifi_clean_map.html"

# --- CLEANUP FUNCTION ---
def cleanup(signum=None, frame=None):
    if os.path.exists(OUTPUT_HTML):
        try:
            while True:
                choice = input("\nDo you want to save the map file? (y/n): ").lower()
                if choice in ['y', 'n']:
                    break
                print("Please enter 'y' or 'n'")
            
            if choice == 'n':
                os.remove(OUTPUT_HTML)
                print(f"Cleaned up: {OUTPUT_HTML}")
            else:
                print(f"Map file saved as: {OUTPUT_HTML}")
        except Exception as e:
            print(f"\nError handling file: {e}")
    sys.exit(0)

# Register the cleanup function for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, cleanup)

# --- EXTRACT ---
def fetch_data(api_url, limit):
    params = {"$limit": limit}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    return response.json()

# --- TRANSFORM ---
def clean_data(raw_data):
    df = pd.DataFrame(raw_data)
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    df.dropna(subset=['latitude', 'longitude'], inplace=True)
    return df

# --- LOAD / DISPLAY ---
def create_clean_map(df, output_html=OUTPUT_HTML):
    # Create map centered on NYC with grayscale tiles 'CartoDB Positron'
    wifi_map = folium.Map(
        location=[40.7128, -74.0060],
        zoom_start=11,
        control_scale=True,
        tiles='CartoDB Positron',
        attr='&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="https://carto.com/attributions">CARTO</a>' # Required attribution for CartoDB tiles
    )

    # Get unique boroughs from the data
    boroughs = df['borough'].unique()

    # Add administrative borders for boroughs
    folium.GeoJson(
        'https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON/master/ny_new_york_zip_codes_geo.min.json',
        style_function=lambda x: {
            'fillColor': 'transparent',
            'color': 'gray',
            'weight': 1,
            'opacity': 0.5 if any(borough.lower() in str(x['properties']).lower() for borough in boroughs) else 0
        }
    ).add_to(wifi_map)

    # Add marker clustering
    cluster = MarkerCluster().add_to(wifi_map)

    for _, row in df.iterrows():
        popup_html = f"""
        <b>SSID:</b> {row.get('ssid', 'Unknown')}<br>
        <b>Provider:</b> {row.get('provider', 'Unknown')}<br>
        <b>Location:</b> {row.get('location', '')}<br>
        <b>Borough:</b> {row.get('borough', '')}
        """
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5,
            fill=True,
            fill_color='blue',
            color='blue',
            fill_opacity=0.7,
            popup=folium.Popup(popup_html, max_width=250)
        ).add_to(cluster)

    wifi_map.save(output_html)
    print(f"✔ Map saved as: {OUTPUT_HTML}")
    # Open the map in the default web browser
    webbrowser.open(output_html)

# --- RUN ---
if __name__ == "__main__":
    print("📡 Fetching NYC Wi-Fi hotspot data...")
    data = fetch_data(API_ENDPOINT, LIMIT)

    print("🧼 Cleaning data...")
    df_wifi = clean_data(data)

    print("🗺️  Generating clean map...")
    create_clean_map(df_wifi)
    print("\nPress Ctrl+C to exit and choose whether to save or delete the map file...")
    
    try:
        # Keep the program running until interrupted
        while True:
            time.sleep(1)  # Sleep for 1 second intervals
    except KeyboardInterrupt:
        cleanup()
