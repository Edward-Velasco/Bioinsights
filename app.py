from flask import Flask, render_template, request, jsonify, g
from services.request_handler import RequestHandler

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    response = RequestHandler.handleRequest(data)
    if response.get('status') == 400:
        return jsonify(response['data']), 400
    return jsonify(response), 200

# if __name__ == '__main__':
#     app.run(debug=True)
