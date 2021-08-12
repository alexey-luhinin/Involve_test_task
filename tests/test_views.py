'''Tests for views.py'''
import pytest
from app import app


def get_page(URI: str):
    return app.test_client().get(URI, follow_redirects=True)


def test_get_index_status_code():
    assert get_page('/').status_code == 200
