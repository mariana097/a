class OrdemServicoController:
    def __init__(self, ordem_service):
        self.service = ordem_service

    def criar_ordem(self, **dados):
        return self.service.criar_ordem(**dados)

    def listar_ordens(self):
        return self.service.listar()
