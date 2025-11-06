from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("patients.json") as f:
        data = json.load(f)
    return data

@app.get("/")
async def hello():
    return {"message": "Patient management system"}

@app.get("/about")
async def about():
    return {"message": "About Page"}    


@app.get('/view')
async def view_patients():
    data = load_data()
    return data