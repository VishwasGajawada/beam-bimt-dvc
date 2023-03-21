def get_combined_caption(captions) :
    for i in range(len(captions)) :
        captions[i]['duration'] = captions[i]['end'] - captions[i]['start']

    captions = sorted(captions, key = lambda x : (x['start'], x['duration']))
    return captions


captions = [{'start': 70.0, 'end': 118.9, 'sentence': 'He is doing a basketball game'}, 
{'start': 4.4, 'end': 20.0, 'sentence': 'A man is seen standing on a court and leads into a basketball court playing basketball'}, {'start': 99.3, 'end': 127.0, 'sentence': 'The man continues to speak to the camera while the man continues to speak to the camera'}, {'start': 0.3, 'end': 2.7, 'sentence': 'We see a title screen'}, {'start': 14.4, 'end': 110.8, 'sentence': 'The man is seen speaking to the camera while another man is seen speaking to the camera'}, {'start': 0.0, 'end': 56.8, 'sentence': 'A man is seen standing in a court speaking to the camera while a man is seen speaking to the camera'}, 
{'start': 13.7, 'end': 33.4, 'sentence': 'The man continues to talk about how to do the same'}, 
{'start': 0.9, 'end': 7.0, 'sentence': 'A white screen appears with white words on the screen'}]

captions = get_combined_caption(captions)
print(type(captions))
print(captions)
