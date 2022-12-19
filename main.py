import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import pycountry
from phonenumbers.phonenumberutil import region_code_for_country_code
from phonenumbers.phonenumberutil import region_code_for_number
from opencage.geocoder import OpenCageGeocode
import folium
import os

header = """
░██████╗░███████╗░█████╗░░█████╗░░█████╗░██████╗░███████╗██████╗░
██╔════╝░██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░██╗░█████╗░░██║░░██║██║░░╚═╝██║░░██║██║░░██║█████╗░░██████╔╝
██║░░╚██╗██╔══╝░░██║░░██║██║░░██╗██║░░██║██║░░██║██╔══╝░░██╔══██╗
╚██████╔╝███████╗╚█████╔╝╚█████╔╝╚█████╔╝██████╔╝███████╗██║░░██║
░╚═════╝░╚══════╝░╚════╝░░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
"""

print(header)
print()
print("------  Made by RITABRATA DAS  ------")
print()

if os.path.exists("mylocation.html"):
  os.remove("mylocation.html")
try:
  number = input("# Enter Phone Number (along with country code): ")
  pn = phonenumbers.parse(number)

  country = pycountry.countries.get(alpha_2=region_code_for_number(pn))
  location = country.name
  print()
  print("# The Location is found at: ", location)
  print("# The Service Provider is: ", carrier.name_for_number(phonenumbers.parse(number), "en"))
  print()

  key = input("# Enter Your API KEY: ")
  geocoder = OpenCageGeocode(key)
  query = str(location)
  results = geocoder.geocode(query)
  lat = results[0]['geometry']['lat']
  lng = results[0]['geometry']['lng']
  print()
  print("# The coordinates are: " + lat + ", " + lng)
  print("Opening Map in Firefox........")

  myMap = folium.Map(location=[lat , lng], zoom_start=9)
  folium.Marker([lat,lng],popup=location).add_to(myMap)
  myMap.save("mylocation.html")
  os.system("firefox mylocation.html")
except:
  print("ERROR RECEIVED: ")
  print("Missing or invalid number.\nPlease enter your phone number with country code.")
