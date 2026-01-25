#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从分类HTML文件中提取知识点并创建单独的HTML文件
"""

import re
from pathlib import Path

# 定义每个文件的section映射
TOPICS_MAP = {
    '01-basic.html': [
        ('intro', '简介'),
        ('installation', '安装'),
        ('basics', '基础语法'),
        ('variables', '变量'),
        ('datatypes', '数据类型'),
        ('controlflow', '控制流'),
        ('functions', '函数'),
        ('oop', '面向对象'),
        ('stringformat', '字符串格式化'),
        ('tips', '常用技巧')
    ],
    '02-file.html': [
        ('fileio', '文件操作'),
        ('directory', '目录操作'),
        ('exceptions', '异常处理'),
        ('pypdf2', 'PyPDF2'),
        ('pythondocx', 'python-docx'),
        ('docxtpl', 'docxtpl'),
        ('openpyxl', 'openpyxl'),
        ('pythonpptx', 'python-pptx'),
        ('difflib', 'difflib'),
        ('filecmp', 'filecmp')
    ],
    '03-network.html': [
        ('network', '网络编程'),
        ('asyncio', '异步编程'),
        ('requests', 'Requests'),
        ('aiohttp', 'aiohttp'),
        ('fastapi', 'FastAPI'),
        ('scapy', 'Scapy')
    ],
    '04-crawler.html': [
        ('beautifulsoup', 'BeautifulSoup'),
        ('selenium', 'Selenium'),
        ('playwright', 'Playwright'),
        ('scrapy', 'Scrapy'),
        ('regex', '正则表达式')
    ],
    '05-data.html': [
        ('numpy', 'NumPy'),
        ('pandas', 'Pandas'),
        ('matplotlib', 'Matplotlib'),
        ('keras', 'Keras')
    ],
    '06-database.html': [
        ('sqlalchemy', 'SQLAlchemy'),
        ('mysql', 'MySQL'),
        ('mongodb', 'MongoDB'),
        ('redis', 'Redis')
    ],
    '07-devops.html': [
        ('advanced', '高级特性'),
        ('fabric', 'Fabric'),
        ('psutil', 'psutil'),
        ('logging', 'logging'),
        ('ansible', 'Ansible')
    ],
    '08-tools.html': [
        ('qrcode', 'QRCode'),
        ('resources', '学习资源')
    ]
}

def extract_section_content(html_file, section_id):
    """从HTML文件中提取指定section的内容"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用正则表达式查找section
    pattern = rf'<section id="{section_id}" class="content-section">(.*?)</section>'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        return f'<section id="{section_id}" class="content-section">{match.group(1)}</section>'
    return None

def create_topic_file(source_file, section_id, title, topics_map):
    """创建知识点文件"""
    # 提取section内容
    section_content = extract_section_content(source_file, section_id)
    if not section_content:
        print(f"警告: 未找到 section {section_id} 在 {source_file}")
        return

    # 获取文件编号
    file_num = source_file.split('-')[0]

    # 创建文件名
    filename = f"{file_num}-{section_id}.html"

    # 读取源文件获取header
    with open(source_file, 'r', encoding='utf-8') as f:
        full_content = f.read()

    # 提取header
    header_match = re.search(r'(<header>.*?</header>)', full_content, re.DOTALL)
    header_content = header_match.group(1) if header_match else ''

    # 创建简化的导航栏，只显示当前分类的链接
    nav_links = []
    current_topic_index = -1
    for i, (sid, stitle) in enumerate(topics_map):
        active_class = ' class="active"' if sid == section_id else ''
        nav_links.append(f'                <li><a href="{file_num}-{sid}.html"{active_class}>{stitle}</a></li>')
        if sid == section_id:
            current_topic_index = i

    # 添加上一个和下一个链接
    prev_next_links = []
    if current_topic_index > 0:
        prev_id, prev_title = topics_map[current_topic_index - 1]
        prev_next_links.append(f'<a href="{file_num}-{prev_id}.html">← {prev_title}</a>')
    if current_topic_index < len(topics_map) - 1:
        next_id, next_title = topics_map[current_topic_index + 1]
        prev_next_links.append(f'<a href="{file_num}-{next_id}.html">{next_title} →</a>')

    # 构建完整的HTML
    html_template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Python 入门教程</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>🐍 Python 入门教程</h1>
        <p>从零开始学习 Python 编程</p>
    </header>

    <nav>
        <div class="nav-category">
            <h3>📚 当前分类</h3>
            <ul>
{chr(10).join(nav_links)}
            </ul>
        </div>
    </nav>

    <main>
        <div class="topic-nav">
            {' | '.join(prev_next_links)}
        </div>

        {section_content}

        <div class="topic-nav">
            {' | '.join(prev_next_links)}
        </div>
    </main>

    <footer>
        <p>© 2026 Python 入门教程 | 祝你学习愉快！</p>
    </footer>
</body>
</html>'''

    # 写入文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"✓ 创建文件: {filename}")

def main():
    """主函数"""
    base_dir = Path('.')

    for source_file, topics in TOPICS_MAP.items():
        source_path = base_dir / source_file
        if not source_path.exists():
            print(f"警告: 文件不存在 {source_file}")
            continue

        print(f"\n处理文件: {source_file}")
        for section_id, title in topics:
            create_topic_file(str(source_path), section_id, title, topics)

    print("\n✓ 所有知识点文件创建完成！")

if __name__ == '__main__':
    main()