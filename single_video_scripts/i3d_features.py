import os as os
import sys

file = sys.argv[1]
# file = "puppies.mp4"
# os.system("conda env create -f conda_env_i3d.yml")

print("exctracting i3d features of ",file)


os.system("python main.py "+
"--feature_type i3d "+
"--on_extraction save_numpy "+
"--device_ids 0 "+
"--extraction_fps 25 "+
"--video_paths ../../test/"+file+" "+
"--output_path ../../test/")