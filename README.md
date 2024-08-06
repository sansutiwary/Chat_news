# News Chat App

![News Chat App Logo](https://drive.google.com/file/d/1U7PADxqEBQOxWxTKVur80QbzzlNybGcS)

Welcome to the News Chat App! This is a Flask web application that allows users to interact with a chat interface to receive the latest news updates from NDTV. Users can request news updates by typing "news" and can choose to receive more updates or end the interaction.

## Features

- **Interactive Chat Interface**: Engaging chat interface for seamless user interaction.
- **Live News Updates**: Fetches and displays the latest news from NDTV.
- **Responsive Design**: Clean, orange-themed UI that works on all devices.
- **User-Friendly**: Simple and intuitive user experience.
- **User Authentication**: Users can log in to personalize their news feed.

## Screenshots

### User Authentication
![User Authentication](https://drive.google.com/uc?export=view&id=1QZKNyVS6LSxKl_I_wlUoJNKTTSG8uRPQ)

### News App Interface
![News App Interface](https://drive.google.com/uc?export=view&id=1Sazj7Pprj6_w9iiVU64NG8fniUVGwyHa)

### Asking for More News
![Asking for More News](https://drive.google.com/uc?export=view&id=1RtgPSmg7ByxlzbkvbfKtpRNbRLoUvWzK)

### More News Provided
![More News Provided](https://drive.google.com/uc?export=view&id=115u7RlgED68r2ELQzHD5qMo96HswC312)

### No More News
![No More News](https://drive.google.com/uc?export=view&id=1pA3Ttk5Cwi7DZ1KaJqzRzZuC9G2nupSa)


## Future Improvements

1. **News Categories**
   - Provide options for users to select news categories (e.g., sports, technology, politics).
   - **Frontend Changes:**
     - Add category buttons.
     - Modify the `fetchNews` function to take a category parameter.

2. **Save/Bookmark Articles**
   - Allow users to save or bookmark articles for later reading.
   - **Frontend Changes:**
     - Add a "Save" button next to each news item.
     - Create a section to display saved articles.

3. **User Preferences**
   - Allow users to set preferences for the type of news they want to receive.
   - **Frontend Changes:**
     - Add a settings page for user preferences.
     - Modify the news-fetching function to filter news based on preferences.

4. **Push Notifications**
   - Send real-time notifications to users when new articles are available.
   - **Frontend Changes:**
     - Implement push notifications using the Web Push API.

5. **Enhanced News Display**
   - Include features like image sliders, video news, and audio summaries.
   - **Frontend Changes:**
     - Add a carousel for images and videos.
     - Embed audio players for news summaries.

6. **User Feedback**
   - Allow users to rate articles or provide feedback on the news.
   - **Frontend Changes:**
     - Add a rating system for each article.
     - Include a feedback form.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/sansutiwary/Chat_news.git
