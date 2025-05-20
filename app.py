from flask import send_from_directory

@app.route('/adsrock.txt')
def serve_adsrock():
    return send_from_directory('static', 'adsrock.txt')
