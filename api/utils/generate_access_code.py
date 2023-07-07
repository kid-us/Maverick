#!/usr/bin/env python
"""
    This module contain a function which is responsible for generating
    an access codes for tournament
    
    file: generate_access_code.py
    Author: Yaekob Demisse
    Date: July 5 2023
"""

from random import randint


def generate_access_string(number_of_players: int) -> str:
    """generate random access code."""

    collector = set()
    while len(collector) < number_of_players:
        collector.add(randint(100000, 999999))

    intger_list = [str(code) for code in collector]

    return ",".join(intger_list)
