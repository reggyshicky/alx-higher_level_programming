#!/usr/bin/python3
"""Module that prevents the user from creating other attributes"""


class LockedClass():
    """defines the LockedClass class"""
    __slots__ = "first_name"
