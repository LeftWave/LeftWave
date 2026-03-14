import random

# 问候语列表
greetings = ["你好", "Hello", "Bonjour", "Hola", "こんにちは"]

# 随机选一个问候语
greeting = random.choice(greetings)

# 生成1-100随机数
number = random.randint(1, 100)

print("问候语:", greeting)
print("随机数字:", number)
