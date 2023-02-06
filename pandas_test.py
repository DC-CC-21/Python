import pandas as pd
from random import randint
from time import strptime
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
# data_url = "http://lib.stat.cmu.edu/datasets/boston"


def reformat_flights_data():
    data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
    df = pd.read_csv(data_url)

    df['dates'] = [
        datetime.date(df.loc[i, 'year'], int(strptime(str(df.loc[i, 'month']), '%B').tm_mon), randint(1,26)) for i in range(len(df['month']))]# f"{randint(1,26):02d}/{int(strptime(str(df.loc[i, 'month']), '%B').tm_mon):02d}/{df.loc[i, 'year']}") for i in range(len(df['month']))]
    df = df.drop('year', axis=1)
    df = df.reindex(sorted(df.columns), axis=1)
    print(df.head(10))
    df.to_excel('pandas_test_data.xlsx', index=False)
# reformat_flights_data()
df = pd.read_excel('pandas_test_data.xlsx')
df['formatted_year'] = df['dates'].dt.year
df['formatted_month'] = df['dates'].dt.month_name()
df['formatted_day'] = df['dates'].dt.day_name()


print(df)

sns.lineplot(data=df, x='month', y='passengers', palette='tab10')
# plt.show()

# from pydataset import data
# import pydataset

# import seaborn as sns
# from sklearn import datasets
# query ='sunspot.year'
# print(pydataset.find_similar(query))
# print(data(query))
