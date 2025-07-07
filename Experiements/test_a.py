code = ()=>{}
a = code()
print(a)

# 测试带参数的箭头函数
add = (x, y)=>{return x + y}
result = add(3, 5)
print(result)

# 测试单参数箭头函数
double = (x)=>{return x * 2}
print(double(4))

# 测试空参数但有返回值的箭头函数
get_five = ()=>{return 5}
print(get_five())