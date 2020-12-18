# lane_detection
Final Project of course "Introduction to Computer Vision" Skoltech 2020

Dataset - TuSimple dataset can be found there: https://github.com/TuSimple/tusimple-benchmark/issues/3


train/acuracy_metric.ipynb - ipynb file with custom metric for measuring distance between line and shift

This metric was created by ego-vehicle localization from paper
On Perfomance Evaluation Metrics for Lane Estimation, R.K.Satzoda, M.M.Trivedi, 2014, ICPR.
https://www.semanticscholar.org/paper/On-Performance-Evaluation-Metrics-for-Lane-Satzoda-Trivedi/7c72e50fd4918fa28b8024105af728965788a873


train/main_lane.ipynb - main function for training with NUM_OF_CLASSES = 3


train/main.ipynb - main function for training with NUM_OF_CLASSES = 5


train/dataset.py - util python file for NUM_OF_CLASSES = 3


train/old_dataset.py - util python file for NUM_OF_CLASSES = 5


train/erfnet.py - architecture of ERFNet


save/model_best_encoder.pth - weights of encoder


save/model_best.pth - weights of decoder


eval/lane_predict_visualize.ipynb - example of single prediction of detecting lanes on image from test_set
