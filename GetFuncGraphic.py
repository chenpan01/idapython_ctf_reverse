# -*- coding:utf-8 -*-
from sets import Set
import pydot
 
# 获取段的起始地址
ea = ScreenEA()
 
callers = dict()
callees = dict()
 
# 遍历所有的函数
for function_ea in Functions(SegStart(ea), SegEnd(ea)):
 
    f_name = GetFunctionName(function_ea)
     
    # 遍历每个函数的引用函数
    for ref_ea in CodeRefsTo(function_ea, 0):
     
        # 引用函数名
        caller_name = GetFunctionName(ref_ea)
         
          #将当前函数添加到引用函数调用的函数列表中   
        callees[caller_name] = callees.get(caller_name, Set())
        
        callees[caller_name].add(f_name)
 
 #创建图像对象       
g = pydot.Dot(type='digraph')
 
#设置默认值
g.set_rankdir('LR')
g.set_size('11,11')
g.add_node(pydot.Node('node', shape='ellipse', color='lightblue', style='filled'))
g.add_node(pydot.Node('edge', color='lightgrey'))
 
 
#获取所有函数
functions = Set(callees.keys()+callers.keys())
 
# 对于每个函数和每个被引用的函数，添加相应的边。
for f in functions:
    if callees.has_key(f):
        for f2 in callees[f]:
            g.add_edge(pydot.Edge(f, f2))
             
# 将输出写入到Postscript文件
g.write_ps('example6.ps')
