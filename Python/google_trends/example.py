# https://towardsdatascience.com/google-trends-api-for-python-a84bc25db88f

import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()

#Categories
#Business and Industrial - 12
#Business news - 784
pytrend.build_payload(kw_list=["TQQQ"], timeframe='now 7-d', cat=12)

df = pytrend.interest_over_time()
df.to_html("interest_over_time.html")
print (df)

'''
df = pytrend.get_historical_interest(keywords=['TQQQ'], year_start=2018, month_start=1, day_start=1, hour_start=0, year_end=2020, month_end=11, day_end=15, hour_end=0)
df.to_html("historical_interest.html")
print (df)

df = pytrend.interest_by_region()
print (df)
df.to_html("temp.html")
#print(df.head(150))

related_queries = pytrend.related_queries()
print (related_queries.values())

related_topics = pytrend.related_topics()
print (related_topics.values())

keywords = pytrend.suggestions(keyword='TQQQ')
df = pd.DataFrame(keywords)
df.drop(columns='mid')
print (df)



df = pytrend.trending_searches(pn='united_states')
#print (df.head())

df = pytrend.today_searches(pn='US')
#print (df.head())

df = pytrend.top_charts(2020, hl='en-US', tz=300, geo='GLOBAL')
#print (df.head())
'''
