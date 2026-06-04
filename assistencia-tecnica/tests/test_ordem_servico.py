from app.models.ordem_servico import OrdemServico
from app.factories.estrategia_factory import EstrategiaFactory


def test_ordem_servico_calcula_valor_total_com_estrategia_urgente():
    ordem = OrdemServico(cliente_id=1, aparelho_id=1, valor_base=100)
    estrategia = EstrategiaFactory.criar("urgente")

    total = ordem.calcular_valor_total(estrategia)

    assert total == 150
    assert ordem.valor_total == 150
