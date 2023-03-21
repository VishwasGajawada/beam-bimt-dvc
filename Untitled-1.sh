cd ../../
conda activate bmt
python ./sample/single_video_prediction.py \
    --prop_generator_model_path ./sample/best_prop_model.pt \
    --pretrained_cap_model_path ./sample/best_cap_model.pt \
    --vggish_features_path ./test/puppies_vggish.npy \
    --rgb_features_path ./test/puppies_rgb.npy \
    --flow_features_path ./test/puppies_flow.npy \
    --duration_in_secs 163 \
    --device_id 0 \
    --max_prop_per_vid 100 \
    --nms_tiou_thresh 0.4