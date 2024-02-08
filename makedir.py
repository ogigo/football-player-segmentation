import os

parent_dirpath = "yolov8"

os.mkdir(parent_dirpath)

os.mkdir(os.path.join(parent_dirpath, "train"))
os.mkdir(os.path.join(parent_dirpath, "train", "images"))
os.mkdir(os.path.join(parent_dirpath, "train", "labels"))

os.mkdir(os.path.join(parent_dirpath, "test"))
os.mkdir(os.path.join(parent_dirpath, "test", "images"))
os.mkdir(os.path.join(parent_dirpath, "test", "labels"))

