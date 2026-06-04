# Diagrama de Classes

classDiagram

class Cliente {
    +id: int
    +nome: string
    +cpf: string
    +telefone: string
    +email: string
}

class Aparelho {
    +id: int
    +tipo: string
    +marca: string
    +modelo: string
    +numero_serie: string
    +observacoes: string
    +status: string
}

class Funcionario {
    +id: int
    +nome: string
    +cpf: string
    +salario: float
}

class Tecnico {
    +especialidade: string
}

class Administrador {
    +nivel_acesso: string
}

class OrdemServico {
    +id: int
    +data_abertura: date
    +data_encerramento: date
    +descricao_problema: string
    +status: string
    +valor_base: float
    +valor_total: float
    +calcularValor()
}

class VisitaTecnica {
    +id: int
    +data_agendamento: date
    +data_realizacao: date
    +resultado: string
    +status: string
}

class Equipamento {
    +id: int
    +nome: string
    +quantidade: int
    +valor_unitario: float
}

class Estoque {
    +id: int
    +quantidade_disponivel: int
    +quantidade_minima: int
    +atualizarEstoque()
}

class ContaReceber {
    +id: int
    +valor: float
    +vencimento: date
    +status: string
}

class Pagamento {
    +id: int
    +valor_pago: float
    +data_pagamento: date
    +forma_pagamento: string
}

%% Strategy

class EstrategiaCalculo {
    <<interface>>
    +calcular(valorBase)
}

class CalculoPadrao {
    +calcular(valorBase)
}

class CalculoUrgente {
    +calcular(valorBase)
}

class CalculoPorHora {
    +calcular(valorBase)
}

class CalculoDomiciliar {
    +calcular(valorBase)
}

%% Factory Method

class EstrategiaFactory {
    +criar(tipo)
}

%% Herança

Funcionario <|-- Tecnico
Funcionario <|-- Administrador

%% Relacionamentos

Cliente "1" --> "*" Aparelho : possui

Aparelho "1" --> "*" OrdemServico : gera

Tecnico "1" --> "*" OrdemServico : executa

OrdemServico "1" --> "*" VisitaTecnica : possui

OrdemServico "1" --> "1" ContaReceber : gera

ContaReceber "1" --> "0..1" Pagamento : recebe

Estoque "1" --> "*" Equipamento : controla

OrdemServico "*" --> "*" Equipamento : utiliza

%% Strategy

OrdemServico --> EstrategiaCalculo : utiliza

EstrategiaCalculo <|.. CalculoPadrao
EstrategiaCalculo <|.. CalculoUrgente
EstrategiaCalculo <|.. CalculoPorHora
EstrategiaCalculo <|.. CalculoDomiciliar

%% Factory

EstrategiaFactory --> EstrategiaCalculo : cria
```

