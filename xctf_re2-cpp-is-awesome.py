# -*- coding:utf-8 -*-
'''
先用以下脚本，找到使用循环结构中的跳转指令，进而找到程序中的循环结构
'''
#把大写字母转换成小写
def SwapToXiao(c):
	t=32
	return chr(ord(c)+t)
def isJmp(addr):
	SzOp=['JO','JNO','JB','JNB','JE','JNE','JBE','JA','JS','JNS','JP','JNP','JL','JNL','JNG','JG','JCXZ','JECXZ','JMP','JMPE']
	llen=len(SzOp)
	for i in range(0,llen):
		SwapAns=''
		#把SzOp数组中所有字符串转换成小写字符串
		for c in SzOp[i]:
			SwapAns+=SwapToXiao(c)
		#加到SzOp数组中
		SzOp.append(SwapAns)
	#获取操作指令
	Op=GetMnem(addr)
	#判断是否是操作指令
	if isCode(GetFlags(addr)):
		#判断是否是跳转指令
		for Sin in SzOp:
			if Sin==Op:
				return 1
	return 0
def isCir(start,end):
	for ea in range(start,end):
		if isJmp(ea)==1:
			#获取跳转地址
			new_addr=GetDisasm(ea)[-6:]
			#判断是否为挑战地址
			if new_addr[-1:]<='9' and new_addr[-1:]>='0':
				if int(new_addr,16)<ea:
					#添加注释
					MakeComm(ea,"循环跳转指令")
# 遍历所有的段
for seg in Segments():  
	#如果为代码段，则调用GetStr
	if SegName(seg) == '.text':
		isCir(seg,SegEnd(seg))
'''
使用以下脚本求出程序的flag
'''

szint=[]
#该函数获取flag
def GetAns(start,end,tstr):
	flag=''
	for i in szint:
		flag+=tstr[i]
	print flag
#该函数获取str字符串
def GetStr():
	str_addr=0x400E58
	tstr=''
	while(1):
		#判断循环是否结束
		if hex(Byte(str_addr))=='0x0' and hex(Byte(str_addr+1))=='0x0':
			break
		#叠加字符串字符生成字符串
		tstr+=chr(Byte(str_addr))
		str_addr+=1
	return tstr
#获取整数数组
def getSzInt(start,end):
	for addr in range(start,end): #rax*4
		#判断是否是mov eax, IntSz[rax*4]指令语句，在该语句中可以获取整数数组的地址
		if 'rax*4' in GetOpnd(addr,1):
			#获取整数数组的地址
			address=hex(Dword(addr+3))[0:8]
			taddress=int(address,16)
			#获取整数数组
			while(1):
				if Dword(taddress)>0x7f:
					break
				szint.append(Dword(taddress))
				taddress+=4
			break
for seg in Segments():
	if SegName(seg) == '.text':
		getSzInt(seg,SegEnd(seg))
		str1=GetStr()
		GetAns(seg,SegEnd(seg),str1)
