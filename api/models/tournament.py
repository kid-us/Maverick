#!/usr/bin/python
""" 
    This module contains the database model for the tournament table.
    It is used for storing and tracking the tournament details.

    file: tournament.py
    Author: Yaekob Demisse
    Date: June 30, 2023
"""


from models import db
from utils.generate_access_code import generate_access_string
from datetime import datetime


class Tournament(db.Model):
    """
    Tournament model for the application

    Attributes:
        id (int): the unique identifier for the tournament
        name (str): the name of the tournament
        description (str): the description of the tournament
        entry_fee (float): the entry fee for the tournament
        number_of_players (int): the number of players for the tournament
        start_date (datetime): the start date of the tournament
        number_of_remaining_players (int): the number of remaining players for the tournament
        access_code (str): the access code for the tournament (delimited string)
        available_access_codes: (str): the list of available access codes
        used_access_codes: (str) : the list of access_code user already joined
        user_id (int): the foreign key to the user who created the tournament
        user (relationship): the relationship to the registered user
        is_active (bool): the status of the tournament
        created_date (datetime): the date the tournament was created
        updated_date (datetime): the date the tournament was updated
    """

    __tablename__ = "tournaments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    description = db.Column(db.Text, nullable=False)
    entry_fee = db.Column(db.Numeric(10, 2), nullable=False)
    number_of_players = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    number_of_remaining_players = db.Column(db.Integer)
    access_code = db.Column(db.Text, nullable=False)
    available_access_codes = db.Column(db.Text, nullable=False)
    used_access_codes = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", backref="tournaments")
    is_active = db.Column(db.Boolean, default=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    def start_date(self):
        """Return the start date of the tournament"""
        return self.start_date

    def is_active(self):
        """Return the status of the tournament"""
        return self.is_active

    def left(self):
        """
        Number of players left to join the tournament
        """
        return self.number_of_remaining_players

    def create_tournament(
        self, name, description, entry_fee, number_of_players, start_date, user_id
    ):
        """Create a new tournament"""
        access_code = generate_access_string(number_of_players)
        tournament = Tournament(
            name=name,
            description=description,
            entry_fee=entry_fee,
            number_of_players=number_of_players,
            start_date=start_date,
            number_of_remaining_players=number_of_players,
            access_code=access_code,
            available_access_codes=access_code,
            user_id=user_id,
        )
        db.session.add(tournament)
        db.session.commit()
        return tournament

    def send_access_code(self):
        """Send an access code for tournament entering players"""

        if self.available_access_codes:
            access_codes = self.available_access_codes.split(",")
            access_code = access_codes.pop()
            self.available_access_codes = ",".join(access_codes)
            self.used_access_codes = (
                ",".join(self.used_access_codes.split(",") + [access_code])
                if self.used_access_codes
                else access_code
            )
            db.session.commit()
            return access_code
        else:
            return None

    def __repr__(self):
        """Return a string representation of the tournament model"""
        return "<Tournament {}-{}>".format(self.id, self.name)
