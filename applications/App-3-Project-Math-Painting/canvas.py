import numpy as np
from PIL import Image
import os

class Canvas:
    """Object where all shapes are going to be drawn"""

    def __init__(self, height, width, color):
        self.color = color
        self.width = width
        self.height = height

        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change [0, 0, 0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


if __name__ == "__main__":
    can = Canvas(900, 900, (255, 255, 0))
    can.make(os.path.join(os.getcwd(), 'canvas.png'))
