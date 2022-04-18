#!/usr/bin/python3
"""
this code is just to get proper linting
"""

from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)


def check_card(func):
    """
    this code validates the credit card transactions
    """
    wraps(func)

    def validation(*args, **kwargs):
        data = request.get_json()
        if not data.get("status"):
            response = {"approved": False, "newLimit": data.get(
                "limit"), "reason": "Blocked Card"}
            return jsonify(response)
        if data.get("limit") < data.get("transaction").get("amount"):
            response = {"approved": False, "newLimit": data.get(
                "limit"), "reason": "Transaction above the limit"}
            return jsonify(response)
        return func(*args, **kwargs)
    return validation


@ app.route("/api/transaction", methods=["POST"])
@ check_card
def transaction():
    """
    this code is responsible to expose endpoint for receiving the incoming transactions
    """
    card = request.get_json()
    new_limit = card.get("limit") - card.get("transaction").get("amount")
    response = {"approved": True, "newLimit": new_limit}
    return jsonify(response)


if __name__ == '_main_':
    app.run(debug=True)
