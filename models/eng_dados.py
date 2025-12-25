import os
import sqlite3
import pandas as pd


df = pd.read_csv(r"csvs\aberta2010\dfp_cia_aberta_BPP_con_2010.csv", encoding="latin 1", sep=";")
df = df[df["DENOM_CIA"]=='ROMI S.A.']
for i in df.itertuples():
    print(i[-3], i[-4])