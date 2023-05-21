import os as os
import sys

def i3d_features(path, file):
    os.chdir("./submodules/video_features")
    # os.system("conda env create -f conda_env_i3d.yml")
    # os.system("conda activate i3d")

    os.system("conda run -n i3d python ../../single_video_scripts/i3d_features.py "+path+" " +file)
    os.chdir("../../")

def vgg_features(path, file):
    os.chdir("./submodules/video_features")
    # os.system("conda env create -f conda_env_vggish.yml")
    # os.system("conda activate vggish")
    # os.system("wget https://storage.googleapis.com/audioset/vggish_model.ckpt -P ./models/vggish/checkpoints")
    os.system("conda run -n vggish python ../../single_video_scripts/vgg_features.py "+path+" " +file)
    os.chdir("../../")

def dense_video_captioning(path, file, search):
    os.system("conda run -n bmt python single_video_scripts/dense_video_captioning.py "+path+" "+file+" "+search)
    # os.system("conda activate bmt")

    


# full_file = "puppies.mp4"
path = sys.argv[1]
full_file = sys.argv[2]
file = full_file.split(".")[0]
search = "beam"
if len(sys.argv) >=4 :
    search = sys.argv[3]

# https://stackoverflow.com/questions/64771560/how-to-activate-a-conda-environment-within-a-python-script
# conda_path = "/home/gpu-user2/anaconda3/etc/profile.d/conda.sh"
# os.system(". "+conda_path)
print(file)
i3d_features(path, full_file)
vgg_features(path, full_file)
dense_video_captioning(path, file, search)
