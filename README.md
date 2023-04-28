# CSCI-635 simulations 
This repository contains the code of our simulations for the CSCI-635 project about faster r-cnn.
### Installation

First clone this repository :

```sh
git clone ...
```

The cloned repository tree is :



Then, install detectron2. (You must be in the root of the cloned folder)

```sh
python3 -m pip install -e detectron2
```
Sometimes, you will need to download manually packages that will not be automically installed by detectron2. Please, install those packages.

You must add training(16GB) and validation(1GB) datasets. For this, go to /../.. and enter the command :

```sh
wget http://images.cocodataset.org/zips/train2017.zip
wget http://images.cocodataset.org/zips/val2017.zip
wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip
```

Then, unzip all the folders.

Make sure that train2017 and val2017 are in ...
Make sure that instances_val2017.json and instances_train2017.json are in ...
(If you don't do this, the program will not work)

Setting up all this stuff is quite long. This is why all the results of our executions are stored in the following txt files :

