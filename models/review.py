#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the Review class."""

    place_id = ""
    user_id = ""
    text = ""