#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("Mary had a little lamb.")
# 打印格式化字符串
print("Its fleece was white as {}.".format("snow"))
print("And everywhere that Mary went.")
# 重复打印 10 次 * 
print("." * 10) # what'd that do?

end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# watch that comma at ehte end. try removing it to see what happens
# 打印 Cheese，并指定字符串尾的字符为空格而不是默认的换行符
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
# 打印 Burger，使用 + 拼接字符串
print (end7 + end8 + end9 + end10 + end11 + end12)


import time
print("Loading", end='')
for i in range(20):
    print('.', end='', flush=True)
    time.sleep(0.5)
