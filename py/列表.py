"""
    列表
"""
list1 = [1, 4, 6, 9, "巴若菡", [12, 32]]
print(list1[4])
print(list1[5])
print(list1[5][1])
print("==============分割线==============")




"""
    列表长度  len()
    列表内容的更新
"""
print(len(list1))
x = "python"
print(len(x))
list1[3] = "爱你"
print(list1)
print("==============分割线==============")




"""
     列表的加法和乘法运算操作
"""
list2 = [5, 6, 7]
print(list1 + list2)
print(list1*2)
print(x*4)
print("==============分割线==============")




"""
    列表的切片取值
"""
print(list2[:2])
print(list1[:7:2])
print(list1[:])
print(list1[::-1])
print("==============分割线==============")



"""
    1.del 关键字  用于删除
    2.append    用于向列表末尾加元素
    3.extend    用于列表相加,等于+号
"""
a = [1, 20, 30, 4, 5]
del a  # 从计算机内存中删除
# print(a)
b = [2, 3, 5, 7, 89, 0, 5]
del b[6]  # 删除单个内容
print(b)
list3 = [1, 2, 3]
list3.append("nihao")
print(list3)
list3.append([2])
print(list3)
list3.append(99)
print(list3)
list3.extend([23, 43, 14])
print(list3)
print("==============分割线==============")




"""
    insert 插入一个值,  第一个参数为位置,第二个参数为替换值
    clear  清空当前列表
"""
list3.insert(1, [23, 3])
print(list3)
list3.clear()
print(list3)
print("==============分割线==============")




"""
    remove  移除所选的元素,如果有多个相同元素则删除第一个
    pop     移除所选下标位置的元素并有返回值,默认删除最后一个
"""
a = ["hello", "world", "god boy", "hello", "python", "hello"]
a.remove("hello")
print(a)
print("原本的列表", a)
print("要移除的元素", a.pop(2))
print("移除后的列表", a)
print("==============分割线==============")




"""
    index  索引并查找元素的下标值,  index("对象",起始,结束)
    reverse  逆转,反转
"""
c=["hello","world","god boy","hello","python","hello"]
r = c.index('hello')
print(c.index('hello'))
print(r)
#  r2 = c.index("1")
#  print(r2)
r3 = c.reverse()
print(r3)
print("==============分割线==============")




"""
    copy:  复制并创建副本
"""
d = ["ader", 2333, "666"]
s = d.copy()
del d[0]
print(s)
x = d
print(x)
print("==============分割线==============")




"""
    sort    对于列表进行排序,ascii码升序进行排序,0~9<A~Z<a~z
"""
s1 = ["tuihuan", "好好好", "多来点", "timi", "sodayo", "meimaob", "21"]
s1.sort()
print(s1)
s2 = [1, 5, 3, 7, 4, 6]
s2.sort()
print(s2)
s3 = s2
s3.sort(reverse=True)
print("==============分割线==============")



"""
    count    统计元素的出现次数 
"""
x1 = [1, 2, 3, 5, 7, 1, 3, 5, 2, 1]
x2 = x1.count(1)
print(x2)
print("==============分割线==============")