from urllib.request import urlopen,urlretrieve,Request
import re
from time import sleep
import jieba
from random_number import random_num


#穿搭类别的预置标签
clothe_list = ["穿","搭","衣","服","衣服","穿搭","衣橱"]

#测试代码段
'''url = "https://m.ix5j.cn/article/show-3487008.html"
op = urlopen(url).read().decode()
list1 = re.findall(r'  (.*?)  </p>',op)
print(list1[0])'''


#该函数的作用是显示作者
def author(url):
	op = urlopen(url).read().decode()
	list1 = re.findall(r'  (.*?)  </p>',op)
	list1[0] = list1[0].strip()
	return list1[0]


#该函数的作用是数每篇文章对应的评论数
def count_comment(url):
	op = urlopen(url).read().decode()
	list1 = re.findall(r'   (.*?)</span>条评论',op)
	a = int(list1[0])
	return a



#该函数的作用是确定抓取文章的类别
def Determining_categories(url):
	op = urlopen(url).read().decode()
	list1 = re.findall(r'="font-weight:600">(.*?)</span>',op)
	dec_list = []
	for i in list1:
		seg_list = jieba.lcut(i,cut_all = False)
		for a in seg_list:
			dec_list.append(a)
	

	ret_list = [a for a in dec_list if a in clothe_list]

	if len(ret_list) != 0:
		print("该类别属于穿搭")
		return 1

	else:
		print("该类别不属于穿搭")
		return 0


#存储抓下来的数据的列表
content_list_clothes=[]
index = 0


#该函数的作用是抓取网页文章并对它进行处理
def save_content(number):
	url = "https://m.ix5j.cn/article/show-" + str(number) + ".html"

	#添加用户代理
	user_agent="User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
	head={"User-Agent":user_agent}
	resp=Request(url,headers=head)

	#打开代理以后的网页
	op = urlopen(resp).read().decode("utf-8")
	list1 = re.findall(r'"articleContent">(.*?)</div>',op)
	categorie = Determining_categories(url)
	sleep(0.3)
	print("现在是" + str(number) + "的页面")
	#该函数的作用是确定页面有无我们所需要的文章
	if (len(list1) == 0):
		print("该页面没有东西......" + str(number))
		
	else:	
		global index
		exa = 0
		#该段落的作用是去除HTML标签
		try:
			str_deal = list1[1]		
			str_dealfin = re.sub(r'<.*?>','',str_deal)		
			list1[1] = str_dealfin
		except:
			print("似乎清除标记的时候出现了一些错误")

		#判定有无重复的文章，有的话则不添加
		for num in content_list_clothes:
			try:
				if (num == list1[1]):
					exa = 1
					print("有重复的内容自动忽略...........\n")
			except:
				exa = 1
				print("似乎出现了一些错误")

	
		if(exa == 0):
			if(categorie == 1):
				try:
					num = count_comment(resp)
					author_str = author(resp)
					list1[1] = "**********作者：" + author_str + "*************    " + list1[1]
					list1[1] = list1[1] + "-----------------------热值数" + str(num)
					content_list_clothes.append(list1[1])
				except:
					print("好像抓不到热值数哦")
					content_list_clothes.append(list1[1])

				index = index + 1


'''save_content(3487002)
print(content_list_clothes)'''

'''for i in range(3487000,3487010):
	save_content(i)
	print("\n")'''
'''for i in range(6669000,6669100):
	save_content(i)
	print("\n")
for i in range(59781000,5978100):
	save_content(i)
	print("\n")
for i in range(60555000,60555100):  
	save_content(i)
	print("\n")'''


#生成随机的数
rand_num_list = random_num(5000,1000,9999)

for i in rand_num_list:
	save_content(i)
	print("\n")


with open("clothes.txt","a+",encoding = "utf-8") as u:
	for it in content_list_clothes:			
		u.write(it)
		u.write("\n\n\n\n\n\n\n")

	u.close()

