'''
打开指定路径下的文件，并遍历计算每个文件行数
'''

import os

def countLines(fname):
    try:
        with open(fname) as f:
            data = f.readlines()
    except FileNotFoundError:
        print(fname + ' does not exist')
    lens = len(data)
    print(fname.split('\\')[1] + 'has' + str(lens)+ ' lines')

path = './testdata'
for fname in os.listdir(path)
    if fname.endwith('.txt')
        file_path = os.path.join(path, fname)
        countLines(file_path)