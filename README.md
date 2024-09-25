# Apartment Finder
CasaCrawlers is a Python-based project designed to collect, analyze, and recommend real estate properties (apartments) by utilizing scraped data from various online sources. The project uses a combination of web scraping, image handling, and machine learning techniques to predict and recommend apartments based on user preferences. The system is also integrated with the Zillow API to retrieve additional property details.

# Features
- Data Collection: Scrapes real estate listings and collects information such as address, number of bedrooms, bathrooms, and prices.
- Image Handling: Displays images of properties by scraping or fetching via the Zillow API.
- Machine Learning Model: Implements K-Nearest Neighbors (KNN) to predict apartment preferences based on user data.
- Zillow API Integration: Retrieves additional apartment details and images
- User Interaction: Allows users to input preferences (like/dislike) based on proprty attributes

# Technologies
- Python
- Zillow API: Used to gather apartment details and images

# Requirements
- Python 3.7 or later
- Zillow API Key

# Setup Instructions
1. Clone the repository
```python
git clone https://github.com/yourusername/CasaCrawlers.git
cd CasaCrawlers
```
2. Install required Python packages:
```python
pip install pandas matplotlib pillow scikit-learn requests
```
3. Set up Zillow API
   - Obtain an API key from Zillow's RapidAPI platform.
   - Add the API key to your environment or directly into the script where needed.
   
# Zillow API Setup
- To fetch additional apartment details, the project uses the Zillow API. Ensure you have an API key and replace it in the script as follows:
```python
headers = {
    "X-RapidAPI-Key": "your_rapidapi_key",
    "X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}
```
# Usage Instructions
1. Open the script and ensure that all paths are correctly set to the dataset and images
2. Run the script
```python
python casacrawlers.py
```
3. Interaction
   - During execution, the script will display properties and their images. Based on the user's preferences (like/dislike), the system will recommend apartments
4. Zillow API Integration
   - The system will fetch additional property images and details from the Zillow API

# Data Flow
1. Apartment Data: The script loads apartment data from Toronto_Apartments.csv.
2. Image Display: Property images are retrieved and displayed using the Pillow library.
3. Machine Learning: The KNN algorithm is used to predict and recommend properties.
4. API Integration: Fetches real-time property data from Zillow API.
