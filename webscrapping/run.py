from app.db.connection import get_conn
import _sqlite3
import pandas as pd
import time
import pyautogui as pag
import re

conn = get_conn()
cursor = conn.cursor()




# df = pd.read_excel(r"webscrapping/assetsCnpjNone.xlsx")

# df["cnpj"] = df["cnpj"].astype(str).str.strip()
# pattern = re.compile(
#     r'^([0-9]{14}|[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2})$'
# )

# for item in df.itertuples(index=False):
#     ticker = item[1]
#     cnpj = item[2]

#     if pattern.match(cnpj):
#         cursor.execute(
#             "UPDATE assets SET cnpj = %s WHERE ticker = %s",
#             (cnpj, ticker)
#         )

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
    