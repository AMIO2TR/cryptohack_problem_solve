import re
from geopy.geocoders import Nominatim

# Initialize geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Input string
input_string = """
Latitude: 40.1792, Longitude: 44.4991
Latitude: -4.6796, Longitude: 55.4919
Latitude: -21.1789, Longitude: -175.1982
Latitude: 31.9522, Longitude: 35.9304
Latitude: 41.3775, Longitude: 64.5853
Latitude: 60.472, Longitude: 8.4689
Latitude: 60.1282, Longitude: 18.6435
Latitude: 53.9045, Longitude: 27.559
Latitude: -18.1248, Longitude: 178.4501
Latitude: 4.3947, Longitude: 18.558
Latitude: -29.6099, Longitude: 28.2336
Latitude: -0.2299, Longitude: -78.5249
Latitude: 64.1355, Longitude: -21.8954
Latitude: 38.861, Longitude: 71.2761
Latitude: 42.5063, Longitude: 1.5211
Latitude: 49.6118, Longitude: 6.1319
Latitude: 48.669, Longitude: 19.699
Latitude: 42.4411, Longitude: 19.2636
Latitude: 11.8251, Longitude: 42.5903
Latitude: 10.6918, Longitude: -61.2225
Latitude: 11.8815, Longitude: -15.617
Latitude: 41.2044, Longitude: 74.7661
"""

# Function to get country name from latitude and longitude
from opencage.geocoder import OpenCageGeocode

# Your OpenCage API key
api_key = '6868ffe0a9db477fa24cef06be367bcc'  # Replace with your API key
geocoder = OpenCageGeocode(api_key)

# Function to get country name from latitude and longitude
def get_country(latitude, longitude):
    result = geocoder.reverse_geocode(latitude, longitude)
    if result and len(result):
        return result[0]['components'].get('country', 'Unknown')
    return "Unknown"



pattern = r"Latitude:\s*([-+]?\d*\.?\d+),\s*Longitude:\s*([-+]?\d*\.?\d+)"
matches = re.findall(pattern, input_string)

# Convert matches to float and find corresponding countries
country_names = [get_country(float(lat), float(lon)) for lat, lon in matches]

# Print the country names as a comma-separated list
print(", ".join(country_names))