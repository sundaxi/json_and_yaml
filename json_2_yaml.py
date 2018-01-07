#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 1/7/2018 6:15 PM
# @Author  : Ying Sun
# @Link    : yinsun@microsoft.com
# @Version : 0.1

import json,yaml
import os
import sys


def json_convert_yaml(file):
    with open(file,'r+',encoding='utf-8') as f:
        json_load = json.load(f)
        json_load_yaml_dump = yaml.dump(json_load)
    print(json_load_yaml_dump)

def yaml_convert_json(file):
    with open(file,'r+',encoding='utf-8') as f:
        yaml_load = yaml.load(f)
        yaml_load_json_dump = json.dump(yaml_load)
    print(yaml_load_json_dump)

if __name__ == '__main__':
    try:
        if len(sys.argv) > 0:
            for file in sys.argv[1:]:
                print(file)
                json_convert_yaml(file)
        else:
            print("Please follow with the jsonfile")
    except Exception as e:
        print("Error! ", e)
