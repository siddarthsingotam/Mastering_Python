import requests
# import json -To check the dictionary structure

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
# print(json.dumps(response, indent=2))

# Processing the result from server.
print(response["value"])
print(f"\n**laughs nervously**") # Common it's Chuck Norris we are talking about, RUN!
