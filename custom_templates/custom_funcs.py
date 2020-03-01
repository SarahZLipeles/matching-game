import json, os, random

def get_box():
    boxes_keys = None
    with open("boxes_key.json", "r") as f:
        boxes_keys = json.loads(f.read())
    BOXES = '%s/_static/boxes/' % os.getcwd()
    list_images = os.listdir(path=(BOXES))
    img_name = random.choice(list_images)
    num_zeros = boxes_keys[img_name[:-4]][:-4].split('-')[1]
    return img_name, num_zeros
