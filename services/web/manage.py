from flask.cli import FlaskGroup

from project import app, db
from project.models import Ids


cli = FlaskGroup(app)

# Create a blank database
@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

# Add an initial values to database
@cli.command("seed_db")
def seed_db():
    db.session.add(Ids(id="42"))
    db.session.add(Ids(id="1"))
    db.session.add(Ids(id="2"))
    db.session.add(Ids(id="4"))
    db.session.add(Ids(id="9"))
    db.session.add(Ids(id="13"))
    db.session.add(Ids(id="15"))
    db.session.add(Ids(id="23"))
    db.session.commit()

if __name__ == "__main__":
    cli()