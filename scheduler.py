# -*- coding: utf-8 -*-
import random

random.seed(1503)

fifo_1 = list()
fifo_2 = list()
scheduler_time = list()

fifo_1.append(random.randint(1, 10))
fifo_2.append(random.randint(1, 5))
scheduler_time.append(1)



count = 0
while True:
	print count, fifo_1, fifo_2
	if( len(fifo_1) > 0 ):
		if(fifo_1[0] == count ):
			fifo_1.append( count + random.randint(1,10))
			fifo_1.pop(0)
	if( len(fifo_2) > 0):
		if(fifo_2[0] == count ):
			fifo_2.append( count + random.randint(1,5) )
			fifo_2.pop(0)

	if count >= 50: break
	count += 1


# print fifo_1, fifo_2
# print fifo_1.pop(0)
# print fifo_1.pop(0)
# print len(fifo_1)
# print fifo_1.pop(0)
# print fifo_1