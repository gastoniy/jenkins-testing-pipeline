from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is created to test Pipeline in Jenkins."

@app.route('/health')
def health():
    return jsonify(
        status="UP",
        message="Application is healthy"
    ), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)