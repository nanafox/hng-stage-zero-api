#!/usr/bin/env python3

"""This module defines the API endpoint that returns the basic information as
requested by the task."""

from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from app.schema import BasicInfo
from config.app import Settings
from lib.current_datetime import current_datetime

app = FastAPI(
    version="v1",
    title="Maxwell Nana Forson | HNG Stage Zero API",
    description="API documentation for the HNG Stage Zero task, providing "
    "detailed information on endpoints and usage.",
    contact={
        "name": "Maxwell Nana Forson",
        "portfolio": "https://www.mnforson.live",
        "email": "nanaforsonjnr@rmail.com",
    },
    docs_url="/swagger-doc",
    redoc_url="/docs",
)


@lru_cache
def get_settings():
    """Get the settings for the application."""
    return Settings()


app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["GET", "HEAD"]
)


@app.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Return Basic Info",
    response_model=BasicInfo,
)
async def root(
    settings: Annotated[Settings, Depends(get_settings)],
) -> BasicInfo:
    """Returns information about the current date and time, my email address
    and the GitHub Repo URL that houses the code for this project."""
    return BasicInfo(
        email=settings.email_address,
        current_datetime=current_datetime(),
        github_url=settings.github_repo_url,
    )
