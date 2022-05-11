import json
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/testdb'

db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.Integer, primary_key=True)
 
    def __repr__(self):
        return '<Book %r>' % self.title

class BookSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    author = fields.Integer()


@app.route('/')
def index():
    return json.dumps({'name': 'alicex',
                       'email': 'alice@outlook.com'})

@app.route('/api/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    schema = BookSchema()
    return jsonify( [ schema.dump(b) for b in books])

if __name__ == '__main__':
        script_name = __file__
        print("run:\n"
            "FLASK_APP-{} python -m flask run --port 8080 --host 0.0.0.0 --debug true".format(script_name))
        exit(1)


