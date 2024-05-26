# # import ls7_module
# # a = int(input('hãy nhập số '))
# # b = int(input('hãy nhập số '))

# # ls7_module.sum(a,b)


    






























# # #b4
# numb = []
# p = 1
# while p != 0:
#     p = (input('Nhap 0 de hoang thanh mang: '))
#     if p != 0:
#         numb.append(p)


def sum_array():
    elements = []
    
    while True:
        element = input("Nhập một phần tử (hoặc nhấn Enter để kết thúc): ")
        if element == "":
            break
        elements.append(element)
    
    valid_numbers = []
    for element in elements:
        try:
            number = float(element)
            valid_numbers.append(number)
        except ValueError:
            print(f"'{element}' không phải là số, bỏ qua.")
    
    total_sum = sum(valid_numbers)
    
    return total_sum

print("Tổng của mảng là:", sum_array())


































































