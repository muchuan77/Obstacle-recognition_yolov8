import os

# 设置原始文件夹和目标文件夹的路径
source_folder = 'D:\pythonyolov8\Obstacles in Public Spaces for Dist-YOLO\labels'
destination_folder = 'D:\pythonyolov8\Obstacles in Public Spaces for Dist-YOLO\labels_new'

# 确保目标文件夹存在
os.makedirs(destination_folder, exist_ok=True)

# 遍历原始文件夹中的所有文件
for filename in os.listdir(source_folder):
    if filename.endswith('.txt'):
        source_file_path = os.path.join(source_folder, filename)
        destination_file_path = os.path.join(destination_folder, filename)

        # 读取每个文件的内容
        with open(source_file_path, 'r') as file:
            lines = file.readlines()

        # 调整每行的第一个数字
        adjusted_lines = []
        for line in lines:
            parts = line.strip().split()
            parts[0] = str(float(parts[0]) - 1)  # 减一并转换回字符串
            adjusted_line = ' '.join(parts) + '\n'
            adjusted_lines.append(adjusted_line)

        # 将调整后的内容写入到目标文件夹中的新文件
        with open(destination_file_path, 'w') as file:
            file.writelines(adjusted_lines)
