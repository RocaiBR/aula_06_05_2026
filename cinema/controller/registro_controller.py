from cinema.service.registro_service import RegistroPublicoService


class RegistroPublicoController:
    def __init__(self):
        self._service = RegistroPublicoService()

    def registrar_publico(self, sessao_id: int, quantidade: int) -> dict:
        try:
            dto = self._service.validar_e_registrar(sessao_id, quantidade)
            return {
                "sucesso": True,
                "registro_id": dto.registro.id,
                "total_acumulado": dto.total_acumulado,
                "capacidade_sala": dto.capacidade_sala,
                "mensagem": (
                    f"Público registrado com sucesso. "
                    f"Total acumulado: {dto.total_acumulado}/{dto.capacidade_sala}"
                ),
            }
        except ValueError as e:
            return {"sucesso": False, "mensagem": str(e)}

    def consultar_totais(self, sessao_id: int) -> dict:
        try:
            dados = self._service.consultar_total(sessao_id)
            return {"sucesso": True, **dados}
        except ValueError as e:
            return {"sucesso": False, "mensagem": str(e)}
