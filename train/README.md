# Training ERFNet in Pytorch

Main paper of using Neural network this: Efficient ConvNet for Real-time Semantic Segmentation
E. Romera, J.M.Alvarez, L.M.Bergasa,R.Arroyo 2017
http://www.robesafe.uah.es/personal/eduardo.romera/pdfs/Romera17iv.pdf


## Output files generated for each training:
Each training will create a new folder in the "erfnet_pytorch/save/" directory named with the parameter --savedir and the following files:
* **automated_log.txt**: Plain text file that contains in columns the following info of each epoch {Epoch, Train-loss,Test-loss,Train-IoU,Test-IoU, learningRate}. Can be used to plot using Gnuplot or Excel.
* **best.txt**: Plain text file containing a line with the best IoU achieved during training and its epoch.
* **checkpoint.pth.tar**: bundle file that contains the checkpoint of the last trained epoch, contains the following elements: 'epoch' (epoch number as int), 'arch' (net definition as a string), 'state_dict' (saved weights dictionary loadable by pytorch), 'best_acc' (best achieved accuracy as float), 'optimizer' (saved optimizer parameters).
* **{model}.py**: copy of the model file used (default erfnet.py). 
* **model.txt**: Plain text that displays the model's layers
* **model_best.pth**: saved weights of the epoch that achieved best val accuracy.
* **model_best.pth.tar**: Same parameters as "checkpoint.pth.tar" but for the epoch with best val accuracy.
* **opts.txt**: Plain text file containing the options used for this training

NOTE: Encoder trainings have an added "_encoder" tag to each file's name.

## IoU display during training

NEW: In previous code, IoU was calculated using a port of the cityscapes scripts, but new code has been added in "iouEval.py" to make it class-general, non-dependable on other code, and much faster (using cuda)

By default, only Validation IoU is calculated for faster training (can be changed in options)
