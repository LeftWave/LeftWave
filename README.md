## Hi there 👋

<!--
**LeftWave/LeftWave** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
# 功能：生成随机问候语+1-100的随机数，适合测试上传GitHub
import random

# 定义问候语列表
greetings = ["你好呀！", "Hello!", "Bonjour!", "Hola!", "こんにちは！"]
# 随机选1个问候语
random_greeting = random.choice(greetings)
# 生成1-100的随机整数
random_number = random.randint(1, 100)

# 打印结果
print("🎯 随机问候：", random_greeting)
print("🎲 随机数字（1-100）：", random_number)

# 额外小功能：判断随机数奇偶性
if random_number % 2 == 0:
    print(f"✨ 数字 {random_number} 是偶数～")
else:
    print(f"✨ 数字 {random_number} 是奇数～")
