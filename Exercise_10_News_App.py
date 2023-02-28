import requests
import json

query = input("What typeof News are you interested in ?")

url = f"https://newsapi.org/v2/everything?q={query}&from=2023-01-28&sortBy=publishedAt&apiKey=566707e6709642869e739d24148bfecc"

r = requests.get(url)

news = json.loads(r.text)
# print(news,type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------------")