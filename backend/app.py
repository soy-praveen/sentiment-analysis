import os
from flask import Flask, request, render_template
from sentiment_analysis import analyze_sentiment  # Import the modified function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Ensure you have this template

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form.get('url')
    if url:
        result = analyze_sentiment(url)
        if 'error' in result:
            return render_template('index.html', error=result['error'])
        return render_template('result.html', result=result)  # Create this template
    return render_template('index.html', error="URL is required.")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the PORT environment variable if available
    app.run(host='0.0.0.0', port=port, debug=True)
