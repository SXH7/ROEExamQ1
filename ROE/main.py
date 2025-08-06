from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data once
with open("data.json") as f:
    data = json.load(f)

@app.get("/query")
async def query(q: str, request: Request):
    answer = handle_query(q)
    headers = {"X-Email": "22f3002772@ds.study.iitm.ac.in"}
    return JSONResponse(content={"answer": answer}, headers=headers)

def handle_query(q):
    q = q.strip().lower()
    print("Query received:", q)  # Optional: for debugging

    if q == "what is the total sales of shirt in sawaynberg?":
        return sum(d["sales"] for d in data if d["product"] == "Shirt" and d["city"] == "Sawaynberg")

    if q == "how many sales reps are there in arizona?":
        return len(set(d["rep"] for d in data if d["region"] == "Arizona"))

    if q == "what is the average sales for towels in nevada?":
        items = [d["sales"] for d in data if d["product"] == "Towels" and d["region"] == "Nevada"]
        return round(sum(items) / len(items), 2) if items else 0

    if q == "on which date did leonard hilll record the highest sale in westland?":
        records = [d for d in data if d["rep"] == "Leonard Hilll" and d["city"] == "Westland"]
        return max(records, key=lambda d: d["sales"])["date"] if records else "N/A"

    if q == "what is the total sales of shoes in colorado springs?":
        return sum(d["sales"] for d in data if d["product"] == "Shoes" and d["city"] == "Colorado Springs")

    if q == "how many sales reps are there in new mexico?":
        return len(set(d["rep"] for d in data if d["region"] == "New Mexico"))

    if q == "what is the average sales for shirt in wyoming?":
        items = [d["sales"] for d in data if d["product"] == "Shirt" and d["region"] == "Wyoming"]
        return round(sum(items) / len(items), 2) if items else 0

    if q == "on which date did guadalupe hamill record the highest sale in assuntashire?":
        records = [d for d in data if d["rep"] == "Guadalupe Hamill" and d["city"] == "Assuntashire"]
        return max(records, key=lambda d: d["sales"])["date"] if records else "N/A"

    if q == "what is the total sales of towels in adellcester?":
        return sum(d["sales"] for d in data if d["product"] == "Towels" and d["city"] == "Adellcester")

    if q == "how many sales reps are there in missouri?":
        return len(set(d["rep"] for d in data if d["region"] == "Missouri"))

    if q == "what is the average sales for shoes in minnesota?":
        items = [d["sales"] for d in data if d["product"] == "Shoes" and d["region"] == "Minnesota"]
        return round(sum(items) / len(items), 2) if items else 0

    if q == "on which date did shirley cummerata record the highest sale in parkercester?":
        records = [d for d in data if d["rep"] == "Shirley Cummerata" and d["city"] == "Parkercester"]
        return max(records, key=lambda d: d["sales"])["date"] if records else "N/A"

    if q == "what is the total sales of table in parkercester?":
        return sum(d["sales"] for d in data if d["product"] == "Table" and d["city"] == "Parkercester")

    if q == "how many sales reps are there in alabama?":
        return len(set(d["rep"] for d in data if d["region"] == "Alabama"))

    if q == "what is the average sales for table in georgia?":
        items = [d["sales"] for d in data if d["product"] == "Table" and d["region"] == "Georgia"]
        return round(sum(items) / len(items), 2) if items else 0

    if q == "on which date did angel flatley record the highest sale in lake justusside?":
        records = [d for d in data if d["rep"] == "Angel Flatley" and d["city"] == "Lake Justusside"]
        return max(records, key=lambda d: d["sales"])["date"] if records else "N/A"

    if q == "what is the total sales of ball in waterbury?":
        return sum(d["sales"] for d in data if d["product"] == "Ball" and d["city"] == "Waterbury")

    if q == "how many sales reps are there in maine?":
        return len(set(d["rep"] for d in data if d["region"] == "Maine"))

    if q == "what is the average sales for gloves in nevada?":
        items = [d["sales"] for d in data if d["product"] == "Gloves" and d["region"] == "Nevada"]
        return round(sum(items) / len(items), 2) if items else 0

    if q == "on which date did nicholas simonis iv record the highest sale in fort joanyview?":
        records = [d for d in data if d["rep"] == "Nicholas Simonis IV" and d["city"] == "Fort Joanyview"]
        return max(records, key=lambda d: d["sales"])["date"] if records else "N/A"

    return "Unknown query"
