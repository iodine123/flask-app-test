from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
most_viewed_api = "http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=4GKINutELZVWbAcMVVmJmJDV2rhxWYbh"

@app.route('/')
def index():
    response = requests.get(most_viewed_api)
    data = response.json()
    articles = data['results']
    for article in articles:
        print(article['id'])

    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    port = os.environ.get("PORT", 8080)
    app.run(debug=False, host='0.0.0.0', port=port)
