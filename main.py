import requests

api_key = "71cb0bc3fbcd4f0db7204030105f3090"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&" \
      "apiKey=71cb0bc3fbcd4f0db7204030105f3090"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
