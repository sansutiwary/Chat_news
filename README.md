\documentclass{article}
\usepackage{hyperref}
\usepackage{listings}
\usepackage{graphicx}
\usepackage{xcolor}

\title{News Chat App}
\author{Sansutiwary}

\begin{document}

\maketitle

\section*{Introduction}
The News Chat App is a web-based application that allows users to interact with a chat interface to receive the latest news updates. The app fetches news from the NDTV RSS feed and displays it in a chat format. Users can request news updates by typing \textit{"news"} and can choose to receive more updates or end the interaction.

\section*{Features}
\begin{itemize}
    \item Interactive chat interface.
    \item Fetches news from NDTV RSS feed.
    \item Displays news in a user-friendly format.
    \item Allows users to request more news or end the interaction.
    \item Responsive design with a clean, orange-themed UI.
\end{itemize}

\section*{Installation}
\begin{enumerate}
    \item Clone the repository:
    \begin{lstlisting}[language=bash]
    git clone https://github.com/sansutiwary/Chat_news.git
    \end{lstlisting}
    \item Navigate to the project directory:
    \begin{lstlisting}[language=bash]
    cd Chat_news
    \end{lstlisting}
    \item Install the required dependencies:
    \begin{lstlisting}[language=bash]
    pip install flask feedparser
    \end{lstlisting}
\end{enumerate}

\section*{Usage}
\begin{enumerate}
    \item Run the Flask application:
    \begin{lstlisting}[language=bash]
    python app.py
    \end{lstlisting}
    \item Open your web browser and go to:
    \begin{lstlisting}[language=bash]
    http://127.0.0.1:5000/
    \end{lstlisting}
    \item Interact with the chat interface to receive news updates.
\end{enumerate}

\section*{Project Structure}
\begin{verbatim}
Chat_news/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    └── css/
        └── styles.css
\end{verbatim}

\section*{Code Overview}
\subsection*{app.py}
The main Flask application file. It defines the routes and logic for fetching and serving news items.

\begin{lstlisting}[language=python]
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
\end{lstlisting}

\subsection*{index.html}
The main HTML file that defines the structure and layout of the chat interface.

\subsection*{styles.css}
The CSS file that defines the styling and theme of the chat interface.

\section*{Future Improvements}
\begin{enumerate}
    \item \textbf{News Categories}
    \begin{itemize}
        \item Provide options for users to select news categories (e.g., sports, technology, politics).
        \item \textbf{Frontend Changes:}
        \begin{itemize}
            \item Add category buttons.
            \item Modify the \texttt{fetchNews} function to take a category parameter.
        \end{itemize}
    \end{itemize}
    \item \textbf{User Authentication}
    \begin{itemize}
        \item Enable users to log in to personalize their news feed.
        \item \textbf{Frontend Changes:}
        \begin{itemize}
            \item Add a login form.
            \item Display personalized messages and news for logged-in users.
        \end{itemize}
    \end{itemize}
    \item \textbf{Save/Bookmark Articles}
    \begin{itemize}
        \item Allow users to save or bookmark articles for later reading.
        \item \textbf{Frontend Changes:}
        \begin{itemize}
            \item Add a "Save" button next to each news item.
            \item Create a section to display saved articles.
        \end{itemize}
    \end{itemize}
    \item \textbf{User Preferences}
    \begin{itemize}
        \item Allow users to set preferences for the type of news they want to receive.
        \item \textbf{Frontend Changes:}
        \begin{itemize}
            \item Add a settings page for user preferences.
            \item Modify the news-fetching function to filter news based on preferences.
        \end{itemize}
    \end{itemize}
    \item \textbf{Push Notifications}
    \begin{itemize}
        \item Send real-time notifications to users when new articles are available.
        \item \textbf{Frontend Changes:}
        \begin{itemize}
            \item Implement push notifications using the Web Push API.
        \end{itemize}
    \end{itemize}
    \item \textbf{Enhanced News Display}
    \begin{itemize}
        \item Include features like image sliders, video news, and audio summaries.
        \item \textbf{Frontend Changes:}
        \begin{itemize}
            \item Add a carousel for images and videos.
            \item Embed audio players for news summaries.
        \end{itemize}
    \end{itemize}
    \item \textbf{User Feedback}
    \begin{itemize}
        \item Allow users to rate articles or provide feedback on the news.
        \item \textbf{Frontend Changes:}
        \begin{itemize}
            \item Add a rating system for each article.
            \item Include a feedback form.
        \end{itemize}
    \end{itemize}
\end{enumerate}

\section*{Screenshots}

\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{news_app_interface.png}
    \caption{News app interface}
\end{figure}

\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{ask_for_more_news.png}
    \caption{App asking if user wants more news}
\end{figure}

\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{yes_more_news.png}
    \caption{More news provided when user types "yes"}
\end{figure}

\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{no_more_news.png}
    \caption{No more news when user types "no"}
\end{figure}

\section*{Contributing}
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

\section*{License}
This project is licensed under the MIT License. See the LICENSE file for details.

\end{document}
