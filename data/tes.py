#!python
import pandas as pd


base = pd.read_csv('./data/logbook.csv')

print(base.head())

print(base[0]['content'].decode())