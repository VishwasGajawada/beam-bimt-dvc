cd ../../
conda deactivate
conda activate bmt
python ./sample/single_video_prediction.py \
    --prop_generator_model_path ./sample/best_prop_model.pt \
    --pretrained_cap_model_path ./sample/best_cap_model.pt \
    --vggish_features_path ./final/1/video_vggish.npy \
    --rgb_features_path ./final/1/video_rgb.npy \
    --flow_features_path ./final/1/video_flow.npy \
    --duration_in_secs 82.77 \
    --device_id 0 \
    --max_prop_per_vid 100 \
    --nms_tiou_thresh 0.4
