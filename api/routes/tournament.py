#!/usr/bin/python
"""
    A Blueprint to handle the tournament

    file: tournament.py
    Author: Yaekob Demisse
    Date: July 6 2023
"""


from flask import Blueprint, jsonify, request
from models.tournament import Tournament
from models import db


tournament = Blueprint("tournament", __name__, url_prefix="/api/v1/tournament")


@tournament.route("/create", methods=["POST"], strict_slashes=False)
def create_tournament():
    """creates a new tournament"""
    user_id = 1
    data = request.get_json()
    if not data:
        return (
            jsonify({"status": "error", "message": "Invalid payload or content type"}),
            400,
        )

    # check for required feilds in the payload
    required = ["name", "description", "entry_fee", "number_of_players", "start_date"]

    for field in required:
        if field not in data:
            return (
                jsonify({"status": "error", "message": "{} is required".format(field)}),
                400,
            )

    # create the tournament
    try:
        tournament = Tournament()
        tournament.create_tournament(
            name=data["name"],
            description=data["description"],
            entry_fee=data["entry_fee"],
            number_of_players=data["number_of_players"],
            start_date=data["start_date"],
            user_id=user_id,
        )
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

    return (
        jsonify(
            {
                "status": "success",
                "message": "Tournament created successfully",
                "data": tournament.access_code,
            }
        ),
        201,
    )
