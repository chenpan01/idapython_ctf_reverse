# -*- coding:utf-8 -*-
from random import choice
pre6='pctfef'
hehe3_8="Pctf2016"
hehe3_8_o=[]
javastr='170501'
base='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-+'
#把hehe3_8中的字符转换成十进制数
def Hehe3_8ToOrd():
	for i in hehe3_8:
		hehe3_8_o.append(ord(i))

def GetBase(str_addr):
	base=''
	while(1):
		#判断循环是否结束
		if hex(Byte(str_addr))=='0x0':
			break
		#叠加字符串字符生成字符串
		base+=chr(Byte(str_addr))
		str_addr+=1
	return base
def Getpadding(str_addr):
	tpadding=''
	while(1):
		#判断循环是否结束
		if hex(Byte(str_addr))=='0x0':
			break
		#叠加字符串字符生成字符串
		tpadding+=chr(Byte(str_addr))
		str_addr+=1
	return tpadding
def getlast():
	#base=GetBase(0x6004)
	last=base[-12:]
	return last
def crazy(a,b):
	t1=a<<4
	t2=~b+1
	t2=0xD0-t2
	ans=(t2 ^ t1) | (t2 &t1 )
	return ans & 0xFF

def hehe2():
	AnsT=''
	AllT=[]
	AnsT=''
	Hehe3_8ToOrd()
	last=getlast()
	for i in range(0,len(hehe3_8_o)):
		t= []
		for j in last:
			for k in last:
				if crazy(ord(j), ord(k)) == hehe3_8_o[i]:
					t.append(j + k)
		AllT.append(t)
	for i in AllT:
		#在列表I中，找出任意值
		AnsT += choice(i)
	AnsTL = list(AnsT)
	index=[5,6,9,11,12,13,14,15]
	i=0
	#对列表值进行交换
	while i <len(index):
		i1=index[i]
		i2=index[i+1]
		i+=2
		t1=AnsTL[i1]
		t2=AnsTL[i2]
		AnsTL[i1]=t2
		AnsTL[i2]=t1
	str1=''.join(AnsTL)
	return str1
def hehe4():
	padding = '075e191fe314c1e7917d9c71f7b6ed9842090f28f649bad384d0880d103b99a8'
	str1=hehe2()
	#AnsCode相当于input，len为30
	AnsCode=pre6+'-'+str1+'-'+javastr
	enstr = AnsCode + padding
	ans = 0
	for i in enstr:
		t = ord(i) - (~(0x28 * ans) + 1)
		ans = t & 0xFFFFFFFF
	return AnsCode+str(ans)
keyTokey={}
def GetFlag():
	str1=hehe4()
	key1=base[26:52]+base[0:26]+base[-12:]
	key2=key1[13:26]+key1[0:13]+key1[39:52]+key1[26:39]+key1[57:62]+key1[52:57]+key1[-2:]
	#生成key的值对应字典
	for i in range(0,len(key2)):
		keyTokey[key2[i]] = key1[i]
	flag=''
	for i in str1:
		flag+=keyTokey[i]
	print 'flag: ',flag
GetFlag()
