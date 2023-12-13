method1:-

import random
random_float_0_to_1=random.random()
print("Random float between 0 and 1:",random_float_0_to_1)
start_range,end_range=5.0,10.0
random_float_in_range=random.uniform(start_range,end_range)
print("Random float betwen",start_range,"and",end_range,":",random_float_in_range)

output:-
Random float between 0 and 1: 0.03411430220436906
Random float betwen 5.0 and 10.0 : 7.446530436597096

method2:-
import random
a=random.uniform(0,1)
b=random.uniform(10,20)
print(a)
print(b)

output:-
0.3025872380048934
10.234889305975752
