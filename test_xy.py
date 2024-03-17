import os

# 使用绝对路径来避免路径错误，这里以一个示例路径替代，请根据您的实际路径进行修改
script_dir = os.path.dirname(__file__)  # 获取当前脚本的目录
labels_dir = os.path.join(script_dir, 'Obstacles in Public Spaces for Dist-YOLO/labels_new')

# 遍历labels文件夹中的每个文件
for label_file in os.listdir(labels_dir):
    file_path = os.path.join(labels_dir, label_file)

    # 打开并读取每个文件
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            parts = line.strip().split()
            # 预期每行有5个部分：x_min, y_min, x_max, y_max, class_id
            if len(parts) == 5:
                # 提取所有值
                x_min, y_min, x_max, y_max, class_id = map(float, parts[:5])
                # 检查坐标是否在0到1之间，这里假设坐标已经归一化
                if not all(0.0 <= val <= 1.0 for val in [x_min, y_min, x_max, y_max]):
                    print(f"文件 {label_file}, 行 {line_number}: 坐标或尺寸超出预期范围。")
            else:
                print(f"文件 {label_file}, 行 {line_number}: 数据格式可能不正确，期望5个值。")
