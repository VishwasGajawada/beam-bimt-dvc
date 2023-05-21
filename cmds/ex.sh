cd ./submodules/video_features
conda deactivate
conda activate i3d
python main.py \
    --feature_type i3d \
    --on_extraction save_numpy \
    --device_ids 0 \
    --extraction_fps 25 \
    --video_paths ../../final/2/video.mp4 \
    --output_path ../../final/2/

# vgg
conda deactivate
conda activate vggish
python main.py \
    --feature_type vggish \
    --on_extraction save_numpy \
    --device_ids 0 \
    --video_paths ../../final/2/video.mp4 \
    --output_path ../../final/2


cd ../../
conda deactivate
conda activate bmt
python ./sample/single_video_prediction.py \
    --prop_generator_model_path ./sample/best_prop_model.pt \
    --pretrained_cap_model_path ./sample/best_cap_model.pt \
    --vggish_features_path ./final/2/video_vggish.npy \
    --rgb_features_path ./final/2/video_rgb.npy \
    --flow_features_path ./final/2/video_flow.npy \
    --duration_in_secs 31.564 \
    --device_id 0 \
    --max_prop_per_vid 100 \
    --nms_tiou_thresh 0.4
