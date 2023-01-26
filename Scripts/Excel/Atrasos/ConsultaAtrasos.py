import datetime
import pandas as pd
import re
def ConsultaAtrasosPagamentosExcel(df):
    data_hoje = datetime.datetime.now()
    datas_vencidas = VerificaSeDataVencimentoJaPassou(data_hoje, df)
    df_contas_vencidas = MontaDfsContasVencidas(df, datas_vencidas)
    df_cobranca = PegaContasVencidasNaoPagas(df_contas_vencidas)
    print(df_cobranca)

def VerificaSeDataVencimentoJaPassou(data_atual, df):
    datas_vencidas = []
    for data_vencimento in df['Data Prevista para pagamento']:
        data_vencida = CalculaDiferencaDias(data_vencimento, data_atual)
        if data_vencida != '':
            datas_vencidas.append(data_vencida)
    return datas_vencidas


def CalculaDiferencaDias(data_vencimento, data_atual):
    calculo = (data_vencimento - data_atual).days
    data_vencida = ChecaDatasVencidas(calculo, data_vencimento)
    return data_vencida


def ChecaDatasVencidas(calculo, data_vencimento):
    if calculo < 0:
        return data_vencimento
    else:
        return ''

def MontaDfsContasVencidas(df, datas_vencidas):
    df_contas_vencidas = ConstrutorDf()
    for data_vencida in datas_vencidas:
        df_conta_vencida = df.loc[(df['Data Prevista para pagamento']) == data_vencida]
        df_contas_vencidas = df_contas_vencidas.merge(df_conta_vencida, how='outer')
    return df_contas_vencidas

def ConstrutorDf():
    COLUNAS = [
        'CPF',
        'Valor em aberto',
        'Data Prevista para pagamento',
        'Status',
        'E-mail',
        'NF'
    ]
    return pd.DataFrame(columns=COLUNAS)

def PegaContasVencidasNaoPagas(df_contas_vencidas):
    return df.loc[(df['Status'] == 'Em aberto')]

df =pd.read_excel(r'C:\Users\T-Gamer\Desktop\projetos\Automacao-Cobranca\Dados\Contas a Receber.xlsx')
ConsultaAtrasosPagamentosExcel(df)