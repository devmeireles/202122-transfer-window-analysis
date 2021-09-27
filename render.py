import pandas as pd
import os

df = pd.read_csv('./data/data.csv')
print(df.head(40))

df = df[df.fee.apply(lambda x: x.isnumeric())]
df['fee'] = df['fee'].apply(int)

profits = df.groupby(by=['country_from'])['fee'].sum().reset_index()
profits.sort_values(by='fee', ascending=False)
print(profits.head(10))

spendthrift = df.groupby(by=['country_to'])['fee'].sum().reset_index()
spendthrift.sort_values(by='fee', ascending=False)
print(spendthrift.head(10))


transfers_per_country_from = df.groupby(by=[
    'country_from',
    'country_to'
    ]).size().reset_index()

print(transfers_per_country_from.head(10))


transfers_per_country_to = df.groupby(by=[
    'country_to',
    'country_from'
    ]).size().reset_index()

print(transfers_per_country_to.head(10))