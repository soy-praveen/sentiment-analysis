import instaloader
from textblob import TextBlob
from instaloader import Instaloader, Post

def analyze_sentiment(post_url):
    # Initialize Instaloader and log in
    loader = Instaloader()

    # Use your Instagram username and password here
    USERNAME = 'ashicultz'
    PASSWORD = 'Mina@143'

    # Log in to Instagram
    try:
        loader.login(USERNAME, PASSWORD)
    except instaloader.exceptions.InstaloaderException as e:
        return {"error": f"Login failed: {str(e)}"}

    # Get post from URL
    shortcode = post_url.split('/')[-2]
    try:
        post = Post.from_shortcode(loader.context, shortcode)
    except Exception as e:
        return {"error": f"Failed to fetch post: {str(e)}"}

    # Extract comments
    comments = [comment.text for comment in post.get_comments()]
    
    # Perform sentiment analysis
    text = ' '.join(comments)
    blob = TextBlob(text)
    
    # Determine sentiment
    sentiment = "Positive" if blob.sentiment.polarity > 0 else "Negative" if blob.sentiment.polarity < 0 else "Neutral"
    
    return {
        "sentiment": sentiment,
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity
    }
