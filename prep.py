from glob import glob
import os

files = glob("/Users/philip/Projects/GRR/visionplaying/project-1-at-2025-01-20-20-00-d1d1eed1/labels/*/*.JPG")

for file in files:
    os.rename(file, f"{file[:-4]}.txt")
    print(file, f"{file[:-4]}.txt")


# base_filepath = "/Users/philip/Projects/GRR/visionplaying/project-1-at-2025-01-20-20-00-d1d1eed1/"

# for i, image_path in enumerate(files):
#     name = image_path[len(base_filepath)+7:-4]
#     data_path = f"{base_filepath}labels/{image_path[len(base_filepath)+7:-4]}.txt"
#     print(data_path)
    
#     if i % 6 == 0:
#         os.rename(image_path, f"{base_filepath}images/val/{name}.JPG")
#         os.rename(data_path, f"{base_filepath}labels/val/{name}.txt")
#     else:
#         os.rename(image_path, f"{base_filepath}images/train/{name}.JPG")
#         os.rename(data_path, f"{base_filepath}labels/train/{name}.txt")
