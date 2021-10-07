#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple Image Background Removal
API - RemoveBG
"""

__author__ = "Bisina Wickremasinghe"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Bisina Wickremasinghe"

import platform
import os
import requests
import time

file_path_unprocessed = None
file_path_bg_removed = None

if platform.system() == "Windows":
    print(platform.system())
    file_path_unprocessed = "unprocessed\\"
    file_path_bg_removed = "bg_removed\\"
elif platform.system() == "Linux":
    print("Only Supported on Windows")

image_list = os.listdir(file_path_unprocessed)
for image in image_list:
    time.sleep(30)
    print(f"Processing Image : {image}")
    try:
        filename = str(image)
        response = requests.post(
            "https://api.remove.bg/v1.0/removebg",
            files={"image_file": open(f"{file_path_unprocessed}{filename}", "rb")},
            data={"size": "auto"},
            headers={"X-Api-Key": "11u5LTRkfZ5hByRFtF2gLVei"},
        )
        if response.status_code == requests.codes.ok:
            with open(f"{file_path_bg_removed}{filename}-no-bg.png", "wb") as out:
                out.write(response.content)
                print(f"Image Converted Successfully, New Image saved in : {file_path_bg_removed}{filename}-no-bg.png")
        else:
            print(f"Error: {response.status_code} \nResponse: {response.text}")
    except Exception as error:
        print(f"Error occurred: {error}")


