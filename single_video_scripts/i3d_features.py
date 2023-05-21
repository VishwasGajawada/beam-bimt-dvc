import os as os
import sys

path = sys.argv[1]
file = sys.argv[2]
# file = "puppies.mp4"
# os.system("conda env create -f conda_env_i3d.yml")

print("exctracting i3d features of ",file)

cmd = "python main.py "+    "--feature_type i3d "+    "--on_extraction save_numpy "+    "--device_ids 0 "+    "--extraction_fps 25 "+    "--video_paths ../../" + path + file+" "+    "--output_path ../../" + path
print(cmd)

os.system(cmd)