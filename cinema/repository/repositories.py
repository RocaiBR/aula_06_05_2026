from cinema.database import get_connection
from cinema.model.models import Sessao, RegistroPublico, Sala


class SessaoRepository:
    def find_by_id(self, sessao_id: int) -> Sessao | None:
        conn = get_connection()
        row = conn.execute("SELECT * FROM sessao WHERE id = ?", (sessao_id,)).fetchone()
        conn.close()
        if row is None:
            return None
        return Sessao(
            id=row["id"],
            data_hora=row["data_hora"],
            sala_id=row["sala_id"],
            filme_id=row["filme_id"],
            valor_ingresso=row["valor_ingresso"],
        )

    def list_all(self) -> list[Sessao]:
        conn = get_connection()
        rows = conn.execute("""
            SELECT s.id, s.data_hora, s.sala_id, s.filme_id, s.valor_ingresso,
                   f.titulo, sl.numero, c.nome AS cinema_nome
            FROM sessao s
            JOIN filme f ON f.id = s.filme_id
            JOIN sala sl ON sl.id = s.sala_id
            JOIN cinema c ON c.id = sl.cinema_id
        """).fetchall()
        conn.close()
        return rows


class SalaRepository:
    def find_by_id(self, sala_id: int) -> Sala | None:
        conn = get_connection()
        row = conn.execute("SELECT * FROM sala WHERE id = ?", (sala_id,)).fetchone()
        conn.close()
        if row is None:
            return None
        return Sala(
            id=row["id"],
            numero=row["numero"],
            capacidade=row["capacidade"],
            cinema_id=row["cinema_id"],
        )


class RegistroPublicoRepository:
    def save(self, registro: RegistroPublico) -> int:
        conn = get_connection()
        cursor = conn.execute(
            "INSERT INTO registro_publico (sessao_id, data, quantidade) VALUES (?, ?, ?)",
            (registro.sessao_id, registro.data, registro.quantidade),
        )
        registro_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return registro_id

    def sum_by_sessao(self, sessao_id: int) -> int:
        conn = get_connection()
        row = conn.execute(
            "SELECT COALESCE(SUM(quantidade), 0) AS total FROM registro_publico WHERE sessao_id = ?",
            (sessao_id,),
        ).fetchone()
        conn.close()
        return row["total"]

    def list_by_sessao(self, sessao_id: int) -> list[RegistroPublico]:
        conn = get_connection()
        rows = conn.execute(
            "SELECT * FROM registro_publico WHERE sessao_id = ? ORDER BY data",
            (sessao_id,),
        ).fetchall()
        conn.close()
        return [
            RegistroPublico(
                id=r["id"],
                sessao_id=r["sessao_id"],
                data=r["data"],
                quantidade=r["quantidade"],
            )
            for r in rows
        ]
