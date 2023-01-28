from Scripts.Classes.Classes import Cobranca
import datetime
from Scripts.Excel.Atrasos.ConsultaAtrasos import ConstrutorDf, CalculaDiferencaDias,MontaDfsContasVencidas
import pandas as pd
import re

def ConsultaAtrasosBD(cursor):
    retorno = ExecutaConsulta(cursor)
    df = MontaDfCobranca(retorno)
    data_hoje = datetime.datetime.now()
    data_hoje = ConverteDateEmStr(data_hoje)
    datas_vencidas = VerificaSeDataVencimentoJaPassou(df, data_hoje)
    df_contas_vencidas = MontaDfsContasVencidas(df, datas_vencidas)
    return df_contas_vencidas

def ExecutaConsulta(cursor):
    return cursor.execute("SELECT * FROM Cobranca WHERE Status != 'Pago'")

def MontaDfCobranca(retorno):
    df = ConstrutorDf()
    for ret in retorno:
        (cpf_cnpj, valor_em_aberto, data_prevista_pagamento, email, nf, status) = ret
        cobranca = Cobranca(cpf_cnpj, valor_em_aberto, data_prevista_pagamento, status, email, nf)
        df = AtualizaDf(cobranca, df)
    return df

def ConverteDateEmStr(data):
    if type(data) is datetime.datetime:
        return datetime.datetime.strftime(data, '%Y-%m-%d')
    elif type(data) is list:
        return [datetime.datetime.strftime(date, '%Y-%m-%d') for date in data]
    else:
        return ''

def AtualizaDf(cobranca, df):
    return MesclaDfs(df, cobranca)

def ConstrutorDfComDados(cobranca):
    df = [[cobranca.cpf_cnpj, cobranca.valor_em_aberto, cobranca.data_prevista_pagamento,
                 cobranca.status, cobranca.email, cobranca.nf]]

    return pd.DataFrame(df, columns=['CPF',
                                    'Valor em aberto',
                                    'Data Prevista para pagamento',
                                    'Status',
                                    'E-mail',
                                    'NF'])
def MesclaDfs(df, cobranca):
    return df.merge(ConstrutorDfComDados(cobranca), how='outer')


def VerificaSeDataVencimentoJaPassou(df, data_atual):
    datas_vencidas = []
    for data_vencimento in df['Data Prevista para pagamento']:
        data_vencimento, data_atual = ConverteStrEmDate(data_vencimento, data_atual)
        data_vencida = CalculaDiferencaDias(data_vencimento, data_atual)
        if data_vencida != '':
            data_vencida = ConverteDateEmStr(data_vencida)
            datas_vencidas.append(data_vencida)
    return datas_vencidas

def ConverteStrEmDate(data, data2):
    if type(data) is str:
        data = datetime.datetime.strptime(data, '%Y-%m-%d')
    if type(data2) is str:
        data2 = datetime.datetime.strptime(data2, '%Y-%m-%d')
    return data, data2





