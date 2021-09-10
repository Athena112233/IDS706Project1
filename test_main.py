from fastapi.testclient import TestClient
from fastapi import FastAPI
from main import app
import pytest

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Proceed to IP/docs to enter testing values"}
    
    response = client.get("/get_recipe/milk")
    assert response.status_code == 200
    assert response.json() != {}
