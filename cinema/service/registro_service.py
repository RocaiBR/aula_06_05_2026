from datetime import date

from cinema.model.models import RegistroPublico, RegistroPublicoDTO
from cinema.repository.repositories import (
    SessaoRepository,
    SalaRepository,
    RegistroPublicoRepository,
)


class RegistroPublicoService:
    def __init__(self):
        self._sessao_repo = SessaoRepository()
        self._sala_repo = SalaRepository()
        self._registro_repo = RegistroPublicoRepository()

    def validar_e_registrar(self, sessao_id: int, quantidade: int) -> RegistroPublicoDTO:
        # Busca sessão
        sessao = self._sessao_repo.find_by_id(sessao_id)
        if sessao is None:
            raise ValueError(f"Sessão {sessao_id} não encontrada.")

        if quantidade <= 0:
            raise ValueError("A quantidade de público deve ser maior que zero.")

        # Busca sala para validar capacidade
        sala = self._sala_repo.find_by_id(sessao.sala_id)
        total_atual = self._registro_repo.sum_by_sessao(sessao_id)
        novo_total = total_atual + quantidade

        if novo_total > sala.capacidade:
            raise ValueError(
                f"Capacidade excedida: sala comporta {sala.capacidade} pessoas, "
                f"já registradas {total_atual}, tentativa de adicionar {quantidade}."
            )

        # Grava o registro
        registro = RegistroPublico(
            id=None,
            sessao_id=sessao_id,
            data=date.today().isoformat(),
            quantidade=quantidade,
        )
        registro.id = self._registro_repo.save(registro)

        return RegistroPublicoDTO(
            registro=registro,
            total_acumulado=novo_total,
            capacidade_sala=sala.capacidade,
        )

    def consultar_total(self, sessao_id: int) -> dict:
        sessao = self._sessao_repo.find_by_id(sessao_id)
        if sessao is None:
            raise ValueError(f"Sessão {sessao_id} não encontrada.")
        sala = self._sala_repo.find_by_id(sessao.sala_id)
        total = self._registro_repo.sum_by_sessao(sessao_id)
        registros = self._registro_repo.list_by_sessao(sessao_id)
        return {
            "sessao_id": sessao_id,
            "data_hora": sessao.data_hora,
            "capacidade": sala.capacidade,
            "total_publico": total,
            "registros": registros,
        }
