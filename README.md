# ⚽ Dynamic Fbref Football Data Scraper
A customizable Python web scraping utility designed to extract comprehensive football (soccer) statistics from the Fbref website. This project was developed as a college project to demonstrate practical data acquisition skills, a crucial step in my journey toward becoming a Data Scientist.
The key feature of this script is its ability to allow the user to dynamically select both the Year and the League for data retrieval, enabling flexible historical and comparative analysis.
## ✨ Features
- Dynamic Selection: Scrape data for any season (e.g., 2023-2024, 2019-2020) and any major league available on Fbref.
- Comprehensive Data: Extracts key metrics and statistics from the selected league table.
- Structured Output: Saves the cleaned data directly into a .csv file for easy import into tools like Pandas, Excel, or SQL databases.
- Robust HTML Parsing: Utilizes BeautifulSoup for efficient and reliable extraction of table data.
## 🛠️ Requirements
This script requires Python 3.6+ and the following libraries:
- requests: To send HTTP requests and fetch the HTML content.
- beautifulsoup4 (bs4): To parse the HTML and navigate the DOM structure.
- pandas: To handle the structured data and export it to a CSV file.
## 🚀 Installation and Setup
Clone the Repository:
` 
git clone [https://github.com/Taggu1/football-info-scrapper.git](https://github.com/Taggu1/football-info-scrapper.git)
cd football-info-scrapper
`

Install Dependencies:
It is highly recommended to use a virtual environment.
# Create virtual environment (optional but recommended)
`python -m venv venv`
- source venv/bin/activate  # On macOS/Linux
- venv\Scripts\activate   # On Windows

# Install the required packages
`pip install requests beautifulsoup4 pandas re`

## 📁 Data Output
The output will be a CSV file named using the format: player_stats.csv.
Each row in the CSV will represent a player, and columns will include all relevant statistics scraped from the Fbref league table.
## 💡 Future Enhancements
Potential future improvements for this project include:
GUI/Web Interface: Developing a simple web interface (using Flask or Streamlit) to make the data selection even easier.
Data Cleaning Module: Adding a module to further clean, normalize, and perhaps merge the scraped data with other sources.
Database Integration: Implementing functionality to directly store the results into a MongoDB or PostgreSQL database instead of a local CSV.
Advanced Stats: Expanding the scraper to fetch more advanced performance metrics (e.g., xG, xA).
