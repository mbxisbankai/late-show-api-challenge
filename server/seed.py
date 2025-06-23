from .app import app
from .models import db, Guest, Episode, Appearance
from datetime import datetime

# Sample data
guests = [
    Guest(name="Keanu Reeves", occupation="Actor"),
    Guest(name="Taylor Swift", occupation="Musician"),
    Guest(name="Elon Musk", occupation="Entrepreneur")
]

episodes = [
    Episode(date=datetime(2023, 10, 5), number=101),
    Episode(date=datetime(2023, 10, 6), number=102),
    Episode(date=datetime(2023, 10, 7), number=103)
]

appearances = [
    Appearance(guest=guests[0], episode=episodes[0], rating=5),
    Appearance(guest=guests[1], episode=episodes[1], rating=4),
    Appearance(guest=guests[2], episode=episodes[2], rating=3),
    Appearance(guest=guests[1], episode=episodes[0], rating=2) 
]

# Seed logic
with app.app_context():
    print("Clearing database...")
    Appearance.query.delete()
    Episode.query.delete()
    Guest.query.delete()

    print("Seeding guests...")
    db.session.add_all(guests)

    print("Seeding episodes...")
    db.session.add_all(episodes)

    print("Seeding appearances...")
    db.session.add_all(appearances)

    db.session.commit()
    print("Seeding complete.")
