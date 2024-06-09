# thisdict = {
#     'class_name' : "csb03",
#     'years' : 2024,
#     'stu_count':10
# }

# ## #accees
# # print(thisdict['class_name'])

# ## #change item
# # thisdict['stu_count'] = 9
# # print(thisdict['stu_count'])

# ## #add item
# # thisdict["newstu"] = 'Ngọc'
# # print(thisdict)

# ##remove items
# # thisdict.pop('newstu')

# ##remove last
# #thisdict.popitem()
# # print(thisdict)

# ##duyet all key
# # for y in thisdict: 
# #     print(y)

# ##duyet value
# # for x in thisdict:
# #     print(thisdict[x])

# ##duyet key value
# # for a,b in thisdict.items():
# #     print(a,b)

# ##copy
# # new_dict = thisdict.copy()
# # print(new_dict)

# #nested dict
# my_class ={
#     "student":{
#         'name':'Tai',
#         'age':18
#     },
#     'stu2':{
#         'name':'Ngoc',
#         'age':15
#     },
#     'stu3':{
#         'name':'Lam',
#         'age':17
#     }
# }

# # for x,y in my_class:
# #     print(x)
# #     for i in y:
# #         print(i + ':',y[i])

# # for i in my_class.values():
# #     print(i['name'])

# for x,y in my_class.items():
#     print(y['name'])

##b1
# my_dict={
#     'HP': 20,
#     'DELL': 50,
#     'MACBOOK': 12,
#     'ASUS': 30
# }
# for a,b in my_dict.items():
#     print(a,b)

# print(f"There are {my_dict['MACBOOK']} macbook there")
# x = str(input('nhập hãng (nhớ viết hoa) '))
# if x in my_dict:
#     print(f"There are {my_dict[x]} {x} there")
# else:
#     print('nhập sai')

##b2
# character = {
#     'Name':'Light',
#     'Age': 17,
#     'Strength': 8,
#     'Defense': 10,
#     'HP': 100,
#     'Backpack': 'Shield, Bread Loaf',
#     'Gold': 100,
#     'Level': 2
# }
# character['Gold'] = character['Gold']+50
# print(character['Gold'])

# character['Backpack'] = character['Backpack']+',FlintStone'
# print(character['Backpack'])

# character['Pocket'] = ['MonsterDex', 'Flashligh']
# print(character['Pocket'])

students_details = {
    "Alice": {"age": 20, "score": 85},
    "Bob": {"age": 22, "score": 92},
    "Charlie": {"age": 21, "score": 78}
}
#p1
if 'David' in students_details:
    print('David in dic')
else:
    print('david is not in dic ')

#p2
new_detail = {}
for a,b in students_details.items(
    
):
    z = b["score"]
 























































































































































































































