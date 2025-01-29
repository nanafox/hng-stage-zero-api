#!/usr/bin/env python3

"""This module contains the configuration for the app."""

from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Contains the configuration for the app."""

    email_address: EmailStr
    github_repo_url: str
    model_config = SettingsConfigDict(env_file=".env")
