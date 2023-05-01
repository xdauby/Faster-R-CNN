# CSCI-635 simulations 
This repository contains the code of our simulations for the CSCI-635 project about Faster R-CNN.

### Installation

This code have been run in weasley nodeclient. To connect to this node enter this command line and then your password :

```sh
ssh [your id]@weasley.cs.rit.edu
```


Then, clone this repository :

```sh
git clone https://github.com/xdauby/Faster-R-CNN
```

The cloned repository tree is :

```sh
.
├── FPN_test_output.txt
├── R101_test_output.txt
├── R50_test_output.txt
├── R50_proof_of_train.txt
├── README.md
├── datasets
│   └── coco
├── main_test_coco.py
├── main_train_coco.py
└── model.py
```

Then, install requirements and detectron2 using the command (You must be in the root of the cloned folder) : 

```sh
pip install -r requirements.txt
git clone https://github.com/facebookresearch/detectron2.git
python3 -m pip install -e detectron2
```
Sometimes, you will need to download manually packages that will not be automically installed by detectron2. Please, install those packages.

You must add training(16GB) and validation(1GB) datasets. For this, go to /datasets/coco and enter the command :

```sh
wget http://images.cocodataset.org/zips/train2017.zip
wget http://images.cocodataset.org/zips/val2017.zip
wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip
```

Then, unzip all the folders using the commands :

```sh
unzip train2017.zip
unzip val2017.zip
unzip annotations_trainval2017.zip
```

Make sure that train2017 and val2017 are in /datasets/coco.
Make sure that instances_val2017.json and instances_train2017.json are in /datasets/coco/annotations. The annotations directory should have been created after having run the commands above. If it is not the case, please, create it.
(If you don't do this, the program will not work)


You're final tree must be :

```sh
.
├── FPN_test_output.txt
├── R101_test_output.txt
├── R50_test_output.txt
├── R50_proof_of_train.txt
├── README.md
├── datasets
│   └── coco
│       └── val2017
│       └── train2017
│       └── annotations
│           └── instances_val2017.json
│           └── instances_train2017.json
├── main_test_coco.py
├── main_train_coco.py
└── model.py
```

Setting up all this stuff is quite long. This is why **all the results of our executions are stored in the following txt files** :

```sh
R50_test_output.txt
R101_test_output.txt
FPN_test_output.txt
R50_proof_of_train.txt
```

### How to run 

To start inferences on the validation set, enter the command :

```sh
python3 main_test_coco.py -m [backbone option]
```
where [backbone option] can be R50, R101, FPN.


To start training on the training set, enter the command :

```sh
python3 main_train_coco.py -m [backbone option]
```
where [backbone option] can be R50, R101, FPN.




