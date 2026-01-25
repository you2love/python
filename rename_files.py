#!/usr/bin/env python3
"""
重命名 python-tutorial 目录下的 HTML 文件，并更新所有文件中的链接。
"""

import os
import re

# 定义目录路径
BASE_DIR = '/Users/junjunyi/src-code/flearn/python-tutorial'

# 定义重命名映射
RENAME_MAPPING = {
    # 01-basic 分类文件
    '01-intro.html': 'introduction.html',
    '01-installation.html': 'installation.html',
    '01-basics.html': 'basics.html',
    '01-variables.html': 'variables.html',
    '01-datatypes.html': 'datatypes.html',
    '01-controlflow.html': 'control-flow.html',
    '01-functions.html': 'functions.html',
    '01-oop.html': 'oop.html',
    '01-stringformat.html': 'string-formatting.html',
    '01-tips.html': 'python-tips.html',

    # 02-file 分类文件
    '02-fileio.html': 'file-operations.html',
    '02-directory.html': 'directory-operations.html',
    '02-exceptions.html': 'exceptions.html',
    '02-pypdf2.html': 'pypdf2.html',
    '02-pythondocx.html': 'python-docx.html',
    '02-docxtpl.html': 'docxtpl.html',
    '02-openpyxl.html': 'openpyxl.html',
    '02-pythonpptx.html': 'python-pptx.html',
    '02-difflib.html': 'difflib.html',
    '02-filecmp.html': 'filecmp.html',

    # 03-network 分类文件
    '03-network.html': 'networking.html',
    '03-asyncio.html': 'asyncio.html',
    '03-requests.html': 'requests.html',
    '03-aiohttp.html': 'aiohttp.html',
    '03-fastapi.html': 'fastapi.html',
    '03-scapy.html': 'scapy.html',

    # 04-crawler 分类文件
    '04-beautifulsoup.html': 'beautifulsoup.html',
    '04-selenium.html': 'selenium.html',
    '04-playwright.html': 'playwright.html',
    '04-scrapy.html': 'scrapy.html',
    '04-regex.html': 'regex.html',

    # 05-data 分类文件
    '05-numpy.html': 'numpy.html',
    '05-pandas.html': 'pandas.html',
    '05-matplotlib.html': 'matplotlib.html',
    '05-keras.html': 'keras.html',

    # 06-database 分类文件
    '06-sqlalchemy.html': 'sqlalchemy.html',
    '06-mysql.html': 'mysql.html',
    '06-mongodb.html': 'mongodb.html',
    '06-redis.html': 'redis.html',

    # 07-devops 分类文件
    '07-advanced.html': 'advanced-features.html',
    '07-fabric.html': 'fabric.html',
    '07-psutil.html': 'psutil.html',
    '07-logging.html': 'logging.html',
    '07-ansible.html': 'ansible.html',

    # 08-tools 分类文件
    '08-qrcode.html': 'qrcode.html',
    '08-resources.html': 'resources.html',

    # 分类文件
    '01-basic.html': 'basics.html',
    '02-file.html': 'file-management.html',
    '03-network.html': 'network-programming.html',
    '04-crawler.html': 'web-scraping.html',
    '05-data.html': 'data-analysis.html',
    '06-database.html': 'databases.html',
    '07-devops.html': 'devops.html',
    '08-tools.html': 'tools.html',
}


def update_links_in_file(file_path, rename_mapping):
    """更新文件中的链接"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 替换所有旧文件名为新文件名
        for old_name, new_name in rename_mapping.items():
            # 替换 href 中的链接（包括带锚点的链接）
            content = re.sub(
                rf'href=["\']({re.escape(old_name)})(#[^"\']*)?["\']',
                lambda m: f'href="{new_name}{m.group(2) if m.group(2) else ""}"',
                content
            )
            # 替换 src 中的链接
            content = re.sub(
                rf'src=["\']({re.escape(old_name)})["\']',
                f'src="{new_name}"',
                content
            )
            # 替换纯文本中的链接
            content = re.sub(
                rf'(?<!["\'>=])({re.escape(old_name)})(?=["\'<\s])',
                new_name,
                content
            )

        # 如果内容有变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, len([old for old, new in rename_mapping.items() if old in original_content])

        return False, 0

    except Exception as e:
        print(f"  错误: {e}")
        return False, 0


def main():
    print("=" * 80)
    print("开始重命名 HTML 文件...")
    print("=" * 80)

    # 获取所有 HTML 文件
    html_files = [f for f in os.listdir(BASE_DIR) if f.endswith('.html')]

    print(f"\n找到 {len(html_files)} 个 HTML 文件\n")

    # 第一步：重命名文件
    print("步骤 1: 重命名文件")
    print("-" * 80)
    renamed_count = 0
    for old_name, new_name in RENAME_MAPPING.items():
        old_path = os.path.join(BASE_DIR, old_name)
        new_path = os.path.join(BASE_DIR, new_name)

        if os.path.exists(old_path):
            try:
                os.rename(old_path, new_path)
                print(f"✓ {old_name} → {new_name}")
                renamed_count += 1
            except Exception as e:
                print(f"✗ {old_name} → {new_name} (错误: {e})")
        else:
            print(f"- {old_name} (文件不存在)")

    print(f"\n共重命名 {renamed_count} 个文件\n")

    # 第二步：更新所有 HTML 文件中的链接
    print("步骤 2: 更新文件中的链接")
    print("-" * 80)

    # 获取更新后的文件列表
    updated_html_files = [f for f in os.listdir(BASE_DIR) if f.endswith('.html')]

    updated_files_count = 0
    total_links_updated = 0

    for html_file in updated_html_files:
        file_path = os.path.join(BASE_DIR, html_file)
        updated, links_count = update_links_in_file(file_path, RENAME_MAPPING)

        if updated:
            print(f"✓ {html_file} (更新了 {links_count} 个链接)")
            updated_files_count += 1
            total_links_updated += links_count

    print(f"\n共更新 {updated_files_count} 个文件中的 {total_links_updated} 个链接\n")

    # 第三步：验证结果
    print("步骤 3: 验证结果")
    print("-" * 80)

    # 检查是否所有旧文件都已不存在
    missing_old_files = []
    for old_name in RENAME_MAPPING.keys():
        old_path = os.path.join(BASE_DIR, old_name)
        if os.path.exists(old_path):
            missing_old_files.append(old_name)

    # 检查是否所有新文件都已存在
    missing_new_files = []
    for new_name in RENAME_MAPPING.values():
        new_path = os.path.join(BASE_DIR, new_name)
        if not os.path.exists(new_path):
            missing_new_files.append(new_name)

    if missing_old_files:
        print(f"⚠ 以下旧文件仍然存在（应该已被重命名）:")
        for f in missing_old_files:
            print(f"  - {f}")
        print()

    if missing_new_files:
        print(f"⚠ 以下新文件不存在:")
        for f in missing_new_files:
            print(f"  - {f}")
        print()

    if not missing_old_files and not missing_new_files:
        print("✓ 所有文件重命名成功！\n")

    print("=" * 80)
    print("任务完成！")
    print("=" * 80)


if __name__ == '__main__':
    main()