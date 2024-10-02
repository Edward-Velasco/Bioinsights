from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render the frontend

@app.route('/api/data')
def get_data():
    return jsonify({'message': 'Hello from the backend!'})  # Serve data to frontend

# if __name__ == "__main__":
#     app.run(debug=True)
