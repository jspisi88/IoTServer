#!/usr/bin/python3
from flask import Flask
import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!!!!!!!!"

@app.route("/api/books/titles/", methods=["GET"])
def get_book_titles():
    titles = []
    for book in books:
        titles.append(book['name'])
        return jsonify({​​'titles':titles}​​)
    
if(__name__== "__main__"):
    app.run(host='0.0.0.0', port=80)
    