#!/usr/bin/python
"""
     A Blueprint to handle power partenr of the project

     file: referals.py
     author: Yaekob Demisse
     Date: June 29 09:12 AM
"""


from flask import Blueprint, jsonify, request
from utils.power_partner import generate_unique_link_string
from models.link_db import PowerPartnerLink
from models import db


# create the blueprint that is responsible for
# referal link generation
referal = Blueprint("referal", __name__, url_prefix="/api/v1/power-partner")


@referal.route("/generate-link", methods=["GET"], strict_slashes=False)
def generate_link():
    """ " Generate a unique referal link for a user"""
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"message": "user_id is required"}), 400
    type = request.args.get("type")
    if not type:
        return jsonify({"message": "type is required"}), 400
    if type not in ["monthly", "unlimited"]:
        return jsonify({"message": "type must be monthly or unlimited"}), 400
    price = request.args.get("price")
    if not price:
        return jsonify({"message": "price is required"}), 400
    unique_link = generate_unique_link_string(1).pop()
    link_url = f"http://localhost:5000/api/v1/power-partner/decoder?link={unique_link}"

    new_link = PowerPartnerLink(
        user_id=user_id, link_url=link_url, link_type=type, link_price=price
    )

    db.session.add(new_link)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "link generated successfully",
                "link": link_url,
            }
        ),
        200,
    )


@referal.route("/decoder", methods=["GET"], strict_slashes=False)
def link_decoer():
    """
    Decodes the link and return the link instance
    """

    link = request.args.get("link")
    if not link:
        return jsonify({"message": "link is required"}), 400
    url = f"http://localhost:5000/api/v1/power-partner/decoder?link={link}"
    link_instance = PowerPartnerLink.query.filter_by(link_url=url).first()
    if not link_instance:
        return jsonify({"message": "link not found"}), 404
    link_dict = {
        "id": link_instance.id,
        "link_url": link_instance.link_url,
        "type": link_instance.link_type,
        "active": link_instance.is_active,
        "generated": link_instance.generated_date,
        "price": link_instance.link_price,
        "user_id": link_instance.user_id,
        "count": link_instance.usage_count,
    }
    if not link_instance.is_active:
        return jsonify({"status": "error", "message": "expired link requested"})
    link_instance.usage_count += 1
    db.session.commit()

    return jsonify(link_dict), 200
