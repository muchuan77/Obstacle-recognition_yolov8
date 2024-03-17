import os
import shutil
from sklearn.model_selection import train_test_split

# 原始数据集路径
images_path = 'Obstacles in Public Spaces for Dist-YOLO/images'
labels_path = 'Obstacles in Public Spaces for Dist-YOLO/labels_num'

# 目标数据集路径
dataset_base = 'obstacles'

# 创建所需的目录结构
for split in ['train', 'val', 'test']:
    os.makedirs(os.path.join(dataset_base, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(dataset_base, 'labels', split), exist_ok=True)

# 获取所有图像文件名（不包括文件扩展名）
image_files = [os.path.splitext(f)[0] for f in os.listdir(images_path) if f.endswith(('.jpg', '.png'))]

# 划分数据集
train_files, test_files = train_test_split(image_files, test_size=0.2, random_state=42)
train_files, val_files = train_test_split(train_files, test_size=0.1, random_state=42)


# 定义一个简单的函数来复制图像和标签文件到目标目录
def copy_files(files, source_images, source_labels, dest_images, dest_labels):
    for f in files:
        shutil.copy2(os.path.join(source_images, f + '.jpg'), os.path.join(dest_images, f + '.jpg'))
        label_file = f + '.txt'
        if os.path.exists(os.path.join(source_labels, label_file)):
            shutil.copy2(os.path.join(source_labels, label_file), os.path.join(dest_labels, label_file))

# 复制文件到新的目录结构
copy_files(train_files, images_path, labels_path, os.path.join(dataset_base, 'images/train'), os.path.join(dataset_base, 'labels/train'))
copy_files(val_files, images_path, labels_path, os.path.join(dataset_base, 'images/val'), os.path.join(dataset_base, 'labels/val'))
copy_files(test_files, images_path, labels_path, os.path.join(dataset_base, 'images/test'), os.path.join(dataset_base, 'labels/test'))

print('Dataset preparation is complete.')
