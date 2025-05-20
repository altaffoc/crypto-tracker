import requests
from flask import Flask, render_template, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/adsrock.txt')
def serve_adsrock():
    return send_from_directory('static', 'adsrock.txt')

@app.route('/api/prices')
def get_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin,ethereum,solana',
        'vs_currencies': 'usd'
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        return jsonify({
            'bitcoin': data['bitcoin']['usd'],
            'ethereum': data['ethereum']['usd'],
            'solana': data['solana']['usd']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
