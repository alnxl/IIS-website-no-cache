import os,shutil
import zipfile
import time
import shutil
# 删除指定目录下所有文件
def empty_files(path):
    # for root, dirs, files in os.walk(path):
    #     for name in files:
    #         if name.endswith(".log") or name.endswith(".zip"):
    #             os.remove(os.path.join(root, name))
    #             print("删除文件: " + os.path.join(root, name))
    shutil.rmtree(path)
    os.mkdir(path)
# 删除指定目录下指定后缀名的文件
def delete_files_by_type(path,filetype):
    num=0
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(filetype):
                os.remove(os.path.join(root, name))
                num = num + 1
    print(path+filetype+"删除文件: " + str(num))
def copy_files(source_path,target_path):
    os.system(r"xcopy /S "+source_path+" "+target_path+"")
    # shutil.copy(source_path, target_path)


if __name__ == "__main__":
    print("测试")
