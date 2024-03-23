# Reddit Comment Sentiment Analysis API

This FastAPI application offers a RESTful API to analyze comments from a given subreddit or category and determine their sentiment.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/my_fastapi_project.git
   
   
Install dependencies:

pip install -r requirements.txt
Usage:

1. Start the FastAPI application:
   ```bash
   uvicorn app.main:app --reload
   
2. Access the API documentation at http://localhost:8000/docs to view available endpoints and test the API.

Endpoints

   #### GET /get_sentiments : Gets most recent feddit comments with the sentiment score.

#### Parameters:

    feddit_id: feddit Id for comments.
  
    limit: top number of rows.
  
    skip: skip
  
#### Response:

    List of comments with their unique identifiers, text, polarity scores, and classifications.

Additional Information:

The sentiment analysis logic can be found in src/main.py.
Each API call has a unique request_id that can be mapped back to logs for monitoring



For more details email to : pratgupta35@gmail.com
