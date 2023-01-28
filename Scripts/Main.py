import BancoDeDados.ConexaoBD as cb
from BancoDeDados.InsereDados import InsereDadosBD
from Excel.CarregaExcel import CarregaExcel
from BancoDeDados.Atrasos.ConsultaAtrasosBD import ConsultaAtrasosBD

try:
    df = CarregaExcel()
    conexao = cb.ConectaBD()
    cursor = InsereDadosBD(conexao, df)
    #df_cobranca = ConsultaAtrasosPagamentosExcel(df)
    df_cobranca = ConsultaAtrasosBD(cursor)
    cb.DesconectaBD(conexao)
except(Exception) as err:
    print(f'{type(err)}, {err}')
