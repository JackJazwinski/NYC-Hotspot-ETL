# NYC Wi-Fi Hotspot Mapper 🗽🗺️📡

A Python script that fetches public Wi-Fi hotspot data from NYC Open Data, cleans it, and generates an interactive HTML map to visualize their locations.

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌟 Overview

This script provides an easy way to visualize the distribution of public Wi-Fi hotspots across New York City. It leverages the NYC Open Data API to get the latest information, processes the data for accuracy and usability, and then uses the `folium` library to create a rich, interactive map. Key features include marker clustering for better visibility in dense areas and pop-up details for each hotspot.

## ✨ Features

* **Dynamic Data Fetching**: Retrieves up-to-date Wi-Fi hotspot information directly from the NYC Open Data API.

* **Robust Data Cleaning**: Employs `pandas` for efficient data handling, including type conversion (string to numeric for coordinates) and removal of entries with missing or invalid location data.

* **Interactive HTML Map Generation**: Creates a self-contained HTML file (`nyc_wifi_clean_map.html`) that can be opened in any web browser.

* **Marker Clustering**: Uses `folium.plugins.MarkerCluster` to group nearby hotspot markers, improving map readability and performance, especially in areas with high hotspot density.

* **Informative Popups**: Each marker on the map, when clicked, displays a popup with details such as SSID, provider, specific location description, and borough.

* **Borough Boundaries**: Overlays GeoJSON data to display the administrative borders of NYC boroughs, providing geographical context.

* **Customizable Map Tiles**: Uses 'CartoDB Positron' tiles for a clean and modern map aesthetic, with proper attributions.

* **Automatic Browser Launch**: Automatically opens the generated map in the user's default web browser for immediate viewing.

* **Graceful Termination & Cleanup**: Implements signal handling for `Ctrl+C` (SIGINT) to allow the user to decide whether to keep or delete the generated HTML map file upon exiting the script.

* **User-Friendly Console Output**: Prints informative messages to the console during fetching, cleaning, and map generation stages.

## 📸 Demo (Example)

Example:
![NYC Wi-Fi Map Screenshot](https://raw.githubusercontent.com/JackJazwinski/NYC-Hotspot-ETL/main/assets/nyc_wifi_etl_screenshot.png)

## 🛠️ Requirements

### Software:

* Python 3.x

### Python Libraries:

* `pandas`: For data manipulation and cleaning.

* `requests`: For making HTTP requests to the API.

* `folium`: For creating the interactive map.

You can install these dependencies using `pip`:





pip install pandas requests folium


The script also utilizes built-in Python modules: `webbrowser`, `os`, `signal`, `sys`, and `time`.

## ⚙️ Configuration

The script contains a configuration section at the beginning where you can adjust the following parameters:

* `API_ENDPOINT`: The URL of the NYC Open Data API for Wi-Fi hotspots.

  * Default: `"https://data.cityofnewyork.us/resource/yjub-udmw.json"`

* `LIMIT`: The maximum number of records to fetch from the API. It's advisable to set this to a number higher than the total expected records to ensure all data is retrieved.

  * Default: `4000`

* `OUTPUT_HTML`: The name of the HTML file that will be generated for the map.

  * Default: `"nyc_wifi_clean_map.html"`





--- CONFIGURATION ---
API_ENDPOINT = "https://data.cityofnewyork.us/resource/yjub-udmw.json"
LIMIT = 4000 # Should be higher than the number of records in the dataset
OUTPUT_HTML = "nyc_wifi_clean_map.html"


## 🚀 How to Run

1. **Clone the Repository (Optional):**
   If this script is part of a Git repository, clone it:




git clone https://github.com/JackJazwinski/NYC-Hotspot-ETL.git
cd NYC-Hotspot-ETL

Otherwise, ensure you have the Python script file (e.g., `nyc_wifi_etl.py`) in your desired directory.

2. **Install Dependencies:**
Open your terminal or command prompt and run:





pip install pandas requests folium


3. **Execute the Script:**
Navigate to the directory where you saved the script (e.g., the root of the `NYC-Hotspot-ETL` repository if you cloned it) and run:





python nyc_wifi_etl.py

*(Assuming your script is named `nyc_wifi_etl.py` from the GitHub repository)*

4. **View the Output:**

* The script will print progress messages to the console:




📡 Fetching NYC Wi-Fi hotspot data...
🧼 Cleaning data...
🗺️  Generating clean map...
✔ Map saved as: nyc_wifi_clean_map.html


* The generated HTML map (`nyc_wifi_clean_map.html` by default) will automatically open in your default web browser.

* The script will remain running in the terminal. This allows you to interact with the map. The console will display:




Press Ctrl+C to exit and choose whether to save or delete the map file...


5. **Exit and Cleanup:**

* To stop the script, go to the terminal where it's running and press `Ctrl+C`.

* You will be prompted to decide the fate of the generated map file:




Do you want to save the map file? (y/n):


Enter `y` to keep the file or `n` to delete it. The script will then exit.

## 📄 Output

The primary output of the script is an HTML file (default: `nyc_wifi_clean_map.html`) containing the interactive map. This file is self-contained and can be shared or opened in any modern web browser.

## 🧹 Cleanup Mechanism

The script includes a cleanup function that is triggered when the user presses `Ctrl+C` (SIGINT). This function provides a prompt asking whether to save or delete the generated HTML map file.

* If the user chooses `'y'` (yes), the file is kept.

* If the user chooses `'n'` (no), the `os.remove()` function is called to delete the file.

* The script handles potential errors during file operations within the cleanup process.

This ensures that temporary map files aren't left behind unintentionally unless the user explicitly decides to save them.

## 📂 File Structure (Example)

If your project is structured like your GitHub repository:




NYC-Hotspot-ETL/
├── nyc_wifi_etl.py          # The Python script
├── nyc_wifi_clean_map.html  # The generated interactive HTML map (after running)
├── assets/
│   └── nyc_wifi_etl_screenshot.png # Your map screenshot
├── LICENSE.md               # Your MIT License file
└── README.md                # This README file


## 💡 Troubleshooting

* **No Data or API Error**:

  * Ensure you have an active internet connection.

  * Check if the `API_ENDPOINT` URL is correct and the NYC Open Data service is operational.

  * The API might have rate limits. If you run the script too frequently, you might encounter temporary blocks.

* **Map Not Opening**:

  * Ensure you have a default web browser configured on your system.

  * Check for any error messages in the console that might indicate why `webbrowser.open()` failed.

* **Incorrect Map Display**:

  * If markers are not appearing, there might be an issue with data cleaning or the latitude/longitude values from the API.

  * Ensure the GeoJSON URL for borough boundaries is accessible.

* **Dependency Issues**:

  * Make sure all required libraries (`pandas`, `requests`, `folium`) are installed correctly in your Python environment.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! You can open an issue on the [GitHub repository's issues page](https://github.com/JackJazwinski/NYC-Hotspot-ETL/issues).

1. Fork the Project

2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)

3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)

4. Push to the Branch (`git push origin feature/AmazingFeature`)

5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE) file for details.
