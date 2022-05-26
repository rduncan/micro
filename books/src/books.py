import json
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from marshmallow import Schema, fields, post_load

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/testdb'
api = Api(app)
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
    @post_load
    def make_book(self, data):
        return Book(**data)

class BookListResource(Resource):
    def get(self):
        books = Book.query.all()
        schema = BookSchema()
        return [ schema.dump(b) for b in books ]

    def post(self):
        book = BookSchema.load(request.get_json())
        db.session.add(book)
        db.session.commit()
        schema = BookSchema()
        return schema.dump(book)

api.add_resource(BookListResource, '/books')

if __name__ == '__main__':
        script_name = __file__
        print("run:\n"
            "FLASK_APP-{} python -m flask run --port 8080 --host 0.0.0.0 --debug true".format(script_name))
        exit(1)


