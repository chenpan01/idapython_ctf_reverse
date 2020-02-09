#-*- coding:utf-8 -*-
#第一种方法：
FunAndNum=dict() #保存函数名和函数数量
def GetFuncAndNum(Start,End):
	for function_ea in Functions(Start, End):
		FunctionName=GetFunctionName(function_ea)#获取函数名
		FunAndNum[FunctionName]=FunAndNum.get(FunctionName,0)+1 #函数数量加一
	for Name,Num in FunAndNum.items():
		print "Name:",Name," Num ",Num
for seg in Segments(): #遍历所有的段
	if SegName(seg)=='.text': 
		GetFuncAndNum(seg,SegEnd(seg))
		
#第二种方法：
num=[]
Func=[]
def GetFuncAndNum(Start,End):
	for function_ea in Functions(Start, End):
		FunctionName=GetFunctionName(function_ea)
		try:
			xb=Func.index(FunctionName)	#判断有无该函数							
		except:
			Func.append(FunctionName)
			num.append(0)
			num[len(num)-1]=1
		else:
			num[Func.index(FunctionName)]=num[Func.index(FunctionName)]+1 #统计指令个数
		
	Min=min(num) #列表最小值
	Max=max(num) #列表最大值
	
	#按函数个数大小有序输出函数名
	for i in range(Min,Max+1):
		for j in range(0,len(num)):
			if num[j]==i:
				print Func[j],":",num[j]

for seg in Segments(): #遍历所有的段
    if SegName(seg)=='.text': 
		GetFuncAndNum(seg,SegEnd(seg))
#第三种方法：

