import requests
from pprint import pprint as pp

pos_codes_req = requests.get("http://api.postcodes.io/postcodes/E34HH")
print(pos_codes_req)
print(pos_codes_req.content)
print(pos_codes_req.json())
print(pos_codes_req.json()['result'])

api_list_req = requests.get("http://api.publicapis.org/entries")
pp(api_list_req.json())
