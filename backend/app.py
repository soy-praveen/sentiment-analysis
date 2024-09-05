from flask import Flask, request, jsonify
from sentiment_analysis import get_comments_from_post, analyze_sentiment

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    link = data['link']
    
    try:
        comments = get_comments_from_post(link)
        sentiment = analyze_sentiment(comments)
        return jsonify({"sentiment": sentiment})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
