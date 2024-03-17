import os

input_dir = 'Obstacles in Public Spaces for Dist-YOLO/labels'  # 请更新为您的输入目录路径
output_dir = 'Obstacles in Public Spaces for Dist-YOLO/labels_num'  # 请更新为您期望的输出目录路径

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

print(f"Processing files from {input_dir} to {output_dir}")

for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename)

        print(f"Processing {input_file_path}")

        with open(input_file_path, 'r') as f, open(output_file_path, 'w') as out_f:
            for line in f:
                # 直接处理每一行的数据，不再进行分割
                parts = line.strip().split(' ')
                if len(parts) == 5:
                    class_id, x_center, y_center, width, height = parts
                    try:
                        class_id = int(float(class_id))  # 确保class_id是整数
                        # 将转换后的数据写入新文件，每个标注占据一行
                        out_f.write(f'{class_id} {x_center} {y_center} {width} {height}\n')
                    except ValueError as e:
                        print(f"Error converting annotation in file {filename}: {e}")
                else:
                    print(f"Unexpected annotation format in file {filename}: '{line.strip()}'")
