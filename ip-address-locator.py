# Ip Address Locator
# PIP Install geocoder
import geocoder as geo
# Get your Own IP Address
ip_address = geo.ip('me')
print(ip_address)
# Find City of IP
ip = geo.ip('192.xxx.xxx.x')
print(ip.city)
# Get latitude and longitude of IP Address
print(ip.latlng)
# Get Area Info
info = geo.google('Sao Paulo')
print(info.geojson)
print(info.osm)
print(info.wkt)
