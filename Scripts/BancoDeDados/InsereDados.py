from Scripts.Classes.Classes import Cobranca
import re
def InsereDadosBD(conexao, df):
    cursor = conexao.cursor()
    dados_cobranca = CriaInstanciaCobranca(df)
    Consulta_Cobrancas_Nao_Cadastradas(cursor, dados_cobranca)

def CriaInstanciaCobranca(df):
    data_prevista_pagamento = TrataDatas(list(df['Data Prevista para pagamento']))
    return Cobranca(
        list(df['CPF']),
        list(df['Valor em aberto']),
        data_prevista_pagamento,
        list(df['Status']),
        list(df['E-mail']),
        list(df['NF'])
    )

def TrataDatas(datas):
    datas_sem_hora = [re.sub(r'..:..:..', '', str(data_sem_hora)) for data_sem_hora in datas]
    return [re.sub('-', '/', data) for data in datas_sem_hora]

def Consulta_Cobrancas_Nao_Cadastradas(cursor, dados):
    for i in range(len(dados.cpf_cnpj)):
        comando = f"""
            SELECT * FROM Cobranca WHERE Cpf_Cnpj = '{dados.cpf_cnpj[i]}' AND 
            Valor_Em_Aberto = {dados.valor_em_aberto[i]} AND
            Data_Prevista_Pagamento = '{dados.data_prevista_pagamento[i]}' AND
            Email = '{dados.email[i]}' AND
            Nota_Fiscal = '{dados.nf[i]}' AND
            Status = '{dados.status[i]}'
        """
        retorno = cursor.execute(comando)
        resultado = retorno.fetchone()
        if resultado == None:
            dados_nao_cadastrados = Cobranca(dados.cpf_cnpj[i], dados.valor_em_aberto[i], dados.data_prevista_pagamento[i],dados.status[i], dados.email[i],dados.nf[i])
            ExecutaComandoInsert(dados_nao_cadastrados,cursor)


def ExecutaComandoInsert(dados, cursor):
    comando = f"""
        INSERT INTO Cobranca
        VALUES('{dados.cpf_cnpj}', {dados.valor_em_aberto}, '{dados.data_prevista_pagamento}', '{dados.email}', '{dados.nf}', '{dados.status}')
        """
    cursor.execute(comando)
    cursor.commit()










