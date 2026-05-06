# Regras de Negócio (RN)

- RN01: O número de espectadores registrados em uma sessão
não pode ultrapassar a capacidade máxima do cinema onde a sessão ocorre.

- RN02: Deve haver um intervalo de tempo mínimo (ex: 30 minutos)
entre sessões no mesmo cinema para limpeza e organização (considerado na lógica de agendamento).

- RN03: As sessões só podem ocorrer dentro do horário de funcionamento da unidade. 
O horário previsto para o término do filme não pode ultrapassar o horário de fechamento do cinema.

- RN04: Uma sessão não pode ser cancelada, 
modificada ou excluída caso já possua público registrado (espectadores > 0).

- RN05: O sistema deve impedir a sobreposição de sessões no mesmo cinema,
bloqueando agendamentos que entrem em conflito com o período de uma sessão já existente (horário de início + duração + intervalo).
