'''
暴力破解010editor，我一共分为了三步
'''
1.找到使用了‘Invalid name or password. Please enter your name and password exa’字符串的地方
import time
#Invalid name or password的前12个字符序列
str1='49 6E 76 61 6C 69 64 20 6E 61 6D 65'
def GetStrPos(start,end):
	#查找str2字符串所在的位置
	BinaryAddr=FindBinary(start,SEARCH_DOWN,str1)
	#判断查找是否失败
	if hex(BinaryAddr)=='0xffffffffL':
		print 'not find'
	else:
		print 'BinaryAddr ',hex(BinaryAddr)
		#跳转到字符串所在的位置
		Jump(BinaryAddr)
	#遍历调用该字符串的位置
	for refhs in XrefsTo(BinaryAddr, flags=0):
		print "refhs: %s refhs.frm 0x%x"%(refhs,refhs.frm)
		#暂停2秒
		time.sleep(2)
		#跳转到引用该字符串的地方
		Jump(refhs.frm)
		#做注释
		MakeComm(refhs.frm,"使用了Invalid name or password. Please enter your name and password exa字符串")

for seg in Segments():  
	#如果为只读数据段，则调用GetStrPos
	if SegName(seg) == '.rdata':
		GetStrPos(seg,SegEnd(seg))

2.找到使用‘Invalid name or password. Please enter your name and password exa’字符串附近的跳转指令，分析找到关键跳
def isJmp(addr):
	SzOp=['jo', 'jno', 'jb', 'jnb', 'je', 'jne', 'jbe', 'ja', 'js', 'jns', 'jp', 'jnz', 'jl', 'jnl', 'jng', 'jg', 'jcxz', 'jecxz','jmpe']
	#获取操作指令
	Op=GetMnem(addr)
	#判断是否是操作指令
	if isCode(GetFlags(addr)):
		#判断是否是跳转指令
		for Sin in SzOp:
			if Sin==Op:
				return 1
	return 0
def isRightJmp(start,end):
	for ea in range(start,end):
		if isJmp(ea)==1:
			Disasm=GetDisasm(ea)
			#判断指令后面的操作数是否为地址
			if Disasm[-9:-4]=='14070':
				#获取跳转地址
				new_addr=Disasm[-9:]
				#输出出现在‘Invalid name or password. Please ’附近的跳转指令
				print 'new_addr',new_addr
				MakeComm(ea,"跳转指令")
for seg in Segments():  
	if SegName(seg) == '.text':
		isRightJmp(seg,SegEnd(seg))
3.Nop掉关键跳
PatchDword(0x140707B6B,0x00000000)
