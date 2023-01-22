from Scripts.Classes.Classes import Cobranca

def Valida_Valores_Ja_Inseridos(cursor, comando):
    resp = cursor.execute(comando)
    row = resp.fetchone()
    if row != None:
        print(row)
        return ''
    else:
        row

def Gera_Comandos_Para_Validar(cursor, dados):
    for i in range(len(dados.cpf_cnpj)):
        comando = f"""
            SELECT * FROM Cobranca WHERE Cpf_Cnpj = '{dados.cpf_cnpj[i]}' AND 
            Valor_Em_Aberto = {dados.valor_em_aberto[i]} AND
            Data_Prevista_Pagamento = '{dados.data_prevista_pagamento[i]}' AND
            Email = '{dados.email[i]}' AND
            Nota_Fiscal = '{dados.nf[i]}' AND
            Status = '{dados.status[i]}'
        """
        Valida_Valores_Ja_Inseridos(comando)

def CriaInstanciaCobranca(df):
    return Cobranca(
        list(df['CPF']),
        list(df['Valor em aberto']),
        list(df['Data Prevista para pagamento']),
        list(df['Status']),
        list(df['E-mail']),
        list(df['NF'])
    )

def ExecutaComandoInsert(dados, cursor):
    for i in range(len(dados.cpf_cnpj)):
        comando = f"""
            INSERT INTO Cobranca
            VALUES({dados.cpf_cnpj[i]}, {dados.valor_em_aberto[i]}, {dados.data_prevista_pagamento[i]}, {dados.email[i]}, {dados.nf[i]}, {dados.status[i]})
        """
        cursor.execute(comando)

def InsereDadosBD(conexao, df):
    cursor = conexao.cursor()
    dados_cobranca = CriaInstanciaCobranca(df)
    Verifica_Se_Valores_Ja_Foram_Inseridos(conexao, cursor, dados_cobranca)
    ExecutaComandoInsert(dados_cobranca, cursor)

