#这个函数的作用其实就是把储存在name文件夹里的数据根据热数值从大到小排序,并且将杂乱数据保存在mix_data.txt文件里




#这个函数的功能是切分字符串
def deal_con(name):
	with open(name,"r",encoding = "utf-8") as u:
		content = u.read()
		content_list = content.split("\n\n")
		while '' in content_list:
			content_list.remove('')
		u.close()
	return content_list


none_num_list = []
list_1 = []


def sort_artical(name):
	sort = []
	deal_after_list = deal_con(name)
	for i in deal_after_list:
		 
		try:
			i.split("热值数",1)[1]
			temp = i.split("热值数",1)
			a = int(i.split("热值数",1)[-1])
			temp[-1] = a

			sort.append(tuple(temp))
		except:
			none_num_list.append(i)
			




	sort_list = sorted(sort,key = lambda s : s[-1],reverse=True )
	for i in sort_list:
		a = i[0] + "热值数" +str(i[1])
		list_1.append(a)




	
	with open("sort_clothes.txt","w",encoding = "utf-8") as f:
		for i in list_1:
			f.write(i)
			f.write("\n\n\n")

		f.close()

	with open("mix_data.txt","a+",encoding = "utf-8") as f:
		for i in none_num_list:
			f.write(i)
			f.write("\n\n\n")

		f.close()




sort_artical("clothes.txt")