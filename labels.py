from PIL import Image
import os

# 输入和输出目录路径
input_file_path = 'Obstacles in Public Spaces for Dist-YOLO/_annotations.txt'
output_dir = 'Obstacles in Public Spaces for Dist-YOLO/labels'
images_dir = 'Obstacles in Public Spaces for Dist-YOLO/images'  # 假设图像位于这个目录下

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 读取标注文件
with open(input_file_path, 'r') as f:
    for line in f:
        # 分割行来获取文件名和标注数据
        parts = line.strip().split(' ')
        image_name = parts[0]
        annotations = parts[1:]

        # 获取图像尺寸
        image_path = os.path.join(images_dir, image_name)
        with Image.open(image_path) as img:
            width, height = img.size

        # 构建输出文件路径
        output_file_name = os.path.splitext(image_name)[0] + '.txt'
        output_file_path = os.path.join(output_dir, output_file_name)

        # 写入处理后的标注到新文件
        with open(output_file_path, 'w') as out_f:
            for annotation in annotations:
                # 只保留前5个值（去除距离参数），并计算归一化坐标
                x_min, y_min, x_max, y_max, class_id = map(float, annotation.split(',')[:-1])
                x_center = ((x_min + x_max) / 2) / width
                y_center = ((y_min + y_max) / 2) / height
                norm_width = (x_max - x_min) / width
                norm_height = (y_max - y_min) / height

                # 写入归一化的坐标和类别ID
                out_f.write(f"{class_id} {x_center} {y_center} {norm_width} {norm_height}\n")
