#!/usr/bin/env python
"""
    This module contains the functions that are used to generate unique link strings.
    this servers as a utility module for the power partner link generation handler.

    file: power_partner.py
    Author: Yaekob Demisse
    Date: June 15 2023 08:30
"""


import secrets
import string


def generate_unique_link_string(length):
    """This function generates unique link strings."""
    characters = string.ascii_letters + string.digits
    unique_strings = set()

    while len(unique_strings) < length:
        link_string = "".join(secrets.choice(characters) for _ in range(20))
        unique_strings.add(link_string)

    return unique_strings
