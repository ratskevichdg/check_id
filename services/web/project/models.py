from project import db

class Ids(db.Model):
    __tablename__ = "ids"
    id = db.Column(db.VARCHAR, primary_key=True)
