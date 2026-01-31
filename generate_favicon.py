#!/usr/bin/env python3
import struct
import zlib

def create_simple_png(width, height, color):
    """创建一个简单的PNG图片"""
    def make_png_chunk(chunk_type, data):
        chunk = chunk_type + data
        return struct.pack('>I', len(data)) + chunk + struct.pack('>I', zlib.crc32(chunk) & 0xffffffff)

    # PNG signature
    signature = b'\x89PNG\r\n\x1a\n'

    # IHDR chunk
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)  # 8-bit RGB
    ihdr = make_png_chunk(b'IHDR', ihdr_data)

    # IDAT chunk (image data)
    raw_data = b''
    r, g, b = color
    for y in range(height):
        raw_data += b'\x00'  # filter byte
        for x in range(width):
            raw_data += bytes([r, g, b])

    compressed_data = zlib.compress(raw_data, 9)
    idat = make_png_chunk(b'IDAT', compressed_data)

    # IEND chunk
    iend = make_png_chunk(b'IEND', b'')

    return signature + ihdr + idat + iend

def create_ico_file():
    """创建favicon.ico文件，包含16x16和32x32两种尺寸"""
    # Python蓝色颜色
    python_blue = (55, 118, 234)

    # 创建16x16和32x32的PNG数据
    png_16 = create_simple_png(16, 16, python_blue)
    png_32 = create_simple_png(32, 32, python_blue)

    # ICO文件头
    # 1. ICO头: 2字节 reserved, 2字节 type (1=ICO), 2字节 count
    ico_header = struct.pack('<HHH', 0, 1, 2)  # 2 images

    # 2. 目录条目 (每个16字节)
    # Entry 1: 16x16
    entry_1 = struct.pack('<BBBBHHII',
        16,  # width
        16,  # height
        0,   # colors (0 = 256+)
        0,   # reserved
        1,   # planes
        32,  # bits per pixel
        len(png_16),  # image size
        22   # offset from beginning of file
    )

    # Entry 2: 32x32
    entry_2 = struct.pack('<BBBBHHII',
        32,  # width
        32,  # height
        0,   # colors
        0,   # reserved
        1,   # planes
        32,  # bits per pixel
        len(png_32),  # image size
        22 + len(png_16)  # offset
    )

    # 写入文件
    with open('favicon.ico', 'wb') as f:
        f.write(ico_header)
        f.write(entry_1)
        f.write(entry_2)
        f.write(png_16)
        f.write(png_32)

    print(f"favicon.ico 创建成功!")
    print(f"  - 16x16 PNG: {len(png_16)} bytes")
    print(f"  - 32x32 PNG: {len(png_32)} bytes")
    print(f"  - 总大小: {len(ico_header) + len(entry_1) + len(entry_2) + len(png_16) + len(png_32)} bytes")

if __name__ == '__main__':
    create_ico_file()
