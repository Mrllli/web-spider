import random

#这个函数的作用是生成随机的数
def random_num(number,number1,number2):
	rand_num_list=[]
	st = 0
	while(st < number):
		ran_num = random.randint(number1,number2)
		
		for i in range(1,10):
			ran_num_aft = str(ran_num) + "00"+str(i)
			ran_num_aft = int(ran_num_aft)
			rand_num_list.append(ran_num_aft)
			st =st + 1
	
	return rand_num_list



