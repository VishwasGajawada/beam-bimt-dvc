
# vgg
conda deactivate
conda activate vggish
python main.py \
    --feature_type vggish \
    --on_extraction save_numpy \
    --device_ids 0 \
    --video_paths ../../final/1/video.mp4 \
    --output_path ../../final/1


