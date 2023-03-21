import os as os
import sys

file = sys.argv[1]
print(file)

print("exctracting vggish features of ",file)
# file = "puppies.mp4"

# os.system("conda env create -f conda_env_vggish.yml")
# os.system("wget https://storage.googleapis.com/audioset/vggish_model.ckpt -P ./models/vggish/checkpoints")

os.system("python main.py "+
"--feature_type vggish "+
"--on_extraction save_numpy "+
"--device_ids 0 "+
"--video_paths ../../test/"+file+" "+
"--output_path ../../test/ ")