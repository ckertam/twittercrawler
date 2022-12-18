from pickle import FALSE
import twint
import nest_asyncio
import pandas as pd
import re
import regex
import numpy as np
# from progress.bar import Bar
from datetime import datetime
import inflect
# from sklearn.cluster import KMeans


#nest_asyncio.apply()
p = inflect.engine()

d = twint.Config()
#Usernames = ["espn","cnn","UN","BBCWorld","nytimes","HillaryClinton","Oprah","BarackObama","narendramodi","enews","netflix","maggieNYT","elonmusk","DalaiLama","NASA","twitter","TheEllenShow","jimmyfallon","Google"]
#Usernames = ["teamyoutube","mcdonalds","guardian","business","wwf","bbcsport","dcexaminer"]
d.Limit = 60
d.Pandas = True
d.Lang = 'en'
d.Hide_output = True
d.Since = "2022-01-01 00:00:00"     #First Crawl Date 22.09.2022 
d.Username = "mansuryavas06"

twint.run.Search(d)
Tweets_df = twint.storage.panda.Tweets_df
Tweets_df.to_excel("TestExcel.xlsx", index=False)
print(Tweets_df)
