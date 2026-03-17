# Python 程序员实战指南：2026 年最全学习教程

> 从入门到精通，涵盖 Web 开发、数据分析、人工智能、自动化运维等全栈技能

---

## 前言：为什么选择 Python？

Python 是一门"可执行的伪代码"（executable pseudocode），让开发者能用更少的代码表达更多逻辑。在 2026 年的今天，Python 已经成为全球最流行的编程语言之一。

### Python 的核心优势

- **简洁高效**：一行代码完成列表过滤，用其他语言可能需要 10+ 行
- **生态丰富**：PyPI 已有 40 万 + 包，涵盖 AI、Web、数据分析、自动化
- **多范式支持**：面向对象、函数式、过程式编程样样精通
- **胶水语言**：轻松集成 C/C++/Java/.NET，调用其他语言实现的库
- **社区活跃**：Google、Meta、Netflix、Dropbox 等大厂核心业务都在用

### 一行代码领略 Python 之美

```python
# 列表推导式 - 简洁又高效
squares = [x**2 for x in range(10)]

# 快速排序 - 仅用 3 行
def qsort(arr):
    return qsort([x for x in arr[1:] if x <= arr[0]]) + [arr[0]] + \
           qsort([x for x in arr[1:] if x > arr[0]]) if arr else []

# 文件读取 - with 自动管理资源
with open('data.txt') as f:
    content = f.read()
```

### Python 能做什么？

- **Web 开发**：Django、FastAPI、Flask
- **数据科学**：Pandas、NumPy、Matplotlib
- **AI/ML**：TensorFlow、PyTorch、Keras、Transformers
- **自动化脚本**：文件处理、爬虫、测试自动化
- **DevOps**：Ansible、SaltStack、Fabric

---

## 第一部分：Python 基础入门

### 1.1 安装 Python（2026 最佳实践）

**快速安装（推荐）**

```bash
# macOS
brew install python@3.14

# Linux (Ubuntu/Debian)
sudo apt update && sudo apt install python3.14 python3.14-venv python3.14-dev

# Windows - 从 python.org 下载或使用 winget
winget install Python.Python.3.14
```

**pyenv 多版本管理**

```bash
# 安装 pyenv
curl https://pyenv.run | bash

# 安装多个版本
pyenv install 3.14.0
pyenv install 3.13.0

# 项目切换版本
cd myproject
pyenv local 3.13.0  # 自动创建 .python-version

# 验证
python --version
```

### 1.2 基础语法

**Hello World 与注释**

```python
print("Hello, World!")  # 输出

# 多行注释用三引号
"""
这是文档字符串
也是多行注释
"""
```

**缩进 - Python 的灵魂**

```python
if True:
    print("缩进表示代码块")
    if False:
        print("嵌套缩进")
print("这是外层")  # 缩进错误会导致 IndentationError

# PEP 8: 使用 4 空格，禁止 Tab 混用
```

> ⚠️ **注意**：缩进是 Python 语法的一部分，缩进不一致会报错。推荐使用空格而非 Tab。

### 1.3 变量与数据类型

**变量命名规范**

```python
# 基础类型
name = "张三"      # str
age = 25           # int
height = 1.75      # float
is_active = True   # bool

# 变量命名规范
user_name = "valid"    # 小写 + 下划线
UserName = "Pascal"   # 类名用 PascalCase
CONSTANT = 3.14       # 常量用全大写

# 链式赋值
a = b = c = 0

# 多元解包
x, y, z = 1, 2, 3
first, *rest = [1, 2, 3, 4]  # first=1, rest=[2,3,4]
```

**核心数据类型**

```python
# 数值
x = 10        # int
y = 3.14      # float
z = 1+2j      # complex 复数

# 字符串 - 不可变
s = "hello"
s = 'world'
s = """多行
字符串"""

# 列表 - 可变，有序
nums = [1, 2, 3]
nums.append(4)
nums[0] = 0

# 元组 - 不可变，有序
point = (10, 20)
x, y = point  # 解包

# 字典 - 可变，键值对
user = {"name": "张三", "age": 25}
user["city"] = "北京"

# 集合 - 无序，不重复
unique = {1, 2, 3}
unique.add(4)
unique.add(1)  # 重复无效

# 布尔值
is_valid = True
is_empty = False
bool(0)  # False
bool([])  # False
bool("")  # False
```

**类型转换**

```python
int("42")     # "42" -> 42
float("3.14") # "3.14" -> 3.14
str(42)       # 42 -> "42"
bool(1)       # True
list("abc")   # ['a', 'b', 'c']
set([1,2,2])  # {1, 2}
```

> 💡 **可变 vs 不可变**：
> - **不可变**：int, float, str, tuple, frozenset
> - **可变**：list, dict, set
> - ⚠️ 函数参数传递时注意：可变对象在函数内修改会影响外部

### 1.4 控制流

**条件语句**

```python
age = 18

if age >= 18:
    print("成年人")
elif age >= 13:
    print("青少年")
else:
    print("儿童")
```

**循环**

```python
# for 循环
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(fruit)

# 使用 range()
for i in range(5):
    print(i)  # 输出：0, 1, 2, 3, 4

# while 循环
count = 0
while count < 5:
    print(count)
    count += 1

# break 和 continue
for i in range(10):
    if i == 5:
        break
    print(i)  # 输出：0, 1, 2, 3, 4

for i in range(5):
    if i == 2:
        continue
    print(i)  # 输出：0, 1, 3, 4
```

### 1.5 函数

**函数定义与调用**

```python
def greet(name: str) -> str:
    """带类型提示的函数"""
    return f"Hello, {name}!"

# 调用
result = greet("Python")
print(result)  # Hello, Python!
```

**参数类型全解**

```python
# 位置参数 vs 关键字参数
def f(a, b, c=10): pass
f(1, 2)           # 位置
f(a=1, b=2)       # 关键字
f(1, b=2)         # 混合

# *args **kwargs - 可变参数
def sum_all(*args, **kwargs):
    print(args)    # (1, 2, 3) 元组
    print(kwargs)  # {"x": 1, "y": 2} 字典

sum_all(1, 2, 3, x=1, y=2)

# 仅关键字参数 (Python 3+)
def f(*, key=None):  # 必须用关键字传参
    print(key)
f(key="value")
```

**Lambda 匿名函数**

```python
# 单行简单函数
square = lambda x: x ** 2
print(square(5))  # 25

# 配合内置函数
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x%2==0, nums))

# sorted 配合 lambda
users = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]
sorted_users = sorted(users, key=lambda x: x["age"])
```

> 💡 **技巧**：过度使用 lambda 会降低可读性，复杂逻辑还是用 def 定义函数。

### 1.6 面向对象编程

**类与对象**

```python
class Person:
    # 类属性 - 所有实例共享
    species = "Homo sapiens"

    def __init__(self, name: str, age: int):
        # 实例属性
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

# 创建实例
p = Person("张三", 25)
print(p)  # Person(name='张三', age=25)
```

**继承与多态**

```python
class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# 多态
def make_speak(animal: Animal):
    print(animal.speak())

make_speak(Dog())  # Woof!
make_speak(Cat())  # Meow!
```

**特殊方法 (Dunder Methods)**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):        # +
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):        # ==
        return self.x == other.x and self.y == other.y

    def __str__(self):              # str()
        return f"Point({self.x}, {self.y})"

    def __repr__(self):             # repr()
        return f"Point(x={self.x}, y={self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Point(4, 6)
```

**property 装饰器**

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # 私有属性

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.area)      # 78.53975
c.radius = 10
print(c.area)      # 314.159
```

**数据类 (Python 3.7+)**

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    age: int
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("年龄不能为负")

user = User("张三", 25, tags=["admin", "vip"])
print(user)  # User(name='张三', age=25, tags=['admin', 'vip'])
```

> 💡 **建议**：简单数据结构优先用 dataclass，减少样板代码。

### 1.7 字符串格式化

**f-string（推荐，Python 3.6+，3.12+ 增强）**

```python
# 基本使用
name = "张三"
age = 25
print(f"姓名：{name}, 年龄：{age}")

# 表达式
print(f"明年年龄：{age + 1}")

# 格式化数字
price = 1234.5678
print(f"价格：{price:.2f}")  # 保留两位小数
print(f"百分比：{0.1234:.2%}")  # 百分比

# 对齐和填充
print(f"{'左对齐':<20}")  # 左对齐，宽度 20
print(f"{'右对齐':>20}")  # 右对齐，宽度 20
print(f"{'居中':^20}")    # 居中，宽度 20

# 数字格式化
number = 1234567
print(f"千分位：{number:,}")  # 1,234,567
print(f"科学计数：{number:e}")  # 1.234567e+06

# 填充 0
print(f"编号：{5:03d}")  # 005

# 调用方法
text = "hello world"
print(f"大写：{text.upper()}")

# 字典访问
person = {"name": "李四", "age": 30}
print(f"姓名：{person['name']}, 年龄：{person['age']}")

# 列表访问
items = ["apple", "banana", "orange"]
print(f"第一个：{items[0]}")

# 格式化日期
from datetime import datetime
now = datetime.now()
print(f"当前时间：{now:%Y-%m-%d %H:%M:%S}")
```

---

## 第二部分：文件操作

### 2.1 文件读写

**with 自动管理资源**

```python
# 读取
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 逐行读取（内存高效）
with open("file.txt") as f:
    for line in f:
        print(line.strip())

# 写入
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")

# 追加
with open("log.txt", "a") as f:
    f.write("new entry\n")
```

### 2.2 pathlib 现代路径操作

```python
from pathlib import Path

p = Path("project/src/main.py")

p.exists()      # 文件存在
p.is_file()     # 是文件
p.is_dir()      # 是目录
p.parent        # 父目录
p.name          # 文件名
p.stem          # 不带扩展名的文件名
p.suffix        # 扩展名

# 创建目录
Path("new_dir").mkdir(parents=True, exist_ok=True)

# 遍历文件
for p in Path(".").rglob("*.py"):
    print(p)
```

### 2.3 目录操作

**使用 pathlib（推荐）**

```python
from pathlib import Path

# 获取当前目录
current_dir = Path.cwd()
print(f"当前目录：{current_dir}")

# 创建目录
new_dir = Path("my_folder")
new_dir.mkdir(exist_ok=True)

# 创建嵌套目录
nested_dir = Path("parent/child/grandchild")
nested_dir.mkdir(parents=True, exist_ok=True)

# 遍历目录
for item in current_dir.iterdir():
    if item.is_file():
        print(f"文件：{item.name}")
    elif item.is_dir():
        print(f"目录：{item.name}")

# 获取所有 Python 文件
python_files = list(current_dir.glob("*.py"))
print(f"Python 文件：{[f.name for f in python_files]}")
```

**遍历目录树**

```python
import os

# 遍历目录树
for root, dirs, files in os.walk("."):
    print(f"当前目录：{root}")
    print(f"子目录：{dirs}")
    print(f"文件：{files}")
    print("-" * 40)

# 使用 pathlib 递归遍历
from pathlib import Path
for path in Path(".").rglob("*.py"):
    print(f"Python 文件：{path}")
```

### 2.4 异常处理

**基本异常处理**

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("错误：不能除以零")

try:
    number = int(input("请输入一个数字："))
    print(f"你输入的数字是：{number}")
except ValueError:
    print("错误：请输入有效的数字")
except Exception as e:
    print(f"发生了未知错误：{e}")
```

**else 和 finally**

```python
try:
    file = open('example.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("文件不存在")
else:
    # 没有异常时执行
    print(f"文件内容：{content}")
finally:
    # 无论是否有异常都会执行
    print("操作完成")
    if 'file' in locals():
        file.close()
```

**自定义异常**

```python
class InvalidAgeError(Exception):
    """自定义异常"""
    pass

def set_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError("年龄必须在 0 到 150 之间")
    return age

try:
    set_age(200)
except InvalidAgeError as e:
    print(f"捕获到自定义异常：{e}")
```

### 2.5 PDF 文件操作（PyPDF2）

**安装**

```bash
pip install PyPDF2
```

**读取 PDF 信息**

```python
from PyPDF2 import PdfReader

# 读取 PDF 文件
reader = PdfReader('example.pdf')

# 获取页数
print(f"总页数：{len(reader.pages)}")

# 获取 PDF 信息
info = reader.metadata
print(f"标题：{info.get('/Title', '未知')}")
print(f"作者：{info.get('/Author', '未知')}")

# 读取第一页
page = reader.pages[0]
print(f"第一页内容：{page.extract_text()}")
```

**合并 PDF 文件**

```python
from PyPDF2 import PdfMerger

# 创建合并器
merger = PdfMerger()

# 添加 PDF 文件
merger.append('file1.pdf')
merger.append('file2.pdf')
merger.append('file3.pdf')

# 保存合并后的 PDF
merger.write('merged.pdf')
merger.close()
```

**分割 PDF 文件**

```python
from PyPDF2 import PdfReader, PdfWriter

# 读取 PDF
reader = PdfReader('example.pdf')

# 分割：提取前 3 页
writer = PdfWriter()
for i in range(3):
    writer.add_page(reader.pages[i])

# 保存
with open('first_3_pages.pdf', 'wb') as f:
    writer.write(f)
```

### 2.6 Word 文档操作（python-docx）

**安装**

```bash
pip install python-docx
```

**创建 Word 文档**

```python
from docx import Document
from docx.shared import Pt, RGBColor, Inches

# 创建文档
doc = Document()

# 添加标题
doc.add_heading('文档标题', level=0)
doc.add_heading('一级标题', level=1)
doc.add_heading('二级标题', level=2)

# 添加段落
paragraph = doc.add_paragraph('这是一个普通段落。')

# 添加带格式的段落
paragraph = doc.add_paragraph()
run = paragraph.add_run('这是粗体文本。')
run.bold = True

run = paragraph.add_run(' 这是斜体文本。')
run.italic = True

run = paragraph.add_run(' 这是下划线文本。')
run.underline = True

# 添加列表
doc.add_paragraph('无序列表项 1', style='List Bullet')
doc.add_paragraph('无序列表项 2', style='List Bullet')
doc.add_paragraph('有序列表项 1', style='List Number')
doc.add_paragraph('有序列表项 2', style='List Number')

# 保存文档
doc.save('example.docx')
```

**添加表格**

```python
from docx import Document

doc = Document()

# 添加表格
table = doc.add_table(rows=4, cols=3)
table.style = 'Table Grid'

# 设置表头
header_cells = table.rows[0].cells
header_cells[0].text = '姓名'
header_cells[1].text = '年龄'
header_cells[2].text = '城市'

# 填充数据
data = [
    ['张三', 25, '北京'],
    ['李四', 30, '上海'],
    ['王五', 28, '广州']
]

for i, row_data in enumerate(data):
    row = table.rows[i + 1]
    row.cells[0].text = row_data[0]
    row.cells[1].text = str(row_data[1])
    row.cells[2].text = row_data[2]

doc.save('table_example.docx')
```

### 2.7 文档模板生成（docxtpl）

**安装**

```bash
pip install docxtpl
```

**基本使用**

```python
from docxtpl import DocxTemplate

# 加载模板
doc = DocxTemplate("template.docx")

# 准备数据
context = {
    'name': '张三',
    'age': 25,
    'city': '北京',
    'hobbies': ['阅读', '编程', '旅行']
}

# 渲染模板
doc.render(context)

# 保存文档
doc.save("output.docx")
```

**模板语法（Jinja2）**

```python
# 在 Word 模板中使用以下语法：

# 简单变量
{{ name }}

# 条件判断
{% if age >= 18 %}
成年人
{% else %}
未成年
{% endif %}

# 循环
{% for hobby in hobbies %}
- {{ hobby }}
{% endfor %}

# 表格
| 姓名 | 年龄 | 城市 |
|------|------|------|
{% for person in persons %}
| {{ person.name }} | {{ person.age }} | {{ person.city }} |
{% endfor %}
```

**批量生成文档**

```python
from docxtpl import DocxTemplate

# 加载模板
template = DocxTemplate("template.docx")

# 准备数据列表
data_list = [
    {'name': '张三', 'age': 25, 'city': '北京'},
    {'name': '李四', 'age': 30, 'city': '上海'},
    {'name': '王五', 'age': 28, 'city': '广州'}
]

# 批量生成文档
for i, data in enumerate(data_list):
    context = {'person': data}
    template.render(context)
    template.save(f"output_{i+1}.docx")
    print(f"已生成：output_{i+1}.docx")
```

---

## 第三部分：网络编程

### 3.1 Socket 编程基础

```python
import socket

# 创建 TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取主机名
hostname = socket.gethostname()
print(f"主机名：{hostname}")

# 获取 IP 地址
ip_address = socket.gethostbyname(hostname)
print(f"IP 地址：{ip_address}")

# 关闭 socket
sock.close()
```

### 3.2 TCP 服务器

```python
import socket

# 创建 socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址和端口
server_socket.bind(('localhost', 8888))

# 开始监听
server_socket.listen(5)
print("服务器启动，等待连接...")

while True:
    # 接受连接
    client_socket, address = server_socket.accept()
    print(f"连接来自：{address}")

    # 接收数据
    data = client_socket.recv(1024).decode('utf-8')
    print(f"收到消息：{data}")

    # 发送响应
    response = f"服务器回复：{data}"
    client_socket.send(response.encode('utf-8'))

    # 关闭连接
    client_socket.close()
```

### 3.3 TCP 客户端

```python
import socket

# 创建 socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
client_socket.connect(('localhost', 8888))

# 发送数据
message = "Hello, Server!"
client_socket.send(message.encode('utf-8'))

# 接收响应
response = client_socket.recv(1024).decode('utf-8')
print(f"收到响应：{response}")

# 关闭连接
client_socket.close()
```

### 3.4 HTTP 服务器

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 发送响应头
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # 发送响应体
        response = """
        <html>
        <body>
            <h1>Hello, HTTP Server!</h1>
            <p>这是一个简单的 HTTP 服务器</p>
        </body>
        </html>
        """
        self.wfile.write(response.encode('utf-8'))

# 创建服务器
server = HTTPServer(('localhost', 8000), MyHTTPRequestHandler)
print("HTTP 服务器运行在 http://localhost:8000")
server.serve_forever()
```

### 3.5 URL 解析

```python
from urllib.parse import urlparse, parse_qs, urljoin

# 解析 URL
url = 'https://www.example.com/path?name=张三&age=25#section'
parsed = urlparse(url)
print(f"协议：{parsed.scheme}")
print(f"域名：{parsed.netloc}")
print(f"路径：{parsed.path}")
print(f"查询参数：{parsed.query}")
print(f"片段：{parsed.fragment}")

# 解析查询参数
query = parse_qs(parsed.query)
print(f"查询参数：{query}")

# 拼接 URL
base_url = 'https://www.example.com/'
relative_url = 'path/to/resource'
full_url = urljoin(base_url, relative_url)
print(f"完整 URL: {full_url}")
```

---

## 第四部分：爬虫技术

### 4.1 Requests + BeautifulSoup

**安装**

```bash
pip install requests beautifulsoup4 lxml
```

**基本使用**

```python
import requests
from bs4 import BeautifulSoup

# 获取页面
r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html = r.text

# 解析
soup = BeautifulSoup(html, "lxml")

# 选择器
soup.select("div.content")      # CSS 选择器
soup.find_all("a", class_="link")
soup.find("title").text
```

**实际爬虫示例**

```python
import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # 查找所有名言
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').string
        author = quote.find('small', class_='author').string
        tags = [tag.string for tag in quote.find_all('a', class_='tag')]

        print(f"名言：{text}")
        print(f"作者：{author}")
        print(f"标签：{', '.join(tags)}")
        print("-" * 50)

scrape_quotes()
```

### 4.2 Selenium - 动态页面爬取

**安装**

```bash
pip install selenium
```

**基本使用**

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 创建浏览器驱动（Selenium 4.6+ 推荐方式，自动管理驱动）
service = Service()
driver = webdriver.Chrome(service=service)

try:
    # 打开网页
    driver.get('https://www.baidu.com')

    # 查找元素
    search_box = driver.find_element(By.ID, 'kw')

    # 输入搜索内容
    search_box.send_keys('Python 爬虫')

    # 提交搜索
    search_box.send_keys(Keys.RETURN)

    # 等待页面加载
    time.sleep(2)

    # 获取搜索结果
    results = driver.find_elements(By.CSS_SELECTOR, '.result')
    for result in results[:5]:
        print(result.text)

finally:
    # 关闭浏览器
    driver.quit()
```

**元素定位**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service()
driver = webdriver.Chrome(service=service)
driver.get('https://example.com')

# 通过 ID
element = driver.find_element(By.ID, 'element_id')

# 通过 Name
element = driver.find_element(By.NAME, 'element_name')

# 通过 Class Name
element = driver.find_element(By.CLASS_NAME, 'element_class')

# 通过 CSS Selector
element = driver.find_element(By.CSS_SELECTOR, '.class > div')

# 通过 XPath
element = driver.find_element(By.XPATH, '//div[@class="example"]')

driver.quit()
```

**无头模式**

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 配置无头模式
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://example.com')
print(driver.title)
driver.quit()
```

### 4.3 Playwright - 现代方案

**安装**

```bash
pip install playwright
playwright install  # 安装浏览器驱动
```

**基本使用**

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 启动浏览器
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 访问网页
    page.goto('https://example.com')

    # 获取标题
    print(f"标题：{page.title()}")

    # 截图
    page.screenshot(path='example.png')

    # 关闭浏览器
    browser.close()
```

**元素定位和操作**

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://example.com')

    # 点击元素
    page.click('button#submit')

    # 输入文本
    page.fill('input#username', '张三')

    # 获取文本
    text = page.text_content('div.content')

    # 获取属性
    href = page.get_attribute('a.link', 'href')

    # 等待元素
    page.wait_for_selector('.dynamic-content')

    # 等待导航
    page.wait_for_load_state('networkidle')

    # 执行 JavaScript
    result = page.evaluate('() => document.title')

    browser.close()
```

**表单操作**

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://example.com/login')

    # 填写表单
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'password123')

    # 选择下拉框
    page.select_option('select#country', 'China')

    # 勾选复选框
    page.check('input[type="checkbox"]')

    # 点击单选按钮
    page.click('input[type="radio"][value="male"]')

    # 提交表单
    page.click('button[type="submit"]')

    # 等待跳转
    page.wait_for_url('**/dashboard')

    browser.close()
```

---

## 第五部分：数据分析

### 5.1 NumPy - 科学计算基础

**安装**

```bash
pip install numpy
```

**创建数组**

```python
import numpy as np

# 从列表创建数组
arr = np.array([1, 2, 3, 4, 5])
print(f"一维数组：{arr}")

# 创建二维数组
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"二维数组:\n{matrix}")

# 创建特定数组
zeros = np.zeros((3, 3))      # 全零数组
ones = np.ones((2, 4))        # 全一数组
random = np.random.rand(3, 3) # 随机数组
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

print(f"全零数组:\n{zeros}")
print(f"全一数组:\n{ones}")
print(f"随机数组:\n{random}")
print(f"范围数组：{range_arr}")
```

**数组属性**

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(f"形状：{arr.shape}")      # (2, 3)
print(f"维度：{arr.ndim}")       # 2
print(f"大小：{arr.size}")       # 6
print(f"数据类型：{arr.dtype}")  # int64
print(f"元素大小：{arr.itemsize} 字节")
```

**数组运算**

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# 基本运算
print(f"加法：{arr1 + arr2}")      # [ 6  8 10 12]
print(f"减法：{arr1 - arr2}")      # [-4 -4 -4 -4]
print(f"乘法：{arr1 * arr2}")      # [ 5 12 21 32]
print(f"除法：{arr1 / arr2}")      # [0.2 0.333 0.428 0.5]

# 标量运算
print(f"乘以 2: {arr1 * 2}")        # [2 4 6 8]
print(f"加 10: {arr1 + 10}")        # [11 12 13 14]

# 数学函数
print(f"平方：{np.square(arr1)}")  # [ 1  4  9 16]
print(f"平方根：{np.sqrt(arr1)}")  # [1. 1.414 1.732 2.]
print(f"指数：{np.exp(arr1)}")     # [ 2.718  7.389 20.085 54.598]

# 统计函数
print(f"求和：{np.sum(arr1)}")     # 10
print(f"平均值：{np.mean(arr1)}")  # 2.5
print(f"最大值：{np.max(arr1)}")   # 4
print(f"最小值：{np.min(arr1)}")   # 1
print(f"标准差：{np.std(arr1)}")   # 1.118
```

> 💡 **提示**：NumPy 数组比 Python 列表快得多，特别是在处理大量数据时。

### 5.2 Pandas - 数据分析核心

**安装**

```bash
pip install pandas
```

**创建 DataFrame**

```python
import pandas as pd

# 从字典创建
data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 35],
    '城市': ['北京', '上海', '广州']
}
df = pd.DataFrame(data)
print(df)

# 从列表创建
data = [
    ['张三', 25, '北京'],
    ['李四', 30, '上海'],
    ['王五', 35, '广州']
]
df = pd.DataFrame(data, columns=['姓名', '年龄', '城市'])
print(df)
```

**读取和写入数据**

```python
import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('data.csv')

# 读取 Excel 文件
df = pd.read_excel('data.xlsx')

# 读取 JSON 文件
df = pd.read_json('data.json')

# 写入 CSV 文件
df.to_csv('output.csv', index=False, encoding='utf-8')

# 写入 Excel 文件
df.to_excel('output.xlsx', index=False)

# 写入 JSON 文件
df.to_json('output.json', force_ascii=False, indent=2)
```

**数据查看**

```python
import pandas as pd

# 假设 df 是一个 DataFrame
print(f"前 5 行:\n{df.head()}")
print(f"后 5 行:\n{df.tail()}")
print(f"基本信息:\n{df.info()}")
print(f"统计信息:\n{df.describe()}")
print(f"列名：{df.columns.tolist()}")
print(f"形状：{df.shape}")
print(f"数据类型:\n{df.dtypes}")
```

**数据选择**

```python
import pandas as pd

# 选择列
print(df['姓名'])        # 单列
print(df[['姓名', '年龄']])  # 多列

# 选择行（位置索引）
print(df.iloc[0])       # 第一行
print(df.iloc[0:3])     # 前三行

# 选择行（标签索引）
print(df.loc[0])        # 第一行
print(df.loc[0:2])      # 前三行

# 条件选择
print(df[df['年龄'] > 25])      # 年龄大于 25 的行
print(df[df['城市'] == '北京']) # 城市为北京的行

# 组合条件
print(df[(df['年龄'] > 25) & (df['城市'] == '上海')])
```

**数据操作**

```python
import pandas as pd

# 添加列
df['工资'] = [8000, 10000, 12000]

# 删除列
df = df.drop('工资', axis=1)

# 重命名列
df = df.rename(columns={'姓名': 'name', '年龄': 'age'})

# 排序
df_sorted = df.sort_values('年龄', ascending=False)

# 去重
df_unique = df.drop_duplicates()

# 填充缺失值
df_filled = df.fillna(0)

# 删除缺失值
df_clean = df.dropna()
```

**数据聚合**

```python
import pandas as pd

# 按列分组
grouped = df.groupby('城市')
print(f"各城市平均年龄:\n{grouped['年龄'].mean()}")

# 多种聚合
result = df.groupby('城市').agg({
    '年龄': ['mean', 'max', 'min'],
    '工资': 'sum'
})
print(result)

# 计数
count = df['城市'].value_counts()
print(f"城市人数:\n{count}")
```

> 💡 **提示**：Pandas 是数据分析和数据科学的基础库，建议深入学习。

### 5.3 Matplotlib - 数据可视化

**安装**

```bash
pip install matplotlib
```

**基本折线图**

```python
import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 创建图表
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='blue', label='数据')

# 添加标题和标签
plt.title('折线图示例', fontsize=16)
plt.xlabel('X 轴', fontsize=12)
plt.ylabel('Y 轴', fontsize=12)

# 添加网格
plt.grid(True, linestyle='--', alpha=0.6)

# 显示图例
plt.legend()

# 显示图表
plt.show()
```

**柱状图**

```python
import matplotlib.pyplot as plt

# 数据
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

# 创建柱状图
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='skyblue', edgecolor='black')

# 添加标题和标签
plt.title('柱状图示例', fontsize=16)
plt.xlabel('类别', fontsize=12)
plt.ylabel('数值', fontsize=12)

# 在柱子上显示数值
for i, v in enumerate(values):
    plt.text(i, v + 1, str(v), ha='center', va='bottom')

plt.show()
```

**散点图**

```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
np.random.seed(42)
x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)

# 创建散点图
plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')

# 添加标题和标签
plt.title('散点图示例', fontsize=16)
plt.xlabel('X 轴', fontsize=12)
plt.ylabel('Y 轴', fontsize=12)

# 添加颜色条
plt.colorbar(label='颜色')

plt.show()
```

**饼图**

```python
import matplotlib.pyplot as plt

# 数据
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
explode = (0, 0.1, 0, 0)  # 突出显示第二块

# 创建饼图
plt.figure(figsize=(10, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.title('饼图示例', fontsize=16)
plt.axis('equal')  # 使饼图为圆形

plt.show()
```

**子图**

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建 2x2 子图
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 子图 1: 折线图
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x), color='blue')
axes[0, 0].set_title('正弦波')
axes[0, 0].grid(True)

# 子图 2: 柱状图
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
axes[0, 1].bar(categories, values, color='orange')
axes[0, 1].set_title('柱状图')

# 子图 3: 散点图
x = np.random.randn(50)
y = np.random.randn(50)
axes[1, 0].scatter(x, y, color='green', alpha=0.6)
axes[1, 0].set_title('散点图')

# 子图 4: 饼图
sizes = [30, 20, 25, 25]
axes[1, 1].pie(sizes, labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')
axes[1, 1].set_title('饼图')

plt.tight_layout()
plt.show()
```

**保存图表**

```python
import matplotlib.pyplot as plt

# 创建图表
plt.figure(figsize=(10, 6))
plt.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
plt.title('保存图表示例')

# 保存为不同格式
plt.savefig('chart.png', dpi=300, bbox_inches='tight')  # PNG
plt.savefig('chart.jpg', quality=95)  # JPG
plt.savefig('chart.pdf')  # PDF
plt.savefig('chart.svg')  # SVG

plt.close()
```

> 💡 **提示**：Matplotlib 功能强大，可以创建几乎所有类型的图表，建议结合 Pandas 使用进行数据可视化。

---

## 第六部分：AI 与机器学习

### 6.1 PyTorch - 深度学习框架

**安装**

```bash
# CPU 版本
pip install torch

# GPU 版本 (CUDA 12.4)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

**张量基础**

```python
import torch

# 创建张量
x = torch.tensor([1, 2, 3, 4, 5])
print(f"一维张量：{x}")

# 创建二维张量
matrix = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(f"二维张量:\n{matrix}")

# 创建特定张量
zeros = torch.zeros(3, 3)           # 全零
ones = torch.ones(2, 4)             # 全一
random = torch.rand(3, 3)           # 随机
eye = torch.eye(3)                  # 单位矩阵
arange = torch.arange(0, 10, 2)     # [0, 2, 4, 6, 8]

print(f"形状：{matrix.shape}")
print(f"数据类型：{matrix.dtype}")
print(f"设备：{matrix.device}")
```

**自动求导**

```python
import torch

# 创建需要梯度的张量
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2 + 3 * x + 1

# 反向传播
y.backward()

print(f"x 的梯度：{x.grad}")  # dy/dx = 2x + 3 = 7

# 多变量求导
x = torch.randn(3, requires_grad=True)
y = x * 2
z = y.sum()
z.backward()

print(f"梯度：{x.grad}")
```

**构建神经网络**

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x

# 创建模型
model = NeuralNetwork(input_size=784, hidden_size=128, output_size=10)
print(model)
```

**训练循环**

```python
import torch
import torch.nn as nn
import torch.optim as optim

# 假设已有数据和模型
X_train = torch.randn(1000, 784)
y_train = torch.randint(0, 10, (1000,))

model = NeuralNetwork(784, 128, 10)

# 损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练循环
num_epochs = 10
batch_size = 32

for epoch in range(num_epochs):
    model.train()
    total_loss = 0

    for i in range(0, len(X_train), batch_size):
        # 获取批次数据
        X_batch = X_train[i:i+batch_size]
        y_batch = y_train[i:i+batch_size]

        # 前向传播
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)

        # 反向传播
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss:.4f}")
```

**使用 GPU 加速**

```python
import torch

# 检查 GPU 可用性
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"使用设备：{device}")

# 将模型和数据移动到 GPU
model = NeuralNetwork(784, 128, 10).to(device)
X_train = X_train.to(device)
y_train = y_train.to(device)

# 后续训练会自动在 GPU 上进行
```

**保存和加载模型**

```python
# 保存模型参数（推荐方式）
torch.save(model.state_dict(), 'model.pth')

# 加载模型参数（PyTorch 2.0+ 推荐 weights_only=True）
model = NeuralNetwork(784, 128, 10)
model.load_state_dict(torch.load('model.pth', weights_only=True))
model.eval()

# 使用 safetensors 格式保存（更安全）
from safetensors.torch import save_file, load_file
save_file(model.state_dict(), 'model.safetensors')

# 加载 safetensors 格式
state_dict = load_file('model.safetensors')
model.load_state_dict(state_dict)
```

> 💡 **提示**：PyTorch 的动态计算图让调试更简单，非常适合研究和快速原型开发。

### 6.2 Scikit-learn - 机器学习库

**安装**

```bash
pip install scikit-learn
```

**数据预处理**

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np

# 生成示例数据
X = np.random.randn(100, 5)
y = np.random.randint(0, 2, 100)

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 归一化
minmax = MinMaxScaler()
X_normalized = minmax.fit_transform(X)

# 划分训练测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"训练集大小：{len(X_train)}, 测试集大小：{len(X_test)}")
```

**分类算法**

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 加载数据
iris = load_iris()
X, y = iris.data, iris.target

# 划分数据
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 随机森林
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
print(f"随机森林准确率：{accuracy_score(y_test, rf_pred):.4f}")

# SVM
svm = SVC(kernel='rbf', random_state=42)
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)
print(f"SVM 准确率：{accuracy_score(y_test, svm_pred):.4f}")

# 逻辑回归
lr = LogisticRegression(random_state=42)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
print(f"逻辑回归准确率：{accuracy_score(y_test, lr_pred):.4f}")

# 详细评估
print(classification_report(y_test, rf_pred))
```

**回归算法**

```python
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 加载加州房价数据集
california = fetch_california_housing()
X, y = california.data, california.target

print(f"数据集大小：{X.shape[0]} 个样本，{X.shape[1]} 个特征")

# 划分数据
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 线性回归
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
print(f"线性回归 R²: {r2_score(y_test, lr_pred):.4f}")

# 岭回归
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
ridge_pred = ridge.predict(X_test)
print(f"岭回归 R²: {r2_score(y_test, ridge_pred):.4f}")

# 梯度提升
gbr = GradientBoostingRegressor(n_estimators=100, random_state=42)
gbr.fit(X_train, y_train)
gbr_pred = gbr.predict(X_test)
print(f"梯度提升 R²: {r2_score(y_test, gbr_pred):.4f}")
```

**聚类算法**

```python
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score

# 生成聚类数据
X, y_true = make_blobs(n_samples=300, centers=4,
                        cluster_std=0.60, random_state=0)

# K-Means 聚类
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans_labels = kmeans.fit_predict(X)
kmeans_score = silhouette_score(X, kmeans_labels)
print(f"K-Means 轮廓分数：{kmeans_score:.4f}")

# DBSCAN 聚类
dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan_labels = dbscan.fit_predict(X)
dbscan_score = silhouette_score(X, dbscan_labels)
print(f"DBSCAN 轮廓分数：{dbscan_score:.4f}")
```

**模型选择与调参**

```python
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier

# 参数网格
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

# 网格搜索
grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print(f"最佳参数：{grid_search.best_params_}")
print(f"最佳交叉验证分数：{grid_search.best_score_:.4f}")

# 交叉验证
cv_scores = cross_val_score(grid_search.best_estimator_,
                            X_train, y_train, cv=10)
print(f"10 折交叉验证平均分：{cv_scores.mean():.4f}")
```

> 💡 **提示**：Scikit-learn API 设计统一，所有模型都遵循 fit/predict 模式，易于学习和使用。

### 6.3 Transformers - 大语言模型库

**安装**

```bash
pip install transformers
pip install torch  # PyTorch 后端
```

**文本分类（情感分析）**

```python
from transformers import pipeline

# 使用预训练管道
classifier = pipeline("sentiment-analysis")

# 情感分析
result = classifier("I love using Transformers library!")
print(f"情感：{result[0]['label']}")
print(f"置信度：{result[0]['score']:.4f}")

# 多文本
texts = [
    "This is amazing!",
    "I hate this.",
    "It's okay, nothing special."
]
results = classifier(texts)
for text, result in zip(texts, results):
    print(f"'{text}' -> {result['label']} ({result['score']:.4f})")
```

**文本生成**

```python
from transformers import pipeline

# 文本生成管道
generator = pipeline("text-generation", model="gpt2")

# 生成文本
prompt = "Once upon a time"
result = generator(prompt, max_length=50, num_return_sequences=3)

for i, r in enumerate(result):
    print(f"\n生成文本 {i+1}:")
    print(r['generated_text'])
```

**问答系统**

```python
from transformers import pipeline

# 问答管道
qa_pipeline = pipeline("question-answering")

context = """
Python 是一种高级编程语言，由 Guido van Rossum 于 1991 年创建。
Python 设计哲学强调代码可读性，使用缩进来表示代码块。
Python 支持多种编程范式，包括面向对象、函数式和过程式编程。
"""

question = "Python 是谁创建的？"
result = qa_pipeline(question=question, context=context)

print(f"答案：{result['answer']}")
print(f"置信度：{result['score']:.4f}")
```

**使用 Auto 类加载模型**

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 模型名称
model_name = "bert-base-chinese"

# 加载分词器和模型
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 准备输入
text = "这是一个测试句子"
inputs = tokenizer(text, return_tensors="pt",
                   padding=True, truncation=True)

# 模型推理
with torch.no_grad():
    outputs = model(**inputs)

print(f"输出形状：{outputs.logits.shape}")
```

**中文文本处理**

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# 使用中文预训练模型
model_name = "hfl/chinese-roberta-wwm-ext"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 中文文本
texts = [
    "这部电影非常好看，剧情精彩",
    "服务太差了，不会再来了",
    "产品质量一般，价格偏高"
]

# 批量编码
inputs = tokenizer(texts, padding=True, truncation=True,
                   return_tensors="pt", max_length=128)

print(f"输入形状：{inputs['input_ids'].shape}")
print(f"分词结果：{tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])}")
```

> 💡 **提示**：Hugging Face Model Hub 提供了超过 10 万个预训练模型，可以直接使用或微调。

### 6.4 Keras 3.x - 高级神经网络 API

**安装**

```bash
# 方式 1：安装独立的 Keras 3（推荐）
pip install keras

# 方式 2：使用 TensorFlow 集成的 Keras
pip install tensorflow
```

**基本神经网络模型**

```python
import keras
from keras import layers

# 创建序列模型（Keras 3 API）
model = keras.Sequential([
    layers.Input(shape=(10,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# 编译模型
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()
```

**训练模型**

```python
import keras
from keras.datasets import mnist

# 加载数据
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

# 创建并训练模型
model = keras.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
```

**Keras 3 主要特性**

- 🔄 **多后端支持**：可切换 TensorFlow、PyTorch 或 JAX 后端
- 🚀 **性能优化**：自动启用 XLA 加速
- 🎯 **原生支持**：支持原生 TensorFlow、PyTorch 和 JAX 工作流
- 📦 **向后兼容**：完全兼容 Keras 2.x API

### 6.5 OpenCV - 计算机视觉

**安装**

```bash
pip install opencv-python
pip install opencv-python-headless  # 无 GUI 版本 (服务器)
```

**读取和显示图像**

```python
import cv2

# 读取图像
img = cv2.imread('image.jpg')

# 检查是否成功
if img is None:
    print("无法读取图像")
else:
    print(f"图像形状：{img.shape}")  # (高度，宽度，通道数)

    # 显示图像
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 保存图像
    cv2.imwrite('output.jpg', img)
```

**图像预处理**

```python
import cv2

# 读取图像
img = cv2.imread('image.jpg')

# 转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 高斯模糊
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# 边缘检测
edges = cv2.Canny(img, 100, 200)

# 显示结果
cv2.imshow('Original', img)
cv2.imshow('Gray', gray)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 第七部分：包管理工具

### 7.1 包管理工具对比

| 工具 | 发布时间 | 语言 | 主要用途 | 依赖锁定 | 虚拟环境 |
|------|----------|------|----------|----------|----------|
| **pip** | 2008 | Python | 包安装 | ❌ (需 requirements.txt) | ❌ (需配合 venv) |
| **pipx** | 2019 | Python | 应用隔离 | ✅ 自动 | ✅ 自动 |
| **Poetry** | 2018 | Python | 项目管理 | ✅ poetry.lock | ✅ 自动 |
| **Pipenv** | 2017 | Python | 项目管理 | ✅ Pipfile.lock | ✅ 自动 |
| **Conda** | 2012 | Python/C | 科学计算 | ✅ environment.yml | ✅ 自动 |
| **uv** | 2024 | Rust | 全能管理 | ✅ uv.lock | ✅ 自动 |

### 7.2 pip - 官方标配

```bash
# 安装包
pip install package_name

# 安装指定版本
pip install package_name==1.2.3

# 安装 requirements.txt
pip install -r requirements.txt

# 卸载包
pip uninstall package_name

# 列出已安装包
pip list

# 查看过时包
pip list --outdated

# 升级包
pip install --upgrade package_name

# 导出已安装包
pip freeze > requirements.txt
```

**pip 最佳实践**

```bash
# 1. 永远使用虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 2. 升级 pip 到最新版
python -m pip install --upgrade pip

# 3. 使用 requirements.txt 锁定依赖
pip freeze > requirements.txt
```

### 7.3 uv - 2026 首选（比 pip 快 100 倍）

```bash
# 安装
pip install uv

# 常用命令
uv pip install requests
uv venv .venv           # 创建虚拟环境
uv sync                  # 同步依赖
uv add requests          # 添加依赖
```

### 7.4 Poetry - 项目依赖管理

```bash
pip install poetry
poetry init
poetry add requests
poetry install
poetry lock
```

### 7.5 Pipenv - Pip + Virtualenv

```bash
pip install pipenv
pipenv install requests
pipenv shell
pipenv run python script.py
```

### 7.6 选择建议

```
开始选择
    ↓
安装 Python 应用？
    ↓ 是 → 使用 pipx
    ↓ 否
科学计算/多语言？
    ↓ 是 → 使用 Conda
    ↓ 否
需要最快速度？
    ↓ 是 → 使用 uv (推荐)
    ↓ 否
成熟稳定优先？
    ↓ 是 → 使用 Poetry
    ↓ 否
使用 pip + venv
```

---

## 第八部分：数据存储

### 8.1 SQLAlchemy - Python ORM 标准

**安装**

```bash
pip install sqlalchemy pymysql  # MySQL
```

**基本用法**

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 创建引擎
engine = create_engine("sqlite:///app.db")
Session = sessionmaker(bind=engine)
session = Session()

# ORM 方式
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# 创建表
Base.metadata.create_all(engine)

# 增删改查
user = User(name="张三")
session.add(user)
session.commit()

# 查询
users = session.query(User).filter_by(name="张三").all()
```

**ORM 模式（对象关系映射）**

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 创建基类
Base = declarative_base()

# 定义模型
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"

# 创建引擎和会话
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# 创建（插入）
user1 = User(name='王五', age=28)
user2 = User(name='赵六', age=32)
session.add(user1)
session.add(user2)
session.commit()

# 读取（查询）
all_users = session.query(User).all()
for user in all_users:
    print(user)

# 条件查询
user = session.query(User).filter_by(name='王五').first()
print(f"找到用户：{user}")

# 更新
user = session.query(User).filter_by(name='王五').first()
user.age = 29
session.commit()

# 删除
user = session.query(User).filter_by(name='赵六').first()
session.delete(user)
session.commit()

# 关闭会话
session.close()
```

**关系映射**

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    # 一对多关系
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author_id = Column(Integer, ForeignKey('authors.id'))

    # 多对一关系
    author = relationship("Author", back_populates="books")

# 创建表
engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# 创建作者和书籍
author = Author(name='鲁迅')
book1 = Book(title='狂人日记', author=author)
book2 = Book(title='阿 Q 正传', author=author)

session.add(author)
session.commit()

# 查询作者及其书籍
author = session.query(Author).filter_by(name='鲁迅').first()
print(f"作者：{author.name}")
print(f"书籍：{[book.title for book in author.books]}")

session.close()
```

### 8.2 MySQL

**安装驱动**

```bash
# 方法 1：使用 PyMySQL
pip install pymysql

# 方法 2：使用 mysql-connector-python（官方驱动）
pip install mysql-connector-python
```

**使用 PyMySQL**

```python
import pymysql

# 创建连接
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='test_db',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # 创建表
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE,
            age INT
        )
        """
        cursor.execute(sql)
        connection.commit()

        # 插入数据
        sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
        cursor.execute(sql, ('张三', 'zhangsan@example.com', 25))
        cursor.execute(sql, ('李四', 'lisi@example.com', 30))
        connection.commit()

        # 查询数据
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 更新数据
        sql = "UPDATE users SET age = %s WHERE name = %s"
        cursor.execute(sql, (26, '张三'))
        connection.commit()

        # 删除数据
        sql = "DELETE FROM users WHERE name = %s"
        cursor.execute(sql, ('李四',))
        connection.commit()

finally:
    connection.close()
```

---

## 第九部分：系统运维

### 9.1 装饰器

**简单的装饰器**

```python
# 装饰器本质：闭包
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"耗时：{time.time() - start:.2f}s")
        return result
    return wrapper

@timer
def slow_func():
    import time
    time.sleep(1)
    return "done"

slow_func()
```

**带参数的装饰器**

```python
def retry(times=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    continue
            return None
        return wrapper
    return decorator

@retry(times=5)
def fetch():
    pass
```

### 9.2 异步编程

```python
import asyncio

async def main():
    # 并发任务
    results = await asyncio.gather(
        asyncio.sleep(1, result="a"),
        asyncio.sleep(1, result="b")
    )
    print(results)  # ['a', 'b']

asyncio.run(main())
```

### 9.3 上下文管理器

```python
# 类方式
class File:
    def __enter__(self):
        self.f = open("file.txt")
        return self.f
    def __exit__(self, *args):
        self.f.close()

# with 使用
with File() as f:
    f.read()

# 或用 contextlib
from contextlib import contextmanager
@contextmanager
def timer():
    import time
    start = time.time()
    yield
    print(f"耗时：{time.time() - start:.2f}")
```

### 9.4 列表推导式

```python
# 传统方式
squares = []
for i in range(10):
    squares.append(i ** 2)

# 列表推导式
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 带条件的列表推导式
even_numbers = [i for i in range(20) if i % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 嵌套列表推导式
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

### 9.5 生成器

```python
# 生成器函数
def fibonacci(n):
    """生成斐波那契数列"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 使用生成器
for num in fibonacci(10):
    print(num, end=' ')  # 0 1 1 2 3 5 8 13 21 34

# 生成器表达式
squares_gen = (i ** 2 for i in range(5))
print(list(squares_gen))  # [0, 1, 4, 9, 16]
```

---

## 第十部分：学习路线与建议

### 10.1 Python 知识体系

```
基础语法 → 数据结构 → 函数&面向对象 → 模块&包 → 实战技能 → Web/数据/AI
```

### 10.2 学习路径建议

**第一阶段：基础入门（1-2 周）**
- 安装 Python 和开发环境
- 掌握基础语法、变量、数据类型
- 理解控制流（if/for/while）
- 学习函数定义和调用

**第二阶段：进阶提升（2-4 周）**
- 面向对象编程（类、继承、多态）
- 文件操作和异常处理
- 常用内置模块（os、pathlib、json）
- 列表推导式、生成器、装饰器

**第三阶段：方向选择（4-8 周）**
- **Web 开发**：FastAPI/Flask、数据库、REST API
- **数据分析**：NumPy、Pandas、Matplotlib
- **爬虫**：Requests、BeautifulSoup、Selenium
- **人工智能**：PyTorch、Keras、Transformers

**第四阶段：实战项目（持续）**
- 选择感兴趣的方向做完整项目
- 阅读优秀开源代码
- 参与开源社区贡献
- 持续学习新技术

### 10.3 2026 年新增内容

- 🐍 **Python 3.14**：新特性和最佳实践
- 🧠 **Keras 3.x**：完整教程，支持多后端
- 📘 **Scikit-learn**：机器学习完整教程
- ⚡ **uv 包管理器**：新一代快速包管理器，速度提升 100 倍
- 📦 **包管理工具对比**：7 种包管理工具详细对比

### 10.4 推荐学习资源

- **官方文档**：docs.python.org - 最权威的资料
- **PyPI**：pypi.org - 查找第三方库
- **GitHub**：关注优秀 Python 项目
- **Stack Overflow**：解决问题的好去处
- **Real Python**：高质量教程网站
- **Python Cookbook**：实用代码片段集合

---

## 结语

Python 是一门"优雅而明确"的编程语言，它的简洁语法和强大生态让开发者能够快速实现想法。无论你是想：

- 🔹 入门编程世界
- 🔹 转行成为专业开发者
- 🔹 提升工作效率
- 🔹 探索人工智能

Python 都是你的不二之选。

**记住 Python 之禅**：

```python
import this
```

> Beautiful is better than ugly.
> Explicit is better than implicit.
> Simple is better than complex.
> Complex is better than complicated.
> Readability counts.

愿你在 Python 的学习之路上越走越远，用代码创造美好！🐍

---

*本文基于 Python 3.14 编写，部分特性可能需要 Python 3.10+ 版本支持。*

*参考资料：Python 官方文档、Real Python、各库官方文档*

*2026 年 3 月更新*
