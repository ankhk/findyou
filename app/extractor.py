import webstruct
import pickle
import requests
import json


def token_identity(html_token):
    return {'token': html_token.token}

def token_isupper(html_token):
    return {'isupper': html_token.token.isupper()}

def parent_tag(html_token):
    return {'parent_tag': html_token.parent.tag}

def border_at_left(html_token):
    return {'border_at_left': html_token.index == 0}


class Extractor:
    def __init__(self):
        """load model"""    
        with open("model_fit.pkl", "rb") as fin:
            model = pickle.load(fin)
            self.ner = webstruct.NER(model)


    def get_from_html(self, html):
        result = self.ner.extract(html)
        result_dict = dict()
        for el in result:
            result_dict[el[0]] = el[1]
        return json.dumps(result_dict, ensure_ascii=False)


    def get_from_url(self, url):
        response = requests.get(url)
        result = json.loads(self.get_from_html(response.text))
        return result