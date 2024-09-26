
# The following commands were used to download and unzip images from Google Drive during development.
# These lines have been removed because the images are now sourced from a different location.
! gdown <google-drive-id>
! unzip "<your-zip-file>.zip" -d .
! gdown <google-drive-id>

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

! pip install pillow

import pandas as pd
from sklearn.model_selection import train_test_split

# Preprocessing
training_data = pd.read_csv("Toronto_Apartments.csv")

from PIL import Image
import os

def display_address(address):
    """
    Displays all PNG images associated with a given address by resizing them to 300x150 pixels.

    Args:
        address (str): The street address used to locate images in the specified directory.

    Returns:
        None
    """
    for file in os.listdir("/content/SPIS Training Images/" + address):
        filename = os.fsdecode(file)
        if filename.endswith(".png"):
            address_pictures = Image.open(os.path.join("/content/SPIS Training Images/" + address, filename))
            address_pictures = address_pictures.resize((300, 150), Image.Resampling.LANCZOS)
            display(address_pictures)

# Collect user responses on house preferences
responses = []
print("Street Address/Monthly Rent/Number of Bedrooms/Number of Bathrooms:")

for index in range(len(training_data)):
    print(training_data.loc[index, "Address"], training_data.loc[index, "Price"], training_data.loc[index, "Bedroom"], training_data.loc[index, "Bathroom"])
    display_address(training_data.loc[index, "Address"])
    single_response = input("Do you like this house (y/n)? ")
    if single_response == "y":
        responses.append(1)
    elif single_response == "n":
        responses.append(0)

# Add user preferences to the dataframe
training_data['Preference'] = responses
print(responses)

def convertPriceToNumber(price_as_string):
    """
    Converts a price from a string format (e.g., '$1,000') to a float number, removing any
    currency symbols and commas, and adjusts the price by multiplying it by 1.22.

    Args:
        price_as_string (str): The price in string format with a dollar sign and commas.

    Returns:
        float: The adjusted price as a float number.
    """
    price_as_string = price_as_string.replace('$', '')
    price_as_string = price_as_string.replace(',', '')
    price_as_number = float(price_as_string)
    adjusted_price_as_number = price_as_number * 1.22
    return adjusted_price_as_number

# Applying the function to the 'Price' column in the dataframe
training_data['Price'] = training_data['Price'].apply(convertPriceToNumber)

from decimal import Decimal
from re import sub
import pandas as pd

# Load and clean the data by removing duplicates based on 'Address' column
data = pd.read_csv("Toronto_Apartments_Full.csv")
data = data.drop_duplicates('Address')

# Remove rows where 'Address' is already present in training_data
cond = data['Address'].isin(training_data['Address'])
data.drop(data[cond].index, inplace=True)

# Apply the conversion function to the 'Price' column
data['Price'] = data['Price'].apply(convertPriceToNumber)

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X_train = training_data[['Bedroom', 'Bathroom', 'Price']].to_numpy()
y_train = training_data['Preference'].to_numpy()

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

model.predict_proba(data[['Bedroom', 'Bathroom', 'Price']].to_numpy())

predictions = model.predict(data[['Bedroom', 'Bathroom', 'Price']].to_numpy())
data['Prediction'] = predictions

preferred = data['Prediction'] == 1
recommended_houses = data[preferred]
sampled_recommended_houses = recommended_houses.sample(20)
sampled_recommended_houses.head(20)

from PIL import Image
import urllib.request
import requests

def show_image_from_url(url):
  urllib.request.urlretrieve(url, "Apart_Pictures.png")
  img = Image.open("Apart_Pictures.png")
  display(img)

import requests
import time
import os

# Load the API key from environment variables
api_key = os.getenv('ZILLOW_API_KEY')

# Zillow API search URL
url = "https://zillow56.p.rapidapi.com/search_address"
headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

num_houses = 0
i = 0

# Loop to retrieve and display information for 3 houses
while num_houses < 3:
	query = {"address": sampled_recommended_houses.iloc[i]['Address']}
	response = requests.get(url, headers=headers, params=query).json()
	time.sleep(1)  # Pause between API requests

	if 'error' in response:  # Skip if there is an error in the response
		i += 1
		continue

	# Print house details
	print(f"Address: {sampled_recommended_houses.iloc[i]['Address']}")
	print(f"Bedroom: {sampled_recommended_houses.iloc[i]['Bedroom']}")
	print(f"Bathroom: {sampled_recommended_houses.iloc[i]['Bathroom']}")
	print(f"Price: {sampled_recommended_houses.iloc[i]['Price']}")

	# Show up to 5 images for the house
	for j in range(min(5, len(response['big']))):
		show_image_from_url(response['big'][j]['url'])

	num_houses += 1
	i += 1
