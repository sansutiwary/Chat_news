from flask import Flask, jsonify, send_from_directory
import feedparser

app = Flask(__name__)
news_index = 0
news_feed_url = 'https://feeds.feedburner.com/ndtvnews-top-stories'
news_items = []

def fetch_news():
    global news_items
    feed = feedparser.parse(news_feed_url)
    news_items = [{
        'title': entry.title,
        'summary': entry.summary,
        'link': entry.link,
        'published': entry.published,
        'image': entry.media_content[0]['url'] if 'media_content' in entry else ''
    } for entry in feed.entries]

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/get-news')
def get_news():
    global news_index
    if not news_items:
        fetch_news()
    news_item = news_items[news_index % len(news_items)]
    news_index += 1
    return jsonify([news_item])

if __name__ == '__main__':
    fetch_news()
    app.run(debug=True)

