from backend import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, index=True)

    def __repr__(self):
        return f"User {self.name}"

class Artists(db.Model):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String,unique=True, nullable=False)
    songs = db.relationship('Songs', backref='name', lazy=True) 

    def __repr__(self):
        return f"International Artist {self.name}"

class Songs(db.Model):
    __tablename__ = "hits"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=True)  
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=True)      

    def __repr__(self):
        return f"{self.title}"