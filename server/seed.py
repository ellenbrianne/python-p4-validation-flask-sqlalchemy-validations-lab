from app import app
from models import db, Author, Post

with app.app_context():

    Author.query.delete()
    Post.query.delete()

    a1 = Author(name="el", phone_number="3142983977")
    a2 = Author(name="jo", phone_number="4132905655")
    db.session.add_all([a1, a2])
    db.session.commit()

    p1 = Post(title="Guess Who", content="a" * 250, category="Fiction", summary="b" * 248)
    p2 = Post(title="Secret Lives", content="a" * 255, category="Non-Fiction", summary="b" * 234)
    db.session.add_all([p1, p2])
    db.session.commit()

