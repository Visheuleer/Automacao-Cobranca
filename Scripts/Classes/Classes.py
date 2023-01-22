class Cobranca:
    def __init__(self, cpf_cnpj, valor_em_aberto, data_prevista_pagamento, status, email, nf):
        self.cpf_cnpj = cpf_cnpj
        self.valor_em_aberto = valor_em_aberto
        self.data_prevista_pagamento = data_prevista_pagamento
        self.status = status
        self.email = email
        self.nf = nf