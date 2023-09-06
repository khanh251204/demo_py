list_a = [1,2,3,4,5,6,7]
#Thêm phần tử list a

# count để tìm phần tử trùng nhau
print(list_a.count(1))
# Sử dụng index để tìm vị trong list
print(list_a.index(6))
# Để tạo một list tương tự list với y/c thì dùng copy
b = list_a.copy()
# print(b)
#Xóa 1 phần tử trong list thì ta dung remove
print(b.clear())
#Đảo ngược list a
list_a.remove(4)
print (list_a[::-1])
list_a.reverse()
print (list_a)