# 创建变量并赋值
types_of_people = 10
# 创建字符串变量
x = f"There are {types_of_people} types of people."

# 创建字符串变量
binary = "binary"
# 创建字符串变量
do_not = "don't"
# 创建格式化字符串变量
y = f"Those who know {binary} and those who {do_not}."

# 打印字符串
print(x)
print(y)

# 打印字符串
print(f"I said: {x}")
print(f"I also said: '{y}'")

# 创建 bool 变量并赋值
hilarious = False
# 创建格式化字符串
joke_evaluation = "Isn't that joke so funny? {}!"

# 打印字符串
print(joke_evaluation.format(hilarious))

# 创建字符串变量并赋值
w = "This is the left side of..."
e = "a string with a right side."

# 拼接字符串
print(w + e)

print(joke_evaluation.format(True))
