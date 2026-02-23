from copy import deepcopy
import pytest

from fastapi.testclient import TestClient

from src.app import app, activities as activities_store


@pytest.fixture
def client():
    """Arrange: provide a TestClient for the FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Arrange: snapshot and restore the in-memory activities between tests"""
    original = deepcopy(activities_store)
    try:
        yield
    finally:
        activities_store.clear()
        activities_store.update(original)
