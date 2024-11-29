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

class UI:
    def __init__(self, ui):
        self.ui = ui
        self.path = None

    def browsing_files(self):
        filename = filedialog.askopenfilename()
        self.path = filename
        # print(main.main())
        # print(test.parse(self.path, "CRAFT_processing/craft_mlt_25k.pth"))

        # coordinates = test.parse(self.path, "CRAFT_processing/craft_mlt_25k.pth")

        # boxes = process_bboxes(coordinates)

        # print(boxes)

        im = Image.open(self.path)

        img2 = im.crop((2, 9, 135, 65))

        # Create figure and axes
        fig, ax = plt.subplots()

        # Display the image
        ax.imshow(img2)

        plt.show()

    def go(self):
        button = Button(master=self.ui, text="Select pitcure to parse...", command=self.browsing_files)
        button.grid(row=0, column=0)
        self.ui.mainloop()


if __name__ == "__main__":
    wn = Tk()
    ui = UI(wn)
    ui.go()