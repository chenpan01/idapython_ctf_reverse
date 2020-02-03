#-*- coding:utf-8 -*-
ea=ScreenEA()
for seg in Segments(): #遍历所有的段
	if SegName(seg)=='.text': #代码段
		print 'SegStart(seg) ',SegStart(seg)
		print 'SegEnd(seg) ',SegEnd(seg)
		for function_ea in Functions(SegStart(seg), SegEnd(seg)):
			print hex(function_ea), GetFunctionName(function_ea)
