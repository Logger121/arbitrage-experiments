import requests
import bs4

result = requests.get("https://www.oddschecker.com/boxing/")
print(result.text)