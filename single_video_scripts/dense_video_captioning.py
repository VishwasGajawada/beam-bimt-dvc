import os as os
import sys

file = sys.argv[1]
print(file)


os.system("python ./sample/single_video_prediction.py "+
"--prop_generator_model_path ./sample/best_prop_model.pt "+
"--pretrained_cap_model_path ./sample/best_cap_model.pt "+
"--vggish_features_path ./test/" +file+"_vggish.npy "+
"--rgb_features_path ./test/" +file+ "_rgb.npy "+
"--flow_features_path ./test/" +file+"_flow.npy "+
"--duration_in_secs 72 "+
"--device_id 0 "+
"--max_prop_per_vid 100 "+
"--nms_tiou_thresh 0.4 ")


"""
python ./sample/single_video_prediction.py \
    --prop_generator_model_path ./sample/best_prop_model.pt \
    --pretrained_cap_model_path ./sample/best_cap_model.pt \
    --vggish_features_path ./test/puppies_vggish.npy \
    --rgb_features_path ./test/puppies_rgb.npy \
    --flow_features_path ./test/puppies_flow.npy \
    --duration_in_secs 99 \
    --device_id 0 \
    --max_prop_per_vid 100 \
    --nms_tiou_thresh 0.4
"""