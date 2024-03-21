from transformers import pipeline
import requests


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
        results=self.get_api_data(feddit_id,skip,limit)
        # print(results)
        text=[i['text'] for i in results['comments']]
        sent=self.tf_obj(text)
        # print(sent)
        for i in range(len(results)):
            results['comments'][i].update(sent[i])
        return results['comments']

if __name__=='__main__':
    sentiment=Sentiment()
    feddit_id=1
    limit=10
    skip=0
    print(sentiment.get_senti(feddit_id,limit,skip))




    

        