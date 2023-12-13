from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    # @validates('name')
    # def has_name(self, key, name):
    #     if not name:
    #         raise ValueError('author must have a name')
    #     return name
    
    @validates('phone_number')
    def check_num(self, key, num):
        if int(num) != 10:
            raise ValueError('phone number must be exactly 10 digits')
        return num

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  
    @validates('title')
    def has_title(self, key, title):
        if not title:
            raise ValueError('post must have a title')
        return title
    
    @validates('content')
    def con_length(self, key, content):
        if len(content) < 250:
            raise ValueError('content must be at least 250 characters')
        return content
    
    @validates('summary')
    def sum_length(self, key, summary):
        if len(summary) > 250:
            raise ValueError('summary must not be longer than 250 characters')
        return summary
    
    @validates('category')
    def correct_cat(self, key, category):
        if category != "Fiction" or category != "Non-Fiction":
            raise ValueError('category must be either Fiction or Non-Fiction')
        return category


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
