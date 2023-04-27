from app.core.Controller import Controller
from app.core.Response import Response
import logging
import json
import requests
from app.consts import Consts

class TextManipulation(Controller):

    def checkSimilarity(self,language,algorithm,firstText,secondText,output):


        firstTextSplit = firstText.split('.')
        secondTextSplit = secondText.split('.')

        firstTextType = 'sentence' if len(firstTextSplit) == 2 else 'paragraph'
        secondTextType = 'sentence' if len(secondTextSplit) == 2 else 'paragraph'

        firstTextSentencesCount = len(firstTextSplit)
        secondTextSentencesCount = len(secondTextSplit)


        url = Consts.ALGO_SERVER+Consts.CALCULATE_SIM
        params = {'language': language,'algorithm' : algorithm, 'firstText' : firstText
                 , 'secondText' : secondText,  'firstTextType' : firstTextType, 
                 'firstTextSentencesCount' : firstTextSentencesCount , 'secondTextType' : secondTextType, 
                 'secondTextSentencesCount' : secondTextSentencesCount}

        response = requests.post(url, data = params)

        data = response.json()

        responseBody = json.dumps({
            'success': True,
            'similarity_score' : data['similarity_score'] if output == '1' or output == '3' else '',
            'similar_calculation_explination' : data['similar_calculation_explination'] if output == '2' or output == '3' else ''
        })
        return Response(body=responseBody)