import click
from flask.cli import FlaskGroup
from app import app
from seed import seed_database

cli = FlaskGroup(app)


@cli.command("seed")
def seed():
    with app.app_context():
        seed_database()

if __name__ == '__main__':
     cli()