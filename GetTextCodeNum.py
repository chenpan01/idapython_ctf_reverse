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
