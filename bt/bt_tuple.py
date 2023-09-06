#1, 2 Tạo 1 tuple , có các kiểu dữ liệu khác nhau
tup_tao = (1,2,3,4,'Khánh',[1,2,3])
print(tup_tao)
# In ra tuple có kiểu dữ liệu số
tup_int = (1,2,3,4)
print(tup_int)
# Thêm phần tử tuple
tup_append = (1,2,3,4,5)
new_tup_append = tup_append + (6,7,8)
print(new_tup_append)
# Ép kiểu tuple về kiểu string
str_tuple = str(tup_append)
print(type(str_tuple))
#Lấy phần tử thứ 4 từ cuối lên 
index_tuple = (1,2,3,4,5)
print (index_tuple.index(-4))

