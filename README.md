# Desafio Cobrança

  Esse projeto é um desafio proposto pela Hastag Treinamentos no vídeo: https://www.youtube.com/watch?v=dUxpMU9Bw3U&t=125s. O desafio é a criação de uma automação que Extraia dados de um excel e faça diversas verificações para o envio de email para clientes com contas que já passaram da data de pagamento limite. Por ser um desafio simples, decidi ir além e criei um Banco de Dados, onde o programa verificará quais contas não foram cadastradas na tabela e irá inseri-las. Além disso, criei as duas versões de extração desses dados: uma via planilha de excel e outra via consultas no banco de dados. 

## :pencil: Pré-requisitos
  ### Linguagem:
  - Python
  
  ### Bibliotecas:
  - Pandas
  - Openpyxl
  - Pyodbc
  - Redmail
  
  ### Banco de Dados:
  - Um Banco de dados chamado "Financeiro"
  - Uma tabela chamada Cobranca
  - A tabela deverá ser composta pelas seguintes colunas: "Cpf_Cnpj"(varchar), "Valor_Em_Aberto"(decimal), "Data_Prevista_Pagamento"(varchar), " Email"(varchar), "Nota_Fiscal"(varchar) e "Status"(varchar)
  
  ### Excel:
  - Planilha Excel que está em Dados/Contas a Receber.xlsx
  
  ### Credenciais de Email:
  - Ter um arquivo txt com email e senha separados por quebra de linha, e colar o caminho do mesmo no script "EnviaEmail", na função PegaCredenciais
  
 ## :wrench: Instalação
  Todas as bibliotecas e dependências do projeto estão presentes no documento "requirements.txt" no repositório e pode ser instalado com o seguinte passo a passo:
  - Abra o terminal onde o repositório está
  -  Digite o comando: `pip install -r Requirements/requirements.txt`
  
  ## :eyes: Observações
  
  - Para rodar via Banco de Dados comente a chamada da função "ConsultaAtrasosPagamentosExcel" no Script Main.py
  - Para rodar via Planilha Excel comente a chamada da função "ConsultaAtrasosBD" no Script Main.py
  - Caso não queira ou não saiba montar o Banco de Dados, comente as chamadas das funções "ConectaBD", "InsereDadosBD" e "DesconectaBD" no Script Main.py
  - O Projeto foi desenvolvido pensando em exercitar meus conhecimentos em Python, por isso fiz via Banco de dados e Excel, em um projeto real seria um ou outro
 
## ✒️ Autores
  - Jonas Euler (Desenvolvedor)
