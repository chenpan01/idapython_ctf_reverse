#1.地址获取：
print hex(MinEA())
print hex(MaxEA()) 
print hex(ScreenEA())
for seg in Segments():  
    #如果为代码段，则调用GetStr
    if SegName(seg) == '.text':
        print hex(SegEnd(seg))
#2.数值获取
print isLoaded(0x401114)
 
print Byte(0x401114)
 
print Word(0x401114)
 
print Dword(0x401114)
 
print Qword(0x401114)
#3.操作码获取
print GetDisasm(0x401114) 
 
print GetOpnd(0x401114,1) 
 
print hex(GetFlags(0x401114)) 
 
print GetMnem(0x401114) 
 
print GetOpType(0x401114,1) 
 
print GetOperandValue(0x401114,1)
#4.搜索操作
print hex(FindBinary(MinEA(),SEARCH_DOWN,'41 42'))
 
print hex(FindCode(MinEA(),SEARCH_DOWN))  
 
print hex(FindData(MinEA(),SEARCH_DOWN))
#5.数据判断操作
print isCode(GetFlags(0x401114))
 
print isData(GetFlags(0x401114)) 
 
print isTail(0x401134) 
 
print isUnknown(0x401214) 
 
print isHead(0x401114)
#6.修改操作部分
PatchByte(0x401114,0x12)
 
PatchWord(0x401124,0x12456978)
 
PatchDword(0x401134,0x00000000)
#7.交互部分
AskYN(1,'is it?')
 
Jump(0x401114)
 
AskStr('hello!','please enter!')
 
Message('hello!')
#8.函数操作部分
for seg in Segments():  
 
    #如果为代码段
 
    if SegName(seg) == '.text':
 
        for function_ea in Functions(seg,SegEnd(seg)):
 
            FunctionName=GetFunctionName(function_ea)
 
            print FunctionName
 
            nextFunc=NextFunction(function_ea)
 
            print nextFunc
