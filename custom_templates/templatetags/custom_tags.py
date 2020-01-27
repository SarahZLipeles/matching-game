from django import template
import os, json, random
register = template.Library()

boxes_keys = None
with open("boxes_key.json", "r") as f:
    boxes_keys = json.loads(f.read())
BOXES = '%s/_static/boxes/' % os.getcwd()

@register.inclusion_tag('_delayed_next.html')
def delayed_next(wait=2000, label="NEXT"):
    return {
        "wait_time": wait,
        "label": label
    }

@register.inclusion_tag('_counting_task.html')
def counting_box(field_name="test", img_set_number=1):
    img_dir = "%s%d" % (BOXES, img_set_number)
    print(img_dir)
    list_images = os.listdir(path=(img_dir))
    img_name = random.choice(list_images)
    img = "boxes/%d/%s" % (img_set_number, img_name)
    num_zeros=int(boxes_keys[img_name[:-4]][:-4].split('-')[1])
    return {
        "img_name": img,
        "answer": num_zeros,
        "field_name": field_name
    }
