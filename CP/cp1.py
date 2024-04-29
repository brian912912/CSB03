#P1

##b1
# f_name = input("Nhập tên của bạn")
# l_name = input("Nhập họ của bạn")
# print("Your full name is ", f_name, l_name)



# ##B2
# inp = input('nhập tên  ')
# print(inp.upper())

#b3
# a = int(input('nhập độ dài'))
# print(float(a*a))

# #b4
# r = float(input("Input circle's radius: "))
# import turtle
# turtle_3 = turtle.Turtle()
# turtle_3.circle(r)
# turtle.mainloop()

#p2
#b1
# for i in range(3,13):
#     print(i)

#b2
# b = int(input('hãy nhập số'))
# if b>0:
#   for o in range(0,b+1):
#     print(o)
# else:
#   print('sai điều kiện')

#b3
# c = int(input('hãy nhập số '))
# if c>0:
#   for l in range(1, c+1,2):
#     print(l)
# else:
#   print('sai điều kiện')


# #b4
# p = int(input('nhập số cạnh'))
# from turtle  import *
#if p >0:
#  for p in range (1,p+1):
#     forward(50)
#     left(360/p)
#else:
#  print('sai điều kiện rồiiiiii')


#p3
#b1
# n = int(input('nhập số'))
# if n > 13:
#     print('số này lớn hơn 13')
# else:
#     print('số này không lớn hơn 13')

#b2
# x = int(input('nhập số'))
# if x%2 == 0:
#     print('số này là số chẵn')
# else:
#     print('số này là số lẻ')

#b3
# m = int(input('nhập tháng'))
# if (m<=0) or  (m >12):
#     print('tháng không hợp lệ')
# else:
#     if m ==2:
#         print('tháng này có 28 ngày')
#     elif (m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12) :
#         print('tháng này có 31 ngày')
#     else:
#         print('tháng này có 30 ngày')


#p4
#b1
# r = 0
# while r<10:
#  name = str(input("hãy nhập tên đăng nhập"))
#  passw = str(input("hãy nhập mật khẩu"))
#  email = str(input('hãy nhập email'))
#  if name != "" and passw!="" and email!="":
#     print('đăng nhập thành công')
#     break
#  else:
#     print('không được để trống')
#     r+=1

#b2
# e = 0
# while e < 10:
#     e+=1
#     name = str(input("hãy nhập tên đăng nhập "))
#     passw = str(input("hãy nhập mật khẩu "))
#     r_passw = str(input('hãy nhập lại password '))
#     email = str(input('hãy nhập email '))
#     if (name != "") and (passw!="") and (email!="") and (r_passw!=""):
#         if passw==r_passw:
#             print('đăng nhập thành công')
#             break
#         else:
#             print('hãy nhập lại pass word')
#             passw = str(input("hãy nhập mật khẩu"))
#     else:
#         print('không được để trống')


# #b3
#y=0
#while i<10:
#  y+=1   
#  name = str(input("hãy nhập tên đăng nhập"))
#  passw = str(input("hãy nhập mật khẩu"))
#  r_passw = str(input('hãy nhập lại password'))
#  email = str(input('hãy nhập email'))
#  if "@" and "." in email:
#    print('email hợp lệ')
#    if name != "" and passw!="" and email!="" and r_passw!="":
#     if passw==r_passw & len(passw) >= 8 and passw.isalnum() == True:
#         print('đăng nhập thành công')
#           break
#     else:
#         print('hãy đăng nhập lại')
#    else:
#         print('không được để trống')
#  else:
#     print('email không hợp lệ')
#     























































































































