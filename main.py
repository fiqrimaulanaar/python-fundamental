import requests

print ("Hello World")

r = requests.get("https://sce.iti.ac.id")

print (r.text)