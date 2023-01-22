import BancoDeDados.ConexaoBD as cb
from BancoDeDados.InsereDados import InsereDadosBD
from Excel.CarregaExcel import CarregaExcel

df = CarregaExcel()
conexao = cb.ConectaBD()
InsereDadosBD(conexao, df)
cb.DesconectaBD(conexao)
