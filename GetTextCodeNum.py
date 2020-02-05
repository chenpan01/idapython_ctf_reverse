第一种方法：
num=[]
Mnem=[]
def GetMnemNum(Start,End):
	for head in Heads(Start,End):#遍历所有指令，head为地址
		if isCode(GetFlags(head)):#判断是否为指令
			flag=GetMnem(head)#获取汇编指令
			try:
				xb=Mnem.index(flag)	#判断有无该指令							
			except:
				Mnem.append(flag)
				num.append(0)
				num[len(num)-1]=1
			else:
				num[Mnem.index(flag)]=num[Mnem.index(flag)]+1 #统计指令个数
				
	for i in range(0,len(num)):
		print Mnem[i],':',num[i]

for seg in Segments(): #遍历所有的段
    GetMnemNum(seg,SegEnd(seg)) 

第二种方法：
Mnem=[]
single=[]
Num=[]
def GetMnemNum(Start,End):
	for head in Heads(Start,End):#遍历所有指令，head为地址
		if isCode(GetFlags(head)):#判断是否为指令
			flag=GetMnem(head)#获取汇编指令
			Mnem.append(flag)
	Mnem.sort(reverse=True)#排序
	single.append(Mnem[0])
	for i in range(1,len(Mnem)):
		if Mnem[i]==Mnem[i-1]:
			continue
		else:#元素不同，则加入，统计不同元素
			single.append(Mnem[i])
	for i in range(0,len(single)):
		print single[i],':',Mnem.count(single[i])
for seg in Segments(): #遍历所有的段
    GetMnemNum(seg,SegEnd(seg))

第三种方法：
CodeAndNum=dict()
def GetMnemNum(Start,End):
	for head in Heads(Start,End):#遍历所有指令，head为地址
		if isCode(GetFlags(head)):#判断是否为指令
			flag=GetMnem(head)#获取汇编指令
			CodeAndNum[flag]=CodeAndNum.get(flag,0)+1
	items=CodeAndNum.items()
	NewItems=[[v[1],v[0]] for v in items]
	NewItems.sort()
	#print NewItems
	for i in range(0,len(NewItems)):
		t=NewItems[i]
		print t[1],t[0]
for seg in Segments(): #遍历所有的段
    GetMnemNum(seg,SegEnd(seg))
