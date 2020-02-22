def GetAns(start,end):
	flag=''
	for addr in range(start-4,end):
		#当前地址的下一个地址
		#判断下一个地址所在的指令是否为mov [esp+xxh], al
		if GetOpnd(addr,1)=='al' and 'esp' in GetOpnd(addr,0):
			#判断当前地址所有的指令是否是'mov  eax, xxh'
			if GetOpnd(addr-5,0)=='eax':
				#获取十六进制数
				hex=GetOpnd(addr-4,1)[:2]
				#转换成10进制数
				Int=int(hex,16)
				flag+=chr(Int)
				if chr(Int)=='}':
					break
	print flag
# 遍历所有的段
for seg in Segments():  
	#如果为代码段，则调用GetStr
	if SegName(seg) == '.text':
		GetAns(seg,SegEnd(seg))
