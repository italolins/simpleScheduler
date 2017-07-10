Implementação de um escalonador de tarefas.

Eventos Primarios ----	Eventos Secundarios

Chegada de fregues ---- *1 escalona proxima chegada (Randomico entre 1 e 10)
da classe 1	   ---- *2 Testa estado do servidor
				Livre: Mude estado para ocupado
					Escalona termino de serviço (Randomico entre 3 e 7)
				Ocupado: Escalona evento "colocar fregues na fila"


Chegada de fregues ---- *1 escalona proxima chegada (Randomico entre 1 e 5)
da classe 2	   ---- *2 Testa estado do servidor
				Livre: Mude estado para ocupado
					Escalona termino de serviço (Randomico entre 3 e 7)
				Ocupado: Escalona evento "colocar fregues na fila"


Termino de serviço ---- *1 Teste estado das filas de espera
			   Vazia: Mude estado servidor para "livre"
			   Não vazia
				Remove fregues da fila
				Escalona evento "Termino de serviço" (Randomico entre 3 e 7)

Como saída, a cada um dos eventos realizados deve ser apresentado o estado do sistema

seguindo o seguinte formato:

Tipo de evento: Chegada/Saída, Momento do evento: Z

Elementos na Fila 1: X

Elementos na Fila 2: Y

Elemento no serviço: A
