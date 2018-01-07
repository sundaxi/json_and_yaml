#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 1/7/2018 8:10 PM
# @Author  : Ying Sun
# @Link    : yinsun@microsoft.com
# @Version : 0.1

import json,yaml
import os
import sys

def yaml_convert_json(file):
    with open(file,'r+',encoding='utf-8') as f:
        yaml_load = yaml.load(f)
        print(type(yaml_load))
        yaml_load_json_dump = json.dumps(yaml_load)
    print(yaml_load_json_dump)

if __name__ == '__main__':
    try:
        if len(sys.argv) > 0:
            for file in sys.argv[1:]:
                print(file)
                yaml_convert_json(file)
        else:
            print("Please follow with the yaml file")
    except Exception as e:
        print("Error! ", e)