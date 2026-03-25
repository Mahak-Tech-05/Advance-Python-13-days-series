import requests

# Step 1: Take city input
city = input("Enter city name: ")

# Step 2: API URL (free API)
url = f"https://wttr.in/{city}?format=j1"

# Step 3: Send request
response = requests.get(url)
#api data json python convert 
# Step 4: Convert JSON → Python
data = response.json()

# Step 5: Extract data
temp = data["current_condition"][0]["temp_C"]
weather = data["current_condition"][0]["weatherDesc"][0]["value"]
humidity = data["current_condition"][0]["humidity"]

# Step 6: Print result
print("\n🌦️ Weather Report")
print("City:", city)
print("Temperature:", temp, "°C")
print("Condition:", weather)
print("Humidity:", humidity)
