from fastapi import FastAPI,Form
from src.main import *
import uvicorn
from fastapi_health import health

def healthy_condition():
    return {"healthy": True}


def healthy():
    return True

def sick():
    return False

app = FastAPI()
app.add_api_route("/health", health([healthy_condition, healthy]))

sentiment=Sentiment()

@app.get('/get_sentiments')
async def get_sentiments(feddit_id=Form(None),skip=Form(None),limit=Form(None)):
    return sentiment.get_senti(feddit_id=feddit_id,limit=limit,skip=skip)

if __name__ == "__main__":
    uvicorn.run(app)
