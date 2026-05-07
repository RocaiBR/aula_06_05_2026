from cinema.controller.registro_controller import RegistroPublicoController
from cinema.repository.repositories import SessaoRepository


class RegistroPublicoView:
    def __init__(self):
        self._controller = RegistroPublicoController()
        self._sessao_repo = SessaoRepository()

    def _listar_sessoes(self):
        sessoes = self._sessao_repo.list_all()
        if not sessoes:
            print("  Nenhuma sessão cadastrada.")
            return
        print(f"\n  {'ID':<4} {'Filme':<30} {'Sala':<6} {'Cinema':<20} {'Data/Hora'}")
        print("  " + "-" * 74)
        for s in sessoes:
            print(f"  {s['id']:<4} {s['titulo']:<30} {s['numero']:<6} {s['cinema_nome']:<20} {s['data_hora']}")

    def exibir_menu(self):
        while True:
            print("\n" + "=" * 50)
            print("  SISTEMA DE REDE DE CINEMAS")
            print("=" * 50)
            print("  1. Registrar público em sessão")
            print("  2. Consultar totais de uma sessão")
            print("  3. Sair")
            print("-" * 50)

            opcao = input("  Escolha: ").strip()

            if opcao == "1":
                self._tela_registrar()
            elif opcao == "2":
                self._tela_consultar()
            elif opcao == "3":
                print("\n  Saindo. Até logo!\n")
                break
            else:
                print("  Opção inválida.")

    def _tela_registrar(self):
        print("\n--- Registrar Público ---")
        self._listar_sessoes()
        try:
            sessao_id = int(input("\n  ID da sessão: "))
            quantidade = int(input("  Quantidade de público: "))
        except ValueError:
            print("  Entrada inválida.")
            return

        resultado = self._controller.registrar_publico(sessao_id, quantidade)
        print()
        if resultado["sucesso"]:
            print(f"  ✓ {resultado['mensagem']}")
        else:
            print(f"  ✗ Erro: {resultado['mensagem']}")

    def _tela_consultar(self):
        print("\n--- Consultar Totais de Sessão ---")
        self._listar_sessoes()
        try:
            sessao_id = int(input("\n  ID da sessão: "))
        except ValueError:
            print("  Entrada inválida.")
            return

        resultado = self._controller.consultar_totais(sessao_id)
        if not resultado["sucesso"]:
            print(f"  ✗ Erro: {resultado['mensagem']}")
            return

        print(f"\n  Sessão #{resultado['sessao_id']} – {resultado['data_hora']}")
        print(f"  Capacidade da sala : {resultado['capacidade']}")
        print(f"  Total de público   : {resultado['total_publico']}")
        print(f"  Ocupação           : {resultado['total_publico'] / resultado['capacidade'] * 100:.1f}%")
        print()
        if resultado["registros"]:
            print(f"  {'Data':<14} {'Quantidade'}")
            print("  " + "-" * 28)
            for r in resultado["registros"]:
                print(f"  {r.data:<14} {r.quantidade}")
