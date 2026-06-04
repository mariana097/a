from app.models.cliente import Cliente
from app.models.aparelho import Aparelho


def test_cliente_e_aparelho_persistem_relacionamento(session):
    cliente = Cliente(nome="Maria Silva", cpf="12345678900", telefone="11999999999", email="maria@example.com")
    session.add(cliente)
    session.commit()

    aparelho = Aparelho(tipo="Notebook", marca="Dell", modelo="Inspiron", numero_serie="ABC123", observacoes="Tela trincada", cliente_id=cliente.id)
    session.add(aparelho)
    session.commit()

    session.refresh(cliente)
    assert cliente.aparelhos
    assert cliente.aparelhos[0].marca == "Dell"
