from fastapi import FastAPI,Form
from src.main import *
import uvicorn

app=FastAPI()
sentiment=Sentiment()

@app.post('/get_sentiments')
async def get_sentiments(feddit_id=Form(None),skip=Form(None),limit=Form(None)):
    return sentiment.get_senti(feddit_id=feddit_id,limit=limit,skip=skip)

if __name__ == "__main__":
    uvicorn.run(app)
