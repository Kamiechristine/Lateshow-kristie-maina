from app import app
from extensions import db
from models import Episode, Guest, Appearance

def seed_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create sample episodes
        episode1 = Episode(date="1/11/99", number=1)
        episode2 = Episode(date="1/12/99", number=2)
        db.session.add_all([episode1, episode2])

        # Create sample guests
        guest1 = Guest(name="Michael J. Fox", occupation="actor")
        guest2 = Guest(name="Sandra Bernhard", occupation="Comedian")
        guest3 = Guest(name="Tracey Ullman", occupation="television actress")
        db.session.add_all([guest1, guest2, guest3])

        # Create sample appearances
        appearance1 = Appearance(rating=4, episode=episode1, guest=guest1)
        appearance2 = Appearance(rating=5, episode=episode2, guest=guest3)
        db.session.add_all([appearance1, appearance2])

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
