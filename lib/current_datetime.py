#!/usr/bin/env python3

"""This module contains a simple function to return the current time in ISO
8601 format."""

from datetime import datetime, timezone


def current_datetime() -> str:
    """Returns the current date and time in ISO 8601 format."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
