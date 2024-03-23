from transformers import pipeline
import requests
import datetime
import uuid


class Sentiment:
    def __init__(self):
        self.tf_obj = pipeline("sentiment-analysis")
    
    
    def get_api_data(self,feddit_id,skip,limit):
        url = f"https://literate-goggles-x65qvrx9pvwfp9j7-8080.app.github.dev/api/v1/comments/?subfeddit_id={feddit_id}&skip={skip}&limit={limit}"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        # print(response.json())
        results=response.json()
        return results

    def get_senti(self,feddit_id,limit,skip):
        request_id = str(uuid.uuid4())
        results={}
        try:
            results=self.get_api_data(feddit_id,skip,limit)
            text=[i['text'] for i in results['comments']]
            sent=self.tf_obj(text)
            # print(sent)
            for i in range(len(results.get("comments"))):
                # results['comments'][i].update(sent[i])
                results['comments'][i]["label"]=sent[i]["label"]
                results['comments'][i]["score"]=sent[i]["score"]
                # print(results['comments'][i])
            print("INFO: "+request_id +" : "+ str(datetime.datetime.now())+": Response: " +str(results['comments']))
            results["request_id"]=request_id
        except Exception as e:
            print("ERROR: "+request_id +" : "+ str(datetime.datetime.now())+": Error: " +str(e))
            results["request_id"]=request_id
            results["error"]=str(e)

        return results


if __name__=='__main__':
    sentiment=Sentiment()
    feddit_id=1
    limit=10
    skip=0
    print(sentiment.get_senti(feddit_id,limit,skip))




    

        