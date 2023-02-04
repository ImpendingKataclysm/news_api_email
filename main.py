import requests
from send_email import send_email

api_key = "71cb0bc3fbcd4f0db7204030105f3090"
url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&" \
      f"apiKey={api_key}"

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["content"] + 2 * "\n"

body = body.encode('utf-8')

send_email(body)
