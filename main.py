from fastapi import FastAPI
import uvicorn
import requests
from bs4 import BeautifulSoup
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Proceed to IP/docs to enter testing values"}

@app.get("/get_recipe/{name}")
def get_recipe(name:str):
    result = {}
    path = "https://www.allrecipes.com/search/results/?search=" + name
    url = requests.get(path)
    soup = BeautifulSoup(url.content)
    top10_rep = soup.find_all("a", class_ = "card__titleLink manual-link-behavior")[:10]
    count = 1
    for link in top10_rep:
        n = "Recipe %d" % count
        count += 1
        result[n] = link['href']
    return result
    
client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Proceed to IP/docs to enter testing values"}
    
    response = client.get("/get_recipe/milk")
    assert response.status_code == 200
    assert response.json() != {}
    
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')
    test_main()
