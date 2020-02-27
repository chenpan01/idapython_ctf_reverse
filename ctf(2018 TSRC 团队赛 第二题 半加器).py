'''
求解该题，我一共使用了三步
'''
#1.找到使用'invalid argument'字符串的地方
#invalid argument的前12个字符序列
str1='69 6E 76 61 6C 69 64 20 61 72 67 75'
def GetStrPos(start,end):
	#查找str2字符串所在的位置
	BinaryAddr=FindBinary(start,SEARCH_DOWN,str1)
	#判断查找是否失败
	if hex(BinaryAddr)=='0xffffffffL':
		print 'not bin'
	else:
		print 'Binary ',hex(BinaryAddr)
		#跳转到字符串所在的位置
		Jump(BinaryAddr)
	#遍历调用该字符串的位置
	for refhs in XrefsTo(BinaryAddr, flags=0):
		print "x: %s x.frm 0x%x"%(refhs,refhs.frm)
		Jump(refhs.frm)
		#做注释
		MakeComm(refhs.frm,"使用了invalid argument字符串")
		#询问用户
		AskYN(1,'看完'+hex(refhs.frm)+'地址处的代码吗？')

for seg in Segments():  
	#如果为只读数据段，则调用GetStrPos
	if SegName(seg) == '.rdata':
		#print 'seg ',hex(seg)
		GetStrPos(seg,SegEnd(seg))

#2.找到使用操作指令的位置，分析找到起到关键作用的操作指令
import re
#算术逻辑操作码
CalOp=['mul','imul','or','not','div','xor']
def isCalOp(Op):
	for i in CalOp:
		if Op==i:
			return 1
	return 0
#清空字符串中的空格
def clearspace(str1):
	str2=''
	for i in str1:
		if i==' ':
			continue
		else:
			str2+=i
	return str2
#判断整个指令是否有注释
def isComment(str):
	for i in str:
		if i==';':
			return True
	return False
#判断算术逻辑指令有没有使用十六进制数进行计算
def isHex(str1):
	#使用正则表达式构造匹配十六进制数的字符串
	pattern= re.compile(r'[-]*[0-9a-fA-F]+')
	sNum=''
	try:
		if isComment(str1):
			xb=str1.rindex(';')
			sNum=str1[str1.rindex(',')+1:xb]
		else:
			sNum=str1[str1.rindex(',')+1:]
		#找到十六进制字符串，若没有找到，则抛出异常
		ans=pattern.match(sNum)
		#判断找到的十六进制数是否准确
		if ans.group(0)==sNum and sNum!='0':
			return 1
	except:
		return 0
	else:
		return 0
def GetOp(start,end):
	for addr in range(start,end):
		#获取操作指令
		Op=GetMnem(addr)
		#判断是否是操作指令
		if isCode(GetFlags(addr)):
			if isCalOp(Op)==1:
				#获取某地址处的字符串，包括指令和注释
				Comm=GetDisasm(addr)
				Comm=clearspace(Comm)
				if isHex(Comm)==1:
					#往ida中添加注释
					MakeComm(addr,"使用了操作码："+Op)
					print "Op_addr ",hex(addr)
for seg in Segments():  
	#是否为代码段
	if SegName(seg) == '.text':
		GetOp(seg,SegEnd(seg))

#3.分析关键的操作指令，得出如下求flag的算法
def GetAns():
	str="invalid argument"
	flag=""
	for i in range(0,len(str)):
		if i==7:
			flag+='A'
		else:
			flag+=chr(ord(str[i])^28^31)
	print flag

GetAns()
