"""
             字符串的切片
"""
#  切片  [开始: 结束]  取左不取右
name = "巴若菡真漂亮，这是没办法的事情啦"
print(name[0:6])

#  切片  [开始:结束:步长]  取左不取右
print(name[:7:2])    #  步长指间隔
print(name[-6:])     #  负号从后数
print(name[-6::2])
print(name[-6::-1])  #  倒序
print(name[-12::-2])
print("==============分割线==============")
#  首位从0开始,末尾从-1开始,空格也记位置
a = " python"
print(a[0])
print(a[2])
print(a[-1])
print(a[-2])
print("==============分割线==============")
"""
               字符串的拼接   +
"""
b = '艾尔登'+"法环"
print(b)
c = '150009'+"15013"
print(c)

s = "你好噻"
d = "你是哪里人"
g = "在哪里上学?"

f = s+d+g
print(f)

h = '?'.join([s,d,g])
print(h)

v = s,d,g
print(v)
print("==============分割线==============")
"""
                     字符串的格式化   配合{}使用
                     format
"""
a2 = "大家好,我的名字叫{},今年{}岁,性别{}".format("叶盖","19","男")
print(a2)
a3 = "大家好,我的名字叫{1},今年{0}岁,性别{2}"
print(a3.format("叶盖","19","男"))
print("==============分割线==============")
"""
        find:查找元素位置    find("查找元素",起始位置.终止位置)
        count:统计出现次数   同上
"""
s2 = "maybe in the home"
print(s2.find("a"))
print(s2.count("h"))
print(s2.count(" "))
print(s2.count(" ",8))
print("==============分割线==============")
"""
               字符串的常用方法: 
               replace:  "要替换的","替换成","替换次数"(默认全部)   
               upper:小写升大写   lower:大写变小写
"""
c1 = "welcome to my house, it's my pleasure"
c2 = c1.replace("m","h")
print(c2)
print(c1.replace("m","h"))
c3 = c1.upper()
print(c3)
c4 = c3.lower()
print(c4)
print("==============分割线==============")
"""
             split:  分割函数  参数1:分割点   参数2:分割次数(默认全部)
             strip:  去除首尾空格
"""
x1 = "111ab222ab333ab444"
print(x1.split("a"))
print(x1.split("a",1))
x2 = "          hhhhh          "
print(x2.strip())
x3 = '666hhhhhhh666'
print(x3.strip('6'))
x4 = '         6666666      7777777'
print(x4.replace(' ',''))    #  灵活运用replace可以替代strip作用
print(x4.strip())
print("==============分割线==============")





