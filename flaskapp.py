from flask import Flask, request
from text_similarity import RatingGenerator
import text_parser
app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_get():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')