import os
import time


# get Image from selectable screen area
def get_scrot_image():
    filename = "{}.png".format(str(round(time.time() * 1000)))
    quality = 100
    command = "scrot -s {} -q {}".format(filename, quality)
    os.system(command)
    return filename


# delete processed file
def remove_file(filename):
    os.remove(filename)
