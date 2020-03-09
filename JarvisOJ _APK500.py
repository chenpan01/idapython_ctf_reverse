#1.使用如下脚本可以获取关键字符串v50
# -*- coding:utf-8 -*-
def GetStr():
	#str_2C87字符串所在的位置
	str_addr=0x2C87
	tstr=''
	while(1):
		#判断循环是否结束
		if chr(Byte(str_addr))=='g' and chr(Byte(str_addr+1))=='X':
			break
		#叠加字符串字符生成字符串
		tstr+=chr(Byte(str_addr))
		str_addr+=1
	#加上最后两个字符
	return tstr+'gX'
print GetStr()
#对应ida中的strdeal函数
def strdeal(str,c):
	index=0
	s=''
	while(index<len(str)):
		v=ord(c)+index
		t=str[index]
		s+=chr(ord(t)^v)
		index+=1
	return s
s=GetStr()
print strdeal(s,'9')

#2.该脚本可以获取dword_4007正型数组中的值
def GetV():
	#str_2C87字符串所在的位置
	str_addr=0x400B
	tstr=''
	i=0
	while i<9:
		print Byte(str_addr),
		i+=1
		str_addr+=1
		
GetV()
#3.该脚本可以求解flag
s = "ddedd4ea2e7bef168491a6cae2bc660"
c1 = []
str_4004 = [133, 139, 236, 0x83, 0x6c, 0x9c, 0x83, 141, 12, 1, 117, 95, 198, 69, 243, 80]
#把十六进制数转换成十进制
def ChrToOrd(c,j):
	t=0x10
	#判断是否是个位数
	if j==2:
		t=0x1
	Hex=['a','b','c','d','e','f']
	Ord=[0xa,0xb,0xc,0xd,0xe,0xf]
	#如果是0-9的数
	if '0'<=c and '9'>=c:
		return (ord(c)-ord('0'))*t
	#如果是a-f的数
	for i in range(6):
		if Hex[i]==c:
			return Ord[i]*t
#把ans字符串中十六进制数转换成十进制
def getStrOrd(i):
	ord=[]
	j=0
	ans=0
	t=i
	#每两位进行转换
	while j<31:
		#ans追踪转换后的数值
		ans=0
		if j==t:
			ans+=0
			#如果j==i,把t标记为-1
			t=-1
		else:
			ans+=ChrToOrd(s[j],1)
			j+=1
			if j==31:
				ord.append(ans)
				break
		if j==t:
			ans+=0
			#如果j==i,把t标记为-1
			t=-1
		else:
			ans+=ChrToOrd(s[j],2)
			j+=1
		ord.append(ans)
	return ord
def getC1Sz():
	for i in range(32):
		t=getStrOrd(i)
		c1.append(t)
#判断是否为可见字符
def isSee(t):
	if(t>32 and t<127):
		return 0
	else:
		return 1
def getFlag():
	getC1Sz()
	for t in c1:
		XorC1 = []
		flag = ''
		print 't ',t
		for i in range(16):
			t1 = t[i]^str_4004[i]
			#print 'p ',p
			XorC1.append(t1)
		#XorC1对应str
		XorC1 = XorC1[-7:] + XorC1[:-7]
		#把str中的前四个元素减1
		for i in range(4):
			XorC1[i] = XorC1[i]- 1
		#把str中的每个元素进行异或处理
		for i in range(16):
			t2 = XorC1[i] ^ i
			#如果不是可见字符则退出
			if(isSee(t2)==1):
				break
			flag+= chr(t2)
		else:
			print flag
			break
getFlag()
