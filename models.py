# # models.py
# from app import db
# from sqlalchemy.orm import validates

# class Hero(db.Model):
#     __tablename__ = 'heroes'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     super_name = db.Column(db.String(100), nullable=False)

# class Power(db.Model):
#     __tablename__ = 'powers'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(255), nullable=False)
    
# class HeroPower(db.Model):
#     __tablename__ = 'hero_powers'
#     id = db.Column(db.Integer, primary_key=True)
#     strength = db.Column(db.String(50))
#     hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
#     power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

#     # Relationships
#     hero = db.relationship('Hero', backref=db.backref('hero_powers', lazy=True))
#     power = db.relationship('Power', backref=db.backref('hero_powers', lazy=True))


from database import db 

class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    super_name = db.Column(db.String(100))
    powers = db.relationship('HeroPower', backref='hero', lazy=True)

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    heroes = db.relationship('HeroPower', backref='power', lazy=True)

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(20))
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

