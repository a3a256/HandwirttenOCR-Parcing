from tkinter import *
from tkinter import filedialog

import sys
import os

from CRAFT_processing import test
from CRAFT_processing.file_utils import process_bboxes
from SimpleHTR_master.src import main

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

import numpy as np

import cv2


class UI:
    def __init__(self, ui):
        self.ui = ui
        self.path = None

    def browsing_files(self):
        filename = filedialog.askopenfilename()
        self.path = filename
        # print(main.main())
        # print(test.parse(self.path, "CRAFT_processing/craft_mlt_25k.pth"))

        coordinates = test.parse(self.path, "CRAFT_processing/craft_mlt_25k.pth")
        # print(coordinates)
        boxes = process_bboxes(coordinates)

        img = Image.open(self.path)

        corner_1 = min(boxes[0][1], boxes[0][3])
        corner_2 = max(boxes[0][5], boxes[0][7])

        im = img.crop((boxes[0][0], corner_1, boxes[0][2], corner_2))

        im.show()


    def go(self):
        button = Button(master=self.ui, text="Select pitcure to parse...", command=self.browsing_files)
        button.grid(row=0, column=0)
        self.ui.mainloop()


if __name__ == "__main__":
    wn = Tk()
    ui = UI(wn)
    ui.go()