import os

# 文件路径配置
classes_path = os.path.join('Obstacles in Public Spaces for Dist-YOLO/_classes.txt')
yaml_path = os.path.join('ultralytics-main/ultralytics-main/datasets/obstacles/dataset.yaml')

# 读取类别名称
with open(classes_path, 'r') as file:
    classes = [line.strip() for line in file.readlines()]

# 创建YAML配置内容
yaml_content = f"""path: {os.path.join('ultralytics-main/ultralytics-main/datasets/obstacles')}  # 数据集的根目录
train: images/train  # 训练集图像目录
val: images/val  # 验证集图像目录
test: images/test  # 测试集图像目录

nc: {len(classes)}  # 类别数量
names: {classes}  # 类别名称列表
"""

# 写入YAML配置文件
with open(yaml_path, 'w') as file:
    file.write(yaml_content)

print(f"YAML配置已生成：{yaml_path}")
