# Instagram Sentiment Analyzer

This project is a simple web application that analyzes the sentiment of comments on Instagram posts or reels. Users can input a link to an Instagram post/reel, and the app will scrape the comments and determine whether the overall sentiment is positive, negative, or neutral.

## Features

- Input form where users can paste an Instagram post or reel URL.
- Scrapes comments from the given Instagram link.
- Sentiment analysis using NLP to classify comments as positive, negative, or neutral.
- Displays the final sentiment based on the analysis.
- Fully deployed on Render for easy access.

## Tech Stack

- **Frontend:** 
  - HTML
  - CSS
  - JavaScript
- **Backend:**
  - Python (Flask or FastAPI)
  - BeautifulSoup/Selenium (for scraping Instagram comments)
  - TextBlob/VADER (for sentiment analysis)
- **Deployment:** Render

## Getting Started

### Prerequisites
- Python 3.x
- Flask or FastAPI
- BeautifulSoup or Selenium
- TextBlob or VADER for sentiment analysis
- Render account (for deployment)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/instagram-sentiment-analyzer.git
