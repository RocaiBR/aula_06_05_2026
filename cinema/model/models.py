from dataclasses import dataclass
from typing import Optional


@dataclass
class Cinema:
    id: Optional[int]
    nome: str
    cidade: str
    estado: str


@dataclass
class Sala:
    id: Optional[int]
    numero: int
    capacidade: int
    cinema_id: int


@dataclass
class Filme:
    id: Optional[int]
    titulo: str
    duracao_min: int
    classificacao: str
    ativo: bool


@dataclass
class Sessao:
    id: Optional[int]
    data_hora: str
    sala_id: int
    filme_id: int
    valor_ingresso: float


@dataclass
class RegistroPublico:
    id: Optional[int]
    sessao_id: int
    data: str
    quantidade: int


@dataclass
class RegistroPublicoDTO:
    registro: RegistroPublico
    total_acumulado: int
    capacidade_sala: int
