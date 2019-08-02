import uuid
from os import remove, path

class Symbol(object):

    def __init__(self, image, top=0, bottom=0, right=0, left=0,filename="",path="", label=""):
        self.image= image
        self.top = top
        self.bottom = bottom
        self.right = right
        self.left = left
        self.label = ""
        self.filename = str(uuid.uuid4())
        self.path = "../data/segmented/" + self.filename + ".png"

    def set_label(self, label):
        self.label = label

    def save_img(self):
        if path.isfile(self.path):
            print("File already exists!")
        else:
            self.image.save(self.path)

    def get_img_path(self):
        if not path.isfile(self.path):
            print("Such file doesn't exist")
        else:
            return self.path

    def delete_img(self):
        if not path.isfile(self.path):
            print("Such file doesn't exist")
        else:
            remove(self.path)
            print("File deleted successfully")

