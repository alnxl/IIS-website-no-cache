# coding: utf-8
# 维护脚本
import argparse
import os.path
from function import file
# 源文件夹路径
source_file_path = ""
# 需要清空的文件夹路径
empty_file_path = ""

def get_check_argument():
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--source_file_path', type=str, default=None)
    parser.add_argument('--empty_file_path', type=str, default=None)

    args = parser.parse_args()
    global source_file_path
    source_file_path = args.source_file_path
    global empty_file_path
    empty_file_path = args.empty_file_path
    if source_file_path is None or not os.path.exists(source_file_path):
        print("不是有效的文件路径")
        return False
    if empty_file_path is None or not os.path.exists(empty_file_path):
        print("不是有效的文件路径")
        return False
    return True
def RunApp():
    # 第一步 清空文件夹
    file.empty_files(empty_file_path)
    # 第二步 复制文件夹至指定目录
    file.copy_files(source_file_path, empty_file_path)
    # 第三步 删除指定目录下js文件
    file.delete_files_by_type(empty_file_path+"\\js", ".js")
    # 第四部 删除指定目录下cshtml文件
    file.delete_files_by_type(empty_file_path + "\\Views", ".cshtml")
    # 第五步 删除指定目录下log文件
    file.delete_files_by_type(empty_file_path + "\\weblog", ".log")
    return True

if __name__ == "__main__":
    if get_check_argument():
        print("开始执行脚本")
        RunApp()
    else:
        print("执行脚本中止")