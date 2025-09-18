#api klici
#
import requests
#
#baseUrl='https://www.google.com/'
#klic=requests.get(baseUrl)
##print(klic)
#print(klic.text)


baseUrl='https://api.chucknorris.io/jokes/random'

#klic=requests.get(baseUrl)
#print(klic)
#print(klic.text)
#js=klic.json()
for i in range(5):
    klic=requests.get(baseUrl)
    js=klic.json()
    print(js.get('value'))