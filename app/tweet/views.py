from pickle import FALSE
from . import twint
import nest_asyncio
import pandas as pd
import re
import regex
import numpy as np
# from progress.bar import Bar
from datetime import datetime
import inflect
# from sklearn.cluster import KMeans
import os
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
import requests
import json
class GetTweetsAPIView(APIView):
    def post(self,request,*args,**kwargs):
        username=request.data.get("username")
        since_date = request.data.get("since_date")
        d = twint.Config()
        #Usernames = ["espn","cnn","UN","BBCWorld","nytimes","HillaryClinton","Oprah","BarackObama","narendramodi","enews","netflix","maggieNYT","elonmusk","DalaiLama","NASA","twitter","TheEllenShow","jimmyfallon","Google"]
        #Usernames = ["teamyoutube","mcdonalds","guardian","business","wwf","bbcsport","dcexaminer"]
        d.Limit = 1000
        d.Pandas = True
        
        d.Hide_output = True
        d.Since = since_date     #First Crawl Date 22.09.2022 
        d.Username = username
        d.Lang = 'en'

        twint.run.Search(d)
        Tweets_df = twint.storage.panda.Tweets_df
        Tweets_df.to_excel("../TestExcel.xlsx", index=False)
        payload = {
            "username":username,
            "since_date":since_date,
            "tweets":Tweets_df["tweet"].values.tolist()
        }
        sentiment_analysis = requests.post(url="http://34.27.20.191:8000/analyze/",json=(payload))
        # print(Tweets_df)
        return Response(sentiment_analysis.json(), status=200)


class GetTweetsSimulationAPIView(APIView):
    def post(self,request,*args,**kwargs):
        username=request.data.get("username")
        since_date = request.data.get("since_date")
        data = request.data.get("data")
        file_path = os.path.abspath("app/tweet/TestExcel.xlsx")
        # df = pd.read_excel(file_path)
        df = pd.read_excel("/TestExcel.xlsx")
        # tweet = df["tweet"].values.tolist()
        payload = {
            "username":username,
            "since_date":since_date,
            "tweets":df["tweet"].values.tolist()
        }
        sentiment_analysis = requests.post(url="http://34.27.20.191:8000/analyze/",json=(payload))

        return Response(sentiment_analysis.json(), status=200)

