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
    @validates('name')
    def validates_name(self, key, name):
        if not name:
            raise ValueError('author must have a name')
        else:
            return name
    
    @validates('phone_number')
    def validates_phone_number(self, key, phone_number):
        if phone_number.isdigit() and len(phone_number) == 10:
            return phone_number
        else:
            raise ValueError('phone number must be 10 digits')

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
    def validates_title(self, key, title):
        if not title:
            raise ValueError('post must have a title')
        else:
            return title
        
    @validates('content')
    def validates_content(self, key, content):
        if len(content.replace(" ", "")) < 250:
            raise ValueError('content must be at least 250 characters')
        else:
            return content
    
    @validates('summary')
    def validates_summary(self, key, summary):
        if len(summary.replace(" ", "")) > 250:
            raise ValueError('summary must be 250 characters or less')
        else: 
            return summary
        
    @validates('category')
    def validates_category(self, key, category):
        accepted = ['Fiction', 'Non-Fiction']
        if category not in accepted:
            raise ValueError('category must be Fiction or Non-Fiction')
        else:
            return category

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
