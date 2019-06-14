import os

data_path = '../../../boyuan/Datasets/KITTI/training/image_02'

#data_path = '../image_02'

if not (os.path.exists("data/Kitti/")):
    os.makedirs("data/Kitti/")


f_train= open("data/Kitti/train_full.txt","w+")

folder_lst = os.listdir(data_path)

for sub_dir in folder_lst[:-2]:
    path = os.path.join(data_path, sub_dir)
    if os.path.isdir(path):
        num_frame = len(os.listdir(path))

        line = sub_dir + " " + str(num_frame) + "\n"
        f_train.write(line)

f_train.close()

f_val= open("data/Kitti/val_full.txt","w+")


for sub_dir in folder_lst[-2:]:
    path = os.path.join(data_path, sub_dir)
    num_frame = len(os.listdir(path))

    line = sub_dir + " " + str(num_frame) + "\n"
    f_val.write(line)

f_val.close()

