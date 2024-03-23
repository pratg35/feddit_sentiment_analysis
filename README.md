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


uvicorn app.main:app --reload
2. Access the API documentation at http://localhost:8000/docs to view available endpoints and test the API.

Endpoints

/comments/{subreddit}: Get the most recent 25 comments from the specified subreddit.

Parameters:
subreddit: Name of the subreddit (e.g., "python").
Response:
List of comments with their unique identifiers, text, polarity scores, and classifications.

Additional Information

The sentiment analysis logic can be found in app.sentiment_analysis.py.
For more details, refer to the FastAPI documentation: https://fastapi.tiangolo.com/
sql
Copy code
