from redmail import outlook
def PreparaDfEmail(df):
    for email in df['E-mail']:
        df_cobranca = df.loc[(df['E-mail'] == email)]
        df_cobranca = ExcluiColunaEmail(df_cobranca)
        df_cobranca = TrocaNomeColuna(df_cobranca, 'Valor em aberto', 'Valor')
        df_cobranca = TrocaNomeColuna(df_cobranca, 'Data Prevista para pagamento', 'Data Vencimento')
        df_cobranca = TrocaNomeColuna(df_cobranca, 'CPF', 'CpfCnpj')
        df_cobranca = EstilizaDf(df_cobranca)
        EnviaEmail(df_cobranca, email)


def ExcluiColunaEmail(df):
    return df.drop(columns=['E-mail'])

def TrocaNomeColuna(df, nome_atual, nome_desejado):
    return df.rename(columns={nome_atual: nome_desejado})

def EstilizaDf(df_cobranca):
    df_cobranca = df_cobranca.style.format({'Valor': 'R${:,.0f}'})
    df_cobranca = df_cobranca.hide_index()
    return df_cobranca


def EnviaEmail(df, email_cobranca):
    email, senha = PegaCredenciais()
    outlook.username = email
    outlook.password = senha
    outlook.send(
            receivers=[email_cobranca],
            subject="Contas Vencidas",
            html=f"""
                <body lang=PT-BR link="#0563C1" vlink="#954F72" style='tab-size:35.4pt'>
                    <div class=WordSection1>
                    <p class=MsoNormal style='background:#F4F4F4'><span style='font-family:"Microsoft Sans Serif",sans-serif'><img id="_x0000_i1025" src="https://1001freedownloads.s3.amazonaws.com/vector/thumb/111085/logo_generic.png" width="200" height="50"></span><span style='font-family:""Microsoft Sans Serif"",sans-serif;mso-fareast-language:PT-BR'><o:p></o:p></span></p>
                    <p style='text-align:justify'><span style='font-size:10.0pt;font-family:"Microsoft Sans Serif",sans-serif'>
                    </span>
                    </p>
                    </div>
                        Prezado(a) Cliente, <br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Não identificamos o pagamento dos seguintes valores: <br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{df.to_html()}<br>
                        <o:p></o:p></span></p>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Como não recebemos nenhuma comunicação sobre os motivos do atraso, solicitamos que entre em contato o quanto antes para regularização desta pendência.<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Caso o pagamento já tenha sido efetuado, por favor desconsidere este aviso.<br>
                        <p style='text-align:justify'><span style='font-size:10.0pt;font-family:""Microsoft Sans Serif"",sans-serif'>Atenciosamente,<o:p></o:p></span></p>
                        <p style='text-align:justify'><span style='font-size:10.0pt;font-family:""Microsoft Sans Serif"",sans-serif'>Empresa S/A.<o:p></o:p></span></p>
                        <p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;text-align:center;background:#DDDDDD'><b><span style='font-size:11.5pt;font-family:"Microsoft Sans Serif",sans-serif;color:#444444'>TI Sistemas - Cobrança </span>
                        <span style='font-family:"Microsoft Sans Serif",sans-serif;color:#444444'><br></span>
                        <span class=SpellE><b><u><span style='font-family:"Microsoft Sans Serif",sans-serif;color:#006A41'>Endereco</span></u></b><b><u><span style='font-family:"Microsoft Sans Serif",sans-serif;color:#006A41'>: Rua, 2 - Bairro, Estado - Cidade, CEP</span></u></b>
                    </body>
            """
        )
def PegaCredenciais():
    with open(r"C:\Users\T-Gamer\Desktop\projetos\Automacao-Cobranca\Scripts\Email\credenciais.txt", 'r') as arq:
        texto = arq.readlines()
        for i in range(len(texto)):
            if i == 0:
                email = TrataStringCredencial(texto[i])
            else:
                senha = TrataStringCredencial(texto[i])
    return email, senha

def TrataStringCredencial(credencial):
    return credencial.replace('\n', '')



