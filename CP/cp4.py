#p1
#b1
thisdict = {
    'HP':20,
    'DELL':50,
    'MACBOOK': 12,
    'ASUS': 30
}
# print(thisdict)
# #b2
# print("THERE ARE " ,thisdict['MACBOOK'], 'IN THERE!')
# #B3
# a = str(input('nhập hãng (viết hoa): '))
# if a in thisdict:
#  print(a, thisdict[a])
# else:
#  print('illegal input')
#p2
# #b1
# thisdict['TOSHIBA']= 10
# print(thisdict)


# #
# x = str(input('Hãy nhập hãng(viết hoa): '))
# y = int(input('Hãy nhập số lượng: '))
# thisdict[x] = y

# #b3
# thisdict['DELL']= 60
# thisdict['MACBOOK']= 2

# #b4
# #duyet key value
# c = 0
# for a,b in thisdict.items():
#     c = c+b
# print(c)

#p3
#b1
mydict = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}

# #b2
# print('giá máy asus là: ' ,mydict['ASUS'])

# #b3
# q = str(input('Nhập hãng(viết hoa): '))
# if q in mydict:
#     print(mydict[q])
# else:
#     print('illegal brand')


# #p4
# #b1
# w = mydict['ASUS']
# print(f"giá 5 máy asus là: {5*w}")

#b2

# e = str(input('nhập hãng(viết hoa): '))
# r = int(input('nhập số lượng: '))
# t = mydict[e]
# if e in mydict:
#  print(f"giá tiền của {r} máy {e} là: {r*t}")
# else:
#  print('nhập sai')

# #b3
# u = str(input('nhập hãng(viết hoa): '))
# p = mydict[u]
# o = int(input('nhập số lượng: '))
# if u in mydict:
#     print(f'total price: {p*o}')
# else:
#     print('nhập sai')
# thisdict[u]= (thisdict[u] - o)
# print(thisdict)

#p5
#b1
# new_d = {}
# new_d['DELL']= (thisdict['DELL'] + mydict['DELL'] )
# new_d['ASUS']= (thisdict['ASUS'] + mydict['ASUS'] )
# new_d['MACBOOK']= (thisdict['MACBOOK'] + mydict['MACBOOK'] )
# new_d['HP']= (thisdict['HP'] + mydict['HP'] )
# print(new_d)

# #b2
# i = 0
# for s,d in new_d.items():
#     i = i+d
# print(i)


#p6
# #b1
# main = {
#     'Name': 'Light',
#      'Age': 17,
#     'Strength': 8,
#     'Defense': 10,
#     'HP': 100,
#     'Backpack': 'Shield, Bread Loaf',
#      'Gold': 100,
#      'Level': 2
# }

# #b2
# main['Gold'] = main['Gold'] + 50

# print(main["Gold"])

# #b3
# main['Backpack'] = (main['Backpack'],'FlintStone')
# print(main['Backpack'])

#p7
#b1
ultimate = {
 'skill1':{
    'Name': 'Tackle',
    'Minimum level': 1,
    'Damage': 5, 
    'Hit rate': 0.3
 },
 'skill2':{
     'Name': 'Quick Attack', 
     'Minimum level': 2, 
     'Damage': 3, 
     'Hit rate': 0.5
 },
 'skill3':{
      'Name': 'Strong Kick', 
      'Minimum level': 4, 
      'Damage': 9, 
      'Hit rate': 0.2
 }
}
#b2












































































































































































































































































