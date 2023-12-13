from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String, db.CheckConstraint('phone_number == 10'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    @validates('name')
    def has_name(self, key, val):
        if len(val) == 0 or hasattr(Author, val):
            raise ValueError('author must have a name and it must be unique')
        return val

    @validates('phone_number')
    def ten_digits(self, key, num):
        if len(num) != 10:
            raise ValueError('phone number must be exactly 10 digits long')
        return num
        

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, db.CheckConstraint('content > 250'))
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  
    @validates('content')
    def content_length(self, key, content):
        if content.len() < 250:
            raise ValueError('post must be at least 250 characters long')
        return content
    
    @validates('summary')
    def sum_length(self, key, summary):
        if len(summary) > 250:
            raise ValueError('post summary must be less than 250 characters')
        return summary
    
    @validates('category')
    def check_cat(self, key, cat):
        if cat != 'Fiction' or cat != 'Non-Fiction':
            raise ValueError('category must be either Fiction or Non-Fiction')
        return cat

    @validates('title')
    def click_bait(self, key, title):
        if ("Won't Believe") or ("Top") or ("Secret") or ("Guess") not in title:
            raise ValueError("title must include either Won't Believe, Secret, Top, or Guess")
        return title

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
