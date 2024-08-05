from flask import Flask, jsonify, send_from_directory, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import feedparser

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db.create_all()

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
@login_required
def index():
    return send_from_directory('.', 'index.html')

@app.route('/get-news')
@login_required
def get_news():
    global news_index
    if not news_items:
        fetch_news()
    news_item = news_items[news_index % len(news_items)]
    news_index += 1
    return jsonify([news_item])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    fetch_news()
    app.run(debug=True)

