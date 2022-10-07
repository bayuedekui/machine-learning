import os
import re
import threading


def copy(path):
    filename = os.path.basename(path)
    dir_name = os.path.dirname(path)
    new_filename = "new_" + filename
    return os.path.join(dir_name, new_filename)

def threading_code():
    print(threading.active_count())


def replace_file_str():
    for filename in os.listdir("project"):
        if filename.startswith("new_"):
            continue
        file_dir = os.path.join("project", filename)
        with open(file_dir, 'r') as f1:
            str = f1.read()
            new_str = re.sub(r"morvanzhou.github.io", "bayuedekui.com", str)
            with open(os.path.join("project", "new_" + filename), 'w') as f2:
                f2.write(new_str)


if __name__ == '__main__':
    print("当前目录：", os.getcwd())
    print("当前目录内容：", os.listdir())
    os.makedirs("project", exist_ok=True)
    print(os.path.exists("project"))
    # print(copy("D:\\EEEEEEEEEEEEEEEEEEEEEEEEEEEE\\PythonProjects\\machine-learning\\aaaa.py"))
    # replace_file_str()
    threading_code()