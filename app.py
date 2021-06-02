#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response
from random import random

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Love Languages',
        'author': 'Gary Chapman', 
        'year_published': 2000
    },
    {
        'id': 2,
        'title': 'Westside',
        'author': 'Blake Freeman', 
        'year_published': 1988
    }
]

authors = ['Chinua Achebe', 'Sidney Sheldon', 'Tom Clancy',
           'Joyce Meyer', 'Stephen King', 'George R. R. Martins', "Dan Brown"]
        
titles = ["The Eagle Eye", "Doomsday Conspiracy", "Half of a Yellow Sun",
          "Nothing Lasts Forever", "Angels and Demons", "A Song of Ice and Fire", "Under the Dome"]

years = [1990, 2004, 1984, 1920, 2015, 1972, 1963]

@app.route('/library/api/v1.0/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/library/api/v1.0/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book[0]})

@app.route('/library/api/v1.0/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author'],
        'year_published': request.json['year_published']
    }
    books.append(book)
    return jsonify({'book': book}), 201

@app.route('/library/api/v1.0/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    books.remove(book[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)