# -*- coding:utf-8 -*-
def GetStr(start,end):
	flag=''
	for addr in range(start,end):
		#判断有没有找到'mov  esi, offset flag'
		if GetOpnd(addr,0)=='esi' and 'flag' in GetOpnd(addr,1):
			#获取flag所在的地址
			address=hex(Dword(addr))[0:8]
			#把地址转换成十进制数
			taddress=int(address,16)
			#使用循环结构获取flag
			while(1):
				
				flag+=chr(Byte(taddress))
				#判断flag读取是否结束
				if chr(Byte(taddress))=='}':
					break
				taddress+=1
			print flag
			break
		

for seg in Segments():  # 遍历所有的段
	#如果为代码段，则调用GetStr
	if SegName(seg) == '.text':
		GetStr(seg,SegEnd(seg))
