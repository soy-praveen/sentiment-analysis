import instaloader
from textblob import TextBlob

def get_comments_from_post(post_url):
    # Initialize Instaloader
    L = instaloader.Instaloader()

    # Fetch post metadata
    short_code = post_url.split('/')[-2]
    post = instaloader.Post.from_shortcode(L.context, short_code)

    comments = []
    for comment in post.get_comments():
        comments.append(comment.text)

    return comments

def analyze_sentiment(comments):
    # Analyze each comment
    positive, negative, neutral = 0, 0, 0

    for comment in comments:
        analysis = TextBlob(comment)
        if analysis.sentiment.polarity > 0:
            positive += 1
        elif analysis.sentiment.polarity < 0:
            negative += 1
        else:
            neutral += 1

    if positive > negative:
        return 'Positive'
    elif negative > positive:
        return 'Negative'
    else:
        return 'Neutral'
