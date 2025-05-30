#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试脚本 - 用于验证脚本管理器的执行功能
"""

import sys
import os
import datetime
import time

def main():
    while True:
        print("Hello, world!")
        time.sleep(1)  # 可选：暂停1秒，避免CPU占用过高
        print("=" * 50)
        print("测试脚本执行")
        print("=" * 50)
        print(f"当前时间: {datetime.datetime.now()}")
        print(f"Python版本: {sys.version}")
        print(f"当前工作目录: {os.getcwd()}")
        print(f"脚本路径: {__file__}")
        print("=" * 50)
        print("测试成功!")
        print("=" * 50)
        time.sleep(1)

if __name__ == "__main__":
    main()
