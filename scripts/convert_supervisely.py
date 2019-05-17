#!/usr/bin/env python3
import json, os

def convert_annotation(obj):
    assert(obj["classTitle"] == "Знак")
    assert(obj["bitmap"] == None)
    assert(obj["points"]["interior"] == [])
    class_id = [val["value"] for val in obj["tags"] if val["name"] == "Класс"]
    if len(class_id) == 0:
        raise Exception("Sign without class")
    class_id = class_id[0]
    is_temp = [val["value"] for val in obj["tags"] if val["name"] == "Временный"]
    is_temp = "false" if is_temp == [] else "true"
    is_occl = [val["value"] for val in obj["tags"] if val["name"] == "Преграждён"]
    is_occl = "false" if is_temp == [] else "true"
    data = [val["value"] for val in obj["tags"] if val["name"] == "Данные"]
    data = "" if data == [] else data[0]
    bbox = obj["points"]["exterior"]
    assert(len(bbox) == 2 and len(bbox[0]) == 2 and len(bbox[0]) == 2)
    xtl = bbox[0][0]
    ytl = bbox[0][1]
    xbr = bbox[1][0]
    ybr = bbox[1][1]
    assert(xtl % 1 == 0 and ytl % 1 == 0 and xbr % 1 == 0 and ybr % 1 == 0)
    assert(xtl < xbr and ytl < ybr)
    points = "%d\t%d\t%d\t%d" % (int(xtl), int(ytl), int(xbr), int(ybr))
    return "\t".join([class_id, points, is_temp, is_occl, data])

def convert_json(path):
    data = json.load(open(path))
    if data["objects"] == []:
        if data["tags"] != [{'name': 'Пустой', 'value': None}]:
            raise Exception("no objects and no empty tag")
        return ""
    if data["tags"] != []:
        raise Exception("annotated objects and frame tag(s)")
    buf = []
    for obj in data["objects"]:
        buf.append(convert_annotation(obj))
    return "\n".join(buf)

def tsv_count(dir):
    c = 0
    for f in os.listdir(dir):
        d = len(open(os.path.join(dir, f)).read().split('\n'))
        c += 1 if d == 0 else d
    return c

def process_dir(in_dir, out_dir):
    os.mkdir(out_dir)
    for f in sorted(os.listdir(in_dir)):
        fid = f.split('.')[0]
        try:
            res = convert_json(os.path.join(in_dir, f))
            open(os.path.join(out_dir, fid + ".tsv"), "w").write(res)
        except Exception as err:
            print("failed to process %s: " % fid, err)

