# -*- coding: utf-8 -*-
import random

random.seed(1503)



servidor_livre = True
termino_servico = 0

fifo_clientes1 = list()
fifo_clientes2 = list()
fifo_clientes1.append(1)
fifo_clientes2.append(2)
chegada_1 = random.randint(1, 10)
chegada_2 = random.randint(1, 5)


count = 0
while True:

        if(servidor_livre):
                if(len(fifo_clientes1) > 0):
                        fifo_clientes1.pop(0)
                        termino_servico = count + random.randint(3, 7)
                        servidor_livre = False
                elif(len(fifo_clientes2) > 0):
                        fifo_clientes2.pop(0)
                        termino_servico = count + random.randint(3, 7)
                        servidor_livre = False
                else: servidor_livre = True
        else:
                if( termino_servico == count):
                        if(len(fifo_clientes1) > 0):
                                fifo_clientes1.pop(0)
                                termino_servico = count + random.randint(3, 7)
                                servidor_livre = False
                        elif(len(fifo_clientes2) > 0):
                                fifo_clientes2.pop(0)
                                termino_servico = count + random.randint(3, 7)
                                servidor_livre = False
                        else: servidor_livre = True

        if(chegada_1 == count):
                fifo_clientes1.append(random.randint(1, 100))
                chegada_1 = count + random.randint(1, 10)
        if(chegada_2 == count):
                fifo_clientes2.append(random.randint(1, 100))
                chegada_2 = count + random.randint(1, 5)
        
        if count >= 10: break
        print 'TS',count
        print 'proxima chegada 1:',chegada_1
        print 'proxima chegada 2:',chegada_2
        print 'termino de servico:',termino_servico
        print 'fila 1:', fifo_clientes1
        print 'fila 2:', fifo_clientes2
        print 'servidor livre?',servidor_livre
        print '=============================='
        count += 1

        

	


# print fifo_1, fifo_2
# print fifo_1.pop(0)
# print fifo_1.pop(0)
# print len(fifo_1)
# print fifo_1.pop(0)
# print fifo_1
