#!/usr/bin/python
"""
    This module contains the database model for the link table.
    it uses for storing and tracking the unique links generated for the power partner program.

    file: link_db.py
    author: Yaekob Demisse
    date: June 04 2023
"""


from models import db
from datetime import datetime


class PowerPartnerLink(db.Model):
    """
    PowerPartnerLink model for the application
    """

    __tablename__ = "power_partner_links"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link_url = db.Column(db.String(255), nullable=False, unique=True, index=True)
    link_type = db.Column(
        db.Enum("monthly", "unlimited", name="link_type_enum"),
        nullable=False,
        index=True,
    )
    generated_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    link_price = db.Column(db.Numeric(10, 2))
    usage_count = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), index=True)
    is_active = db.Column(db.Boolean, default=True)

    def is_active(self):
        """return the status of the link"""
        return self.is_active

    def count(self):
        """return the count of the link"""
        return self.usage_count

    def type(self):
        """return the type of the link"""
        return self.link_type

    def __repr__(self):
        """Return a string representation of the link model"""

        return "<Link {}-{}-{}>".format(self.id, self.link_type, self.usage_count)
