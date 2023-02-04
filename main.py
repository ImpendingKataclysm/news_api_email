import requests
from send_email import send_email

topic = "python"
api_key = "71cb0bc3fbcd4f0db7204030105f3090"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=en"

request = requests.get(url)
content = request.json()

body = "Subject: Today's News\n"

for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body \
               + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] \
               + 2 * "\n"

body = body.encode('utf-8')

send_email(body)
