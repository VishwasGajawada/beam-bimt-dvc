import json
import csv
import random

# Load train.json
with open('train.json', 'r') as f:
    train_json = json.load(f)

# Get list of video IDs
video_ids = list(train_json.keys())
print(len(video_ids))
# Shuffle the list of video IDs
random.shuffle(video_ids)
video_ids_to_remove = []
# Remove 50% of the videos
for i in range(len(video_ids) // 2):
    del train_json[video_ids[i]]
    video_ids_to_remove.append(video_ids[i])
print(len(video_ids_to_remove))
# Update train.csv
# with open('train.csv', 'r') as f:
#     reader = csv.reader(f)
#     rows = list(reader)

#     # Create a list of video IDs to remove
#     video_ids_to_remove = [video_id for video_id in rows if video_id[0] in video_ids[:len(video_ids) // 2]]
# print(video_ids_to_remove[])
# Rewrite train.csv without the removed video IDs
cnt =0
with open('train.csv', 'r', newline='') as f:
    with open('train1.csv', 'w', newline='') as f1:
        reader = csv.reader(f)
        writer = csv.writer(f1)
        rows = list(reader)
        print(len(rows))
        for row in rows:
            if row[0].split("\t")[0] not in video_ids_to_remove:
                writer.writerow(row)
                # print(row[0].split("\t")[0])
                cnt +=1
            else :
                print(row[0].split("\t")[0])
print(cnt)
# Write updated train.json
with open('train.json', 'w') as f:
    json.dump(train_json, f)
