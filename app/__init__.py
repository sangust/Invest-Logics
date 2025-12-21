import pandas as pd
import sqlite3
import requests
from datetime import datetime
import google.generativeai as genai
import os
import json

conn = sqlite3.connect("models/BancoDadosAcionario.db")
cursor = conn.cursor()
ticker_api = requests.get("https://ledev.com.br/api/cotacoes/").json()
hora = datetime.now()
hora = hora.strftime("%H:%M")

# genai.configure(api_key="AIzaSyANY1MPpK2GoZY8Y1CPW6KAiW3JLHcafhk")

# model = genai.GenerativeModel('gemini-2.5-flash')
# df = pd.read_sql_query("SELECT Ticker FROM Acoes", conn)
# for ticker in df.itertuples():
#     response = model.generate_content('''Você é uma API financeira institucional de alta precisão.

#     Sua função é retornar o LPA (Lucro por Ação) ANUAL em VALOR ABSOLUTO do ticker informado, para TODOS os anos disponíveis.

#     PROCESSO OBRIGATÓRIO DE APURAÇÃO:
#     - Consulte e confronte dados de NO MÍNIMO 10 fontes financeiras respeitadas e independentes.
#     - Fontes aceitáveis incluem, mas não se limitam a: relatórios oficiais da empresa (DFP/ITR), CVM, B3, Economatica, Status Invest, Fundamentus, Investsite, Yahoo Finance, Morningstar, TradingView, Reuters, Bloomberg ou equivalentes institucionais.
#     - Caso haja divergência entre fontes:
#       - Utilize o valor mais recorrente entre as fontes.
#       - Se necessário, aplique média ponderada baseada na confiabilidade institucional.
#     - NÃO estime valores.
#     - NÃO projete dados futuros.
#     - NÃO arredonde indevidamente.
#     - Caso o LPA de um determinado ano não possa ser validado com ALTA confiança, esse ano NÃO deve ser retornado.

#     REGRAS CRÍTICAS SOBRE O LPA:
#     - O LPA retornado DEVE ser o valor ABSOLUTO (sempre positivo).
#     - Caso o LPA original seja negativo, retorne seu valor absoluto.
#     - O valor deve ser numérico (float).

#     FLAG DE CONFIABILIDADE:
#     - Inclua a chave "confiabilidade" com valores possíveis:
#       - "alta" → consenso claro entre fontes institucionais
#       - "media" → pequena divergência, mas valor validável
#       - "baixa" → NÃO PERMITIDO (não retorne o registro)

#     REGRAS DE SAÍDA (OBRIGATÓRIAS):
#     - Retorne APENAS JSON válido.
#     - NÃO escreva absolutamente nenhum texto fora do JSON.
#     - NÃO utilize markdown, explicações, comentários ou blocos de código.
#     - O JSON final deve ser um ARRAY de objetos.
#     - Cada objeto deve conter EXATAMENTE as seguintes chaves:
#       - "ticker" (string, em minúsculo)
#       - "ano" (inteiro)
#       - "lpa" (float, valor absoluto)
#       - "confiabilidade" (string: "alta" ou "media")
#     - Não altere nomes de chaves.
#     - Não inclua fontes, observações, metadados ou campos extras.
#     - A saída deve ser determinística, consistente e própria para ingestão automática em banco de dados.

#     FORMATO EXATO DE SAÍDA:
#     [
#       {"ticker":"bbas3","ano":2010,"lpa":0.00,"confiabilidade":"alta"},
#       {"ticker":"bbas3","ano":2011,"lpa":0.00,"confiabilidade":"media"}
#     ]

#     "TICKER: "
#     '''+str(ticker[1]))

#     json_str = response.text
#     json_str = json_str.replace("```json", "").replace("```", "").strip()
#     dados = json.loads(json_str)
#     for response in dados:
#         cursor.execute("INSERT INTO Demonstrativos (Ticker, ano, lpa) VALUES (?,?,?)", (response["ticker"], response["ano"], response["lpa"]))



# df = pd.read_sql_query("SELECT * FROM Demonstrativos", conn)
# df.to_csv("models/lpas.csv")

# cursor.execute("DELETE FROM Demonstrativos")
# df = pd.read_csv("LPA_Corrigido_Yahoo.csv",sep=";", decimal=",")

# for item in df.itertuples():
#     valores = item[0]
#     valores = {
#         "lpa": item[-1],
#         "Ticker": item[1],
#         "ano": item[2]
#     }
#     cursor.execute("INSERT INTO Demonstrativos (lpa, Ticker, ano) VALUES (?,?,?)", (valores["lpa"], valores["Ticker"], valores["ano"]))
# conn.commit()
    
# df = pd.read_sql_query("SELECT * FROM Demonstrativos", conn)
# df.to_csv("models/LPA.csv")

# import yfinance as yf
# import pandas as pd
# import datetime

# cursor.execute("SELECT Ticker FROM Acoes")
# tickers_br = cursor.fetchall()

# dados_lpa = []


# for ticker in tickers_br:
#     ticker = ticker[0].upper() + ".SA"
#     try:
#         print(f"Baixando: {ticker}...")
#         acao = yf.Ticker(ticker)
        
#         balanco = acao.financials
#         balanco = balanco.T
        
#         if "Basic EPS" in balanco.columns:
#             eps_data = balanco["Basic EPS"]
#         elif "Diluted EPS" in balanco.columns:
#             eps_data = balanco["Diluted EPS"]
#         else:
#             try:
#                 lucro = balanco["Net Income"]
#                 acoes = balanco["Basic Average Shares"]
#                 eps_data = lucro / acoes
#             except:
#                 continue

#         for data, valor in eps_data.items():
#             dados_lpa.append({
#                 "Ticker": ticker.replace(".SA", ""), 
#                 "Ano": data.year,
#                 "LPA": valor
#             })
            
#     except Exception as e:
#         print(f"Erro ao processar {ticker}: {e}")

# df_novo = pd.DataFrame(dados_lpa)

# df_novo = df_novo.sort_values(by=["Ticker", "Ano"])

# arquivo_saida = "LPA_Corrigido_Yahoo.csv"
# df_novo.to_csv(arquivo_saida, index=False, sep=";", decimal=",")


# cursor.execute("SELECT Ticker FROM Acoes where Cnpj == 'None'")
# tickers = cursor.fetchall()
# lista_temp = []
# for ticker in tickers:
#     for letra in ticker[0]:
#         if letra in ["1","2","3","4","5","6","7","8","9"]:
#             new_ticker = ticker[0].replace(letra, "")
#     lista_temp.append(new_ticker)

# lista_temp2 = []
# for ticket in lista_temp:
#     try:
#         cursor.execute(f"SELECT Cnpj FROM Acoes where Ticker LIKE '{ticket}%'")       
#         dados = cursor.fetchall()
#         lista_temp2.append(dados[0])
#         print(f"CNPJ DO {ticket}: {dados}")
#     except:
#         pass


# add = [[i[0] for i in tickers], [y[0] for y in lista_temp2]]
# for item in range(len(add[0])):
#     cursor.execute(f"UPDATE Acoes SET Cnpj = '{add[1][item]}' where ticker = '{add[0][item]}'")
    



df_ticker = pd.read_excel("cms_files_148780_1710532689Empresas_da_B3.xlsx")
df_DRE10 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2010.csv", encoding="latin1", sep=";")
df_DRE11 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2011.csv", encoding="latin1", sep=";")
df_DRE12 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2012.csv", encoding="latin1", sep=";")
df_DRE13 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2013.csv", encoding="latin1", sep=";")
df_DRE14 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2014.csv", encoding="latin1", sep=";")
df_DRE15 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2015.csv", encoding="latin1", sep=";")
df_DRE16 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2016.csv", encoding="latin1", sep=";")
df_DRE17 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2017.csv", encoding="latin1", sep=";")
df_DRE18 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2018.csv", encoding="latin1", sep=";")
df_DRE19 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2019.csv", encoding="latin1", sep=";")
df_DRE20 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2020.csv", encoding="latin1", sep=";")
df_DRE21 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2021.csv", encoding="latin1", sep=";")
df_DRE22 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2022.csv", encoding="latin1", sep=";")
df_DRE23 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2023.csv", encoding="latin1", sep=";")
df_DRE24 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2024.csv", encoding="latin1", sep=";")
df_DRE25 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2025.csv", encoding="latin1", sep=";")

dados_anuais_acionarios = [df_DRE10, df_DRE11, df_DRE12, df_DRE13, df_DRE14, df_DRE15, df_DRE16, 
                           df_DRE17, df_DRE18, df_DRE19, df_DRE20, df_DRE21,df_DRE22, df_DRE23, df_DRE24, df_DRE25]

for i, dado in enumerate(dados_anuais_acionarios):
    for linha in dado.itertuples():
        if linha[-4] in ("3.99.01", '3.99.02') and linha[-2] != 0.0 :
            print(linha[4],linha[-3],linha[-2], i +2009)

# ano = 2009
# resultados = []
# for arquivo in dados_anuais_acionarios:
#     ano += 1
#     COD_LUCRO_LIQ = "3.11"

    
    
#     df_lucro = arquivo[
#     (arquivo['CD_CONTA'] == "3.11") &
#     (arquivo['DS_CONTA'].str.contains('Lucro', case=False, na=False))
#     ]

#     if 'ORDEM_EXERC' in arquivo.columns:
#         df_lucro = df_lucro[df_lucro['ORDEM_EXERC'] == 'ÚLTIMO']
#     elif 'DT_REFER' in arquivo.columns:
#         df_lucro = df_lucro[df_lucro['DT_REFER'].astype(str).str.endswith('12-31')]


    
#     for _, row in df_lucro.iterrows():
#         resultados.append({
#             "ticker": row['CNPJ_CIA'],
#             "ano": ano,
#             "lucro_liquido": float(str(row['VL_CONTA']).replace(',', '.'))
#         })

#     lucro_df = pd.DataFrame(resultados)

#     lucro_df = lucro_df.sort_values(['ticker', 'ano'])

#     lucro_df.to_csv("lucro_liquido_anual.csv", index=False)

#     print("Arquivo 'lucro_liquido_anual.csv' gerado com sucesso")

# import pandas as pd


# for i in dados_anuais_acionarios:
#     for y in i.itertuples():
#         print(y)
# df = pd.read_csv("lucro_liquido_anual.csv")

# df = (
#     df
#     .sort_values("ano")
#     .groupby(["ticker", "ano"], as_index=False)
#     .last()
# )

# df.to_csv("lucro_liquido_anual_limpo.csv", index=False)


# lpa = ("3.99.01.01", "3.99.01.02")
# demonstrativos = []
# cursor.execute("SELECT Ticker, Cnpj FROM Acoes where Cnpj <> 'None'")
# tickerlpa = cursor.fetchall()
# ano = 2009
# for dre in dados_anuais_acionarios:
#     ano +=1
#     dt_serv = [str(ano)+ "-12-31", str(ano)+ "-12-31"]
#     for empresa in dre.itertuples():
#         if empresa[-4] not in lpa or empresa[-5] not in dt_serv:
#             continue
#         else:
#             for item in tickerlpa:
#                 if item[1] != empresa[1]: # Verifica CNPJ
#                     continue
                
#                 ticker_atual = item[0]
#                 conta_atual = empresa[-4] # O código da conta (3.99.01.01 ou .02)
                
#                 # REGRA DE OURO: Verifica se o final do ticker bate com a conta
#                 final_ticker = ticker_atual[-1]
                
#                 match_valido = False
                
#                 # Se ticker termina em 3, só aceita conta final .01
#                 if final_ticker == '3' and conta_atual == '3.99.01.01':
#                     match_valido = True
                    
#                 # Se ticker termina em 4, 5 ou 6, só aceita conta final .02
#                 elif final_ticker in ['4', '5', '6'] and conta_atual == '3.99.01.02':
#                     match_valido = True
                    
#                 # Tratamento para Units (11) - Geralmente pega o PN (.02)
#                 elif final_ticker == '1' and conta_atual == '3.99.01.02': # Final 1 do '11'
#                     match_valido = True

#                 if match_valido:
#                     demonstrativos.append({
#                         "Cnpj": empresa[1], 
#                         "LPA": empresa[-2], 
#                         "Ano": ano, 
#                         "Ticker": ticker_atual,
#                         "Conta": conta_atual # Importante guardar para conferência
#                     })

# cursor.execute("DELETE FROM Demonstrativos")
# for lpa in demonstrativos:
#     cursor.execute("INSERT INTO Demonstrativos (Ticker, ano, lpa) VALUES (?,?,?)", (lpa["Ticker"], lpa["Ano"], lpa["LPA"]))
# conn.commit()



# empresasIBOV = []
# contador = 1


# for item in dados_anuais_acionarios:
#     match contador:
#         #Colocando o Ticker e CNPJ
#         case 1:
            
#             for empresa in item.itertuples():
#                 empresasIBOV.append({"Ticker": empresa[1], "Cnpj": str(empresa[-1]), "Hr_Atualizacao": hora})

#             emp = set(i["Ticker"] for i in empresasIBOV)
#             for i in ticker_api:
#                 if i["id"] not in emp:
#                     empresasIBOV.append({"Ticker": i["id"], "Pc_Atual":i["price"], "Nm_Empresarial":"None", "Cnpj":"None", "Hr_Atualizacao":hora})
            
            
        # case _:
        #     #Colocando o nome empresarial
        #     for linha in item.itertuples():
        #         for i in range(0, len(empresasIBOV)):
        #             if linha[1] == empresasIBOV[i]["Cnpj"]:
        #                 if "Nm_empresarial" not in empresasIBOV[i]:
        #                     empresasIBOV[i]["Nm_Empresarial"] = linha[4]
                        
                    


                        # if linha[-4] in lpa:
                        #     if linha[-2] in empresasIBOV[i]:
                        #         continue
                        #     else:
                        #         empresasIBOV[i].append(linha[-2])
        

    # contador += 1







# for itemBD in empresasIBOV:
#     for itemAPI in range(0, len(ticker_api)):
#         if itemBD["Ticker"] == ticker_api[itemAPI]['id']:
#             itemBD["Pc_Atual"] = ticker_api[itemAPI]['price']
            

# for item in empresasIBOV:
#     if "Nm_Empresarial" not in item:
#         item["Nm_Empresarial"] = "None"
#     if "Pc_Atual" not in item:
#         item["Pc_Atual"] = 0.0
#     if "Cnpj" not in item:
#         item["Cnpj"] = "00.000.000/0000-00"
#     if "Hr_Atualizacao" not in item:
#         item["Hr_Atualizacao"] = hora


# for item in empresasIBOV:
#     valores = (
#         item.get('Ticker'), 
#         item.get('Cnpj'), 
#         item.get('Nm_Empresarial'), 
#         item.get('Pc_Atual'), 
#         item.get('Hr_Atualizacao')
#     )

#     try:
#         cursor.execute("""
#             INSERT OR IGNORE INTO Acoes (Ticker, Cnpj, Nm_Empresarial, Pc_Atual, Hr_Atual) 
#             VALUES (?, ?, ?, ?, ?)
#         """, valores)
        
#     except sqlite3.Error as e:
#         print(f"Erro no banco para {item.get('Ticker')}: {e}")
    
    

#     try:
#         cursor.execute(f"Update Acoes SET Cnpj = '{item['Cnpj']}' where ticker = '{item['Ticker']}'")
#     except:
#         pass

#     try:
#         cursor.execute(f"Update Acoes SET Nm_Empresarial = '{item['Nm_Empresarial']}' where ticker = '{item['Ticker']}'")
#     except:
#         pass
    
#     try:
#         cursor.execute(f"Update Acoes SET Pc_Atual = '{item['Pc_Atual']}' where ticker = '{item['Ticker']}'")
#     except:
#         pass
#     try:    
#         cursor.execute(f"Update Acoes SET Hr_Atual = '{item['Hr_Atualizacao']}' where ticker = '{item['Ticker']}'")
#     except:
#         pass


# conn.commit()


