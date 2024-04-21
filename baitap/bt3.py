# #1
# so = int(input("nhập số"))
# if so % 2 == 0:
#     print("số này là số chẵn")
# else:
#     print("số này là số lẽ")


# #b2
# SO = input("Nhập số ")
# x = int(SO)
# if SO == x:
#     print("đây là số nguyên")
# else:
#     print('đây không phải là số nguyên')


# #b3
# b3 = input('hãy nhập ký tự ')
# if b3 == int(b3):
#     print('đây là số')


# #b5
# name = str(input("hãy nhập tên đăng nhập"))
# passw = str(input("hãy nhập mật khẩu"))
# if name == "admin" & passw == "12345":
#     print('đã hoàn tất đăng nhập')
# else:
#     print('sai tên hoặc mật khẩu')

# #b6
# a = int(input('nhập độ dài cạnh 1 '))
# b = int(input('nhập độ dài cạnh 2 '))
# c = int(input('nhập độ dài cạnh 3 '))
# if (a+b > c)or(a+c>b)or(c+b>a) & a>0 &b>0&c>0 :
#     print('thỏa mãn bất đẳng thức')
# else:    
#     print("không thỏa mãn bất đẳng thức")

#
a = int(input('nhập độ dài cạnh 1 '))
b = int(input('nhập độ dài cạnh 2 '))
c = int(input('nhập độ dài cạnh 3 '))
if (a+b > c)or(a+c>b)or(c+b>a) & a>0 &b>0&c>0 :
    print('thỏa mãn bất đẳng thức')
else:    
    print("không thỏa mãn bất đẳng thức")
if (a*a == b*b + c*c)or (b*b == c*c+b*b)or (c*c==b*b+a*a):
    print("tam giác này là tam giác vuông")
if a == b == c :
    print('đây là tam giác đều')
    from turtle import *
    pen()
    left(90)
    forward(a)
    right(120)
    forward(a)
    right(120)
    forward(a)
    






























