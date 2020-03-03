# -*- coding:utf-8 -*-
import base64
import string
def GetAns(base64_flag):
	a = ['i', '5', 'j', 'L', 'W', '7', 'S', '0', 'G', 'X', '6', 'u', 'f', '1', 'c', 'v', '3', 'n', 'y', '4', 'q', '8', 'e', 's', '2', 'Q', '+', 'b', 'd', 'k', 'Y', 'g', 'K', 'O', 'I', 'T', '/', 't', 'A', 'x', 'U', 'r', 'F', 'l', 'V', 'P', 'z', 'h', 'm', 'o', 'w', '9', 'B', 'H', 'C', 'M', 'D', 'p', 'E', 'a', 'J', 'R', 'Z', 'N']
	#把a生成字符串
	Tbase64= ''.join(a)
	#默认的编码
	base64_rel="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	#把默认的编码表变成程序自定义的编码表
	string_rel = string.maketrans(Tbase64,base64_rel)
	#把上述代码输出的base64_flag转换成上述编码表对应的字符串
	Encode_flag = base64_flag.translate(string_rel)
	#解码
	flag = base64.b64decode(Encode_flag)
	print 'flag ',flag
#找到关键字符串在ida中的位置
def findstr(s):
	findstr='4D 62 54 33'
	#查找输入字符串所在的位置
	BinaryAddr=FindBinary(s,SEARCH_DOWN,findstr)
	#判断查找是否失败
	if hex(BinaryAddr)=='0xffffffffL':
		print 'not found'
	else:
		print 'BinaryAddr ',hex(BinaryAddr)
	#返回地址
	return BinaryAddr
def GetStr(s):
	str_addr=findstr(s)
	tstr=''
	while(1):
		#判断循环是否结束
		if hex(Byte(str_addr))=='0x0' and hex(Byte(str_addr+1))=='0x0':
			break
		#叠加字符串字符生成字符串
		tstr+=chr(Byte(str_addr))
		str_addr+=1
	return tstr
def Getbase64(s):
	str=GetStr(s)
	#调换前后一半字符串的位置
	str1=str[16:]+str[0:16]
	i=0
	t=''
	while i<len(str1):
		#调换前后字符的位置
		t+=str1[i+1]+str1[i]
		i+=2
	GetAns(t)
for seg in Segments():  
	#如果为代码段，则调用Getbase64
	if SegName(seg) == '.text':
		Getbase64(seg)
