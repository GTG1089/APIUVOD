import requests

baseUrl='https://api.nationalize.io/?name='
ime="Luka"
klic=requests.get(baseUrl+ime)
#print(klic.url)
#print(klic.get("count"))
#print(klic.get("name"))
drzave=klic.get("country")
for d in drzave:
    print(d.get("country_id"),d.get("probability"))