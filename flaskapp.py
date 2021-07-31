from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_get():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
