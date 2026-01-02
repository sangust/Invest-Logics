from app.db.connection import get_conn
import pandas as pd
import time
import pyautogui as pag
import re

conn = get_conn()
cursor = conn.cursor()
data=pd.read_sql("SELECT cnpj FROM assets", conn)

df = pd.read_csv("webscrapping/dfp_cia_aberta_composicao_capital_2024.csv",encoding="latin-1", sep=";")#valor total está correto
df_db = pd.read_sql("SELECT ticker, cnpj from assets", conn)
lista=[]
for item in df.itertuples():
    cnpjs = df_db[df_db["cnpj"]==item[1]]
    if item[5] != 0:
        for ticker in df_db.itertuples():
           if ticker[2] == item[1] and not ticker[1].endswith(("4", "6", "5", "11")):
            lista.append({"ticker":ticker[1], "qtd_acoes":item[5]-item[8]})    

df_acoes= pd.DataFrame(lista)
df_acoes.to_excel("acoes_ordinarias.xlsx")

# df = pd.read_sql("SELECT * FROM assets", conn)
# for item in df.itertuples(index=False):
#     if item[3] =='None' or item [2]=="nan":
#         for y in data:
#             if item[0] == y[0]:
#                 df.loc[df["ticker"] == item[1], ["cnpj", "nome"]] = [
#                 y[2],y[3]] 


# for item in df.itertuples(index=False):
#     if item[3] =='None' or item [2]=="nan":
#         for y in data:
#             if item[0] == y[0]:
#                 df.loc[df["ticker"] == item[1], ["cnpj", "nome"]] = [
#                 y[2],y[3]]        
                



# df["cnpj"] = df["cnpj"].astype(str).str.strip()
# pattern = re.compile(
#     r'^([0-9]{14}|[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2})$'
# )

# for item in df.itertuples(index=False):
#     ticker = item[1]
#     cnpj = item[2]
#     nome = item[3]
#     if pattern.match(cnpj):
#         cursor.execute("UPDATE assets SET cnpj = %s, nome=%s  WHERE ticker = %s", (cnpj, nome, ticker))

# conn.commit()


# pag.moveTo(1210, 47)
# pag.click()
# time.sleep(0.5)
# pag.moveTo(650, 147)
# time.sleep(0.5)
# pag.click()
# time.sleep(0.05)
# pag.click()
# time.sleep(0.5)

# for item in df.itertuples():
#     pag.hotkey("Ctrl", "c")
#     pag.moveTo(x=982, y=1052)
#     pag.click()
#     time.sleep(0.5)
#     pag.moveTo(1036,947)
#     pag.click()
#     pag.moveTo(495, 58)
#     time.sleep(0.5)
#     pag.click()
#     time.sleep(0.5)
#     pag.click()

#     if item[0] in (7,46,50,72,76,91):
#         pag.press("Backspace")
#         pag.press("Backspace")
#         pag.press("Backspace")
#         pag.press("Backspace")
#         pag.press("Backspace")
#         pag.press("Backspace")
#     else:
#         pag.press("Backspace")
#         pag.press("Backspace")
#         pag.press("Backspace")
#         pag.press("Backspace")
#         pag.press("Backspace")
    
#     pag.hotkey("Ctrl", "v")
#     pag.press("Enter")
#     time.sleep(10)
#     pag.moveTo(993, 562)
#     pag.mouseDown()
#     time.sleep(0.1)
#     pag.moveTo(993, 593, duration=0.3)
#     pag.mouseUp()
#     pag.hotkey("Ctrl", "c")
#     time.sleep(0.2)

#     pag.moveTo(1038,594)
#     pag.mouseDown()
#     time.sleep(0.2)
#     pag.moveTo(x=992, y=636, duration=0.5)
#     pag.mouseUp()
#     pag.hotkey("Ctrl", "c")

#     pag.moveTo(x=1108, y=1062)
#     pag.click()
#     time.sleep(0.2)
#     pag.moveTo(1224,51)
#     pag.click()
#     time.sleep(0.2)
#     pag.press("Tab")
#     time.sleep(0.4)
#     pag.press("Tab")
#     time.sleep(0.2)
#     pag.hotkey("Ctrl", "v")
#     time.sleep(0.5)
#     pag.press("Tab")
#     time.sleep(0.5)
#     pag.hotkey("Win", "v")
#     time.sleep(0.5)
#     pag.press("down")
#     time.sleep(0.2)
#     pag.press("Enter")
#     time.sleep(0.5)
#     pag.press("tab")
#     time.sleep(0.2)
#     pag.press("tab")
#     time.sleep(0.1)
#     pag.press("space")
#     time.sleep(1)
#     pag.hotkey("Ctrl", "a")
#     time.sleep(5)
    