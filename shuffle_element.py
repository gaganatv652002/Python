import random
original_list=["Amit","Sumith","Neenu","Erick"]
shuffled_list=random.sample(original_list,len(original_list))
print("original list:",original_list)
print("shuffled list:",shuffled_list)

output:-
original list: ['Amit', 'Sumith', 'Neenu', 'Erick']
shuffled list: ['Neenu', 'Sumith', 'Erick', 'Amit']
