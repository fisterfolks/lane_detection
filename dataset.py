import numpy as np
import os

from PIL import Image

from torch.utils.data import Dataset

def load_image(file):
    return Image.open(file)

def is_image(filename):
    return any(filename.endswith(ext) for ext in EXTENSIONS)

def is_label(filename):
    return filename.endswith("_labelTrainIds.png")

def image_path(root, basename, extension):
    return os.path.join(root, f'{basename}{extension}')

def image_path_city(root, name):
    return os.path.join(root, f'{name}')

def image_basename(filename):
    return os.path.basename(os.path.splitext(filename)[0])

class lanes(Dataset):

    def __init__(self, root, transform=None, num_classes=3):
        self.root_data = root+"data"
        self.root_labels = root+"labels"
        self.num_classes = num_classes
        self.filenames = [f for f in os.listdir(self.root_data) if os.path.isfile(os.path.join(self.root_data, f))]
        self.filenames.sort()

        

        self.transform = transform # ADDED THIS


    def __getitem__(self, index):
        filename = self.filenames[index]
        
        label1 , label2, label3 = 0, 0, 0
        with open(image_path_city(self.root_data, filename), 'rb') as f:
            image = load_image(f).convert('RGB')
        with open(image_path_city(self.root_labels, os.path.splitext(filename)[0]+"_1.png"), 'rb') as f:
            label1 = load_image(f).convert('P')
        with open(image_path_city(self.root_labels, os.path.splitext(filename)[0]+"_2.png"), 'rb') as f:
            label2 = load_image(f).convert('P')
        with open(image_path_city(self.root_labels, os.path.splitext(filename)[0]+"_3.png"), 'rb') as f:
            label3 = load_image(f).convert('P')
            
        label = [label1 , label2, label3]

        if self.transform is not None:
            image, label = self.transform(image, label)

        return image, label

    def __len__(self):
        return len(self.filenames)