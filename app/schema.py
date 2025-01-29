#!/usr/bin/env python3

"""Defines the schemas for the app."""


from pydantic import BaseModel, EmailStr

from lib.current_datetime import current_datetime


class BasicInfo(BaseModel):
    """Defines the fields required to return the basic information."""

    email: EmailStr = "email@example.com"
    current_datetime: str = current_datetime()
    github_url: str = "https://github.com/nanafox/hng-stage-zero-api"
