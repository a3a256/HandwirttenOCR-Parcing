from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

import sys
import os

from CRAFT_processing import test
from CRAFT_processing.file_utils import process_bboxes
# from SimpleHTR_master.src import main

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

import numpy as np

# import tensorflow as tf


class UI:
    def __init__(self, ui):
        self.ui = ui
        self.path = None
        self.textfield = ScrolledText(self.ui, wrap=WORD)

    def browsing_files(self):
        filename = filedialog.askopenfilename()
        self.path = filename

        self.textfield.delete("1.0", END)

        coordinates = test.parse(self.path, "CRAFT_processing/craft_mlt_25k.pth")
        boxes = process_bboxes(coordinates)

        img = Image.open(self.path)

        bounding_boxes = []
        for box in boxes:
            corner_1 = min(box[1], box[3])
            corner_2 = min(box[5], box[7])
            bounding_box = [box[0], corner_1, box[2], corner_2]
            bounding_boxes += [bounding_box]

        bounding_boxes = sorted(bounding_boxes, key=lambda x: (x[0], x[1], x[2], x[3]))

        result = []
        for box in bounding_boxes:
            im = img.crop((box[0], box[1], box[2], box[3]))
            im.save("SimpleHTR_master/data/obj.png", "PNG")

            os.system("python3 SimpleHTR_master/src/main.py")
            os.remove("SimpleHTR_master/data/obj.png")

            f = open("result.txt", "r")
            result += [f.read()]
            f.close()

        res = " ".join(result)

        print(res)

        self.textfield.insert(END, res)


    def go(self):
        button = Button(master=self.ui, text="Select pitcure to parse...", command=self.browsing_files)
        button.grid(row=0, column=0)
        self.textfield.grid(row=1, column=0)
        self.ui.mainloop()


if __name__ == "__main__":
    wn = Tk()
    ui = UI(wn)
    ui.go()