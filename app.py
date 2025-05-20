from flask import send_from_directory
from flask import Flask, render_template
import os

@app.route('/adsrock.txt')
def serve_adsrock():
    return send_from_directory('static', 'adsrock.txt')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Pastikan file ini ada di folder `templates`

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
