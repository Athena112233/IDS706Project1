from fastapi.testclient import TestClient
from fastapi import FastAPI
from main import app
import pytest
import requests
from bs4 import BeautifulSoup

client = TestClient(app)

def test_main():
    # test root function
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Proceed to IP/docs to enter testing values"}
    
    # test get recipe function
    response = client.get("/get_recipe/milk")
    result = {}
    url = requests.get("https://www.allrecipes.com/search/results/?search=milk")
    soup = BeautifulSoup(url.content, features="html.parser")
    top10_rep = soup.find_all("a", class_ = "card__titleLink manual-link-behavior")[:10]
    count = 1
    
    for link in top10_rep:
        n = "Recipe %d" % count
        count += 1
        result[n] = link['href']
    
    assert response.status_code == 200
    assert response.json() != {}
    assert response.json() == result