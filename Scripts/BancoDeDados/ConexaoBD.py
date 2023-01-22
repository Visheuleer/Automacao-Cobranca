import pyodbc
import sys

def ConectaBD():
    dados = (
        "Driver={SQL Server};"
        "Server=DESKTOP-F9GHF2T\SQLEXPRESS;"
        "Database=Financeiro;"
    )
    try:
        conexao = pyodbc.connect(dados)
        return conexao
    except(Exception) as err:
        print(f"Não foi possível conectar com o banco de dados! {type(err)}, {err}")
        sys.exit()

def DesconectaBD(conexao):
    conexao.close()

