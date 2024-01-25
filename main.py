import os
from os.path import abspath, join, getsize
def script(path,n):
    sizes = {}

    for top_dir, directories, files in os.walk(path):
        for _file in files:
            full_path = abspath(join(top_dir, _file))
            size = getsize(full_path)
            sizes[full_path] = size
            #break


    for path in  dict(list(sizes.items())[0: n+1]):
        if sizes[path] >50:
            print("Path: {0}, size: {1}".format(path, sizes[path]))
if __name__ =="__main__":
    script('.',3)