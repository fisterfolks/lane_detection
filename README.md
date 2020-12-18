# lane_detection
Final Project of course "Introduction to Computer Vision" Skoltech 2020

Dataset - TuSimple dataset can be found there: https://github.com/TuSimple/tusimple-benchmark/issues/3


train/acuracy_metric.ipynb - ipynb file with custom metric for measuring distance between line and shift
train/main_lane.ipynb - main function for training with NUM_OF_CLASSES = 3
train/main.ipynb - main function for training with NUM_OF_CLASSES = 5
train/dataset.py - util python file for NUM_OF_CLASSES = 3
train/old_dataset.py - util python file for NUM_OF_CLASSES = 5
train/erfnet.py - architecture of ERFNet

save/model_best_encoder.pth - weights of encoder
save/model_best.pth - weights of decoder
