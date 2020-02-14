# -*- coding:utf-8 -*-
def mul():
    return 1

def imul():
    return 1

def opand():
    return 1


def opor():
    return 1


def opnot():
    return 1


def div():
    return 1


def xor():
    return 1


def default():
    return 0

switch = {    'mul': mul,
			  'imul': imul,
			  'and': opand,
			  'or': opor,
			  'not': opnot,
			  'div': div,
			  'xor': xor,
                         }
FunAddress = []
OpAndTypeNum=dict()
FindFunc = dict()
def GetKeyFunc(Start, End):
	#把代码段中的所有函数存放在列表FunAddress中
	for function_ea in Functions(Start, End):
		FunAddress.append(function_ea)
	FunAddress.append(End)
	#遍历所有的函数
	for i in range(0, len(FunAddress)):
		#获取函数名
		FunctionName = GetFunctionName(FunAddress[i])
		#判断是否为用户函数
		if i + 1 != len(FunAddress) and FunctionName[0]=='s' and FunctionName[1]=='u' and FunctionName[2]=='b':
			OpNum=0
			#清空字典
			OpAndTypeNum.clear()
			#遍历所有函数中的指令
			for singfuc_ea in range(FunAddress[i], FunAddress[i + 1]):
				flag = GetFlags(singfuc_ea)
				#判断是否为操作码
				if isCode(flag):
					#获取汇编指令
					op = GetMnem(singfuc_ea)
					#使用switch判断是否为算术或逻辑指令
					OpAndTypeNum[op] = OpAndTypeNum.get(op,0)+switch.get(op, default)()
			#统计算术或逻辑指令的个数
			for OP,value in OpAndTypeNum.items():
				if value>0:
					OpNum+=1
					
			#如果算术或逻辑指令的个数大于1，则可以初步判断该函数为用户写的算法函数(有误差)
			if OpNum>2:
				FindFunc[FunctionName]=FunAddress[i]
				#print "i:",FunAddress[i],"i+1:",FunAddress[i+1]
				
	for Name, ea in FindFunc.items():
		print Name, ":", ea
for seg in Segments():  # 遍历所有的段
    if SegName(seg) == '.text':
        GetKeyFunc(seg, SegEnd(seg))
