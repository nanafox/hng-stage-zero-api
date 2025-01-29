#!/usr/bin/env python3

"""Tests for the main module."""

from fastapi import status
from fastapi.testclient import TestClient

from app.main import app, get_settings
from app.schema import BasicInfo
from config.app import Settings
from lib.current_datetime import current_datetime

client = TestClient(app)

current_datetime = current_datetime()


def get_settings_override():
    return Settings(
        email_address="example@example.com",
        github_repo_url="https://github.com/nanafox/hng-stage-zero-api",
    )


app.dependency_overrides[get_settings] = get_settings_override


def test_root_endpoint():
    """Test that the root endpoint returns the correct status code and
    response."""
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK

    schema_response: BasicInfo = BasicInfo(**response.json())

    assert schema_response.email == "example@example.com"
    assert (
        schema_response.github_url
        == "https://github.com/nanafox/hng-stage-zero-api"
    )

    assert schema_response.current_datetime is not None


def test_post_on_root_endpoint():
    """Test that POST requests fail."""
    response = client.post("/")

    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
