
from model import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--models', '-m', default='R50')
args = parser.parse_args()

models = args.models

#Load the model
register_coco_instances('coco_val_2017', {}, 'datasets/coco/annotations/instances_val2017.json', 'datasets/coco/val2017')

if models == 'R50':

    print('R50 models :')

    #ResNet50
    backbone_R_50_C4_1x = "COCO-Detection/faster_rcnn_R_50_C4_1x.yaml"
    backbone_R_50_DC5_1x = "COCO-Detection/faster_rcnn_R_50_DC5_1x.yaml"
    backbone_R_50_C4_3x = "COCO-Detection/faster_rcnn_R_50_C4_3x.yaml"
    backbone_R_50_DC5_3x = "COCO-Detection/faster_rcnn_R_50_DC5_3x.yaml"

    #Define models 
    model_backbone_R_50_C4_1x = Model()
    model_backbone_R_50_DC5_1x = Model()
    model_backbone_R_50_C4_3x = Model()
    model_backbone_R_50_DC5_3x = Model()

    #Config models 
    model_backbone_R_50_C4_1x.config_model(backbone_R_50_C4_1x)
    model_backbone_R_50_DC5_1x.config_model(backbone_R_50_DC5_1x)
    model_backbone_R_50_C4_3x.config_model(backbone_R_50_C4_3x)
    model_backbone_R_50_DC5_3x.config_model(backbone_R_50_DC5_3x)

    #Inferences on validation coco dataset 
    model_backbone_R_50_C4_1x.inferences('coco_val_2017')
    model_backbone_R_50_DC5_1x.inferences('coco_val_2017')
    model_backbone_R_50_C4_3x.inferences('coco_val_2017')
    model_backbone_R_50_DC5_3x.inferences('coco_val_2017')
    
elif models == 'R101':

    print('R101 models :')
    
    #ResNet101
    backbone_R_101_C4_3x = "COCO-Detection/faster_rcnn_R_101_C4_3x.yaml"
    backbone_R_101_DC5_3x = "COCO-Detection/faster_rcnn_R_101_DC5_3x.yaml"
    
    #Define models 
    model_backbone_R_101_C4_3x = Model()
    model_backbone_R_101_DC5_3x = Model()

    #Config models
    model_backbone_R_101_C4_3x.config_model(backbone_R_101_C4_3x)
    model_backbone_R_101_DC5_3x.config_model(backbone_R_101_DC5_3x)

    #Inferences on validation coco dataset 
    model_backbone_R_101_C4_3x.inferences('coco_val_2017')
    model_backbone_R_101_DC5_3x.inferences('coco_val_2017')

elif models == 'FPN':

    print('FPN models :')
    
    #FPN
    backbone_R_50_FPN_1x = "COCO-Detection/faster_rcnn_R_50_FPN_1x.yaml"
    backbone_R_50_FPN_3x = "COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"
    backbone_R_101_FPN_3x = "COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml"

    #Define models 
    model_backbone_R_50_FPN_1x = Model()
    model_backbone_R_50_FPN_3x = Model()
    model_backbone_R_101_FPN_3x = Model()

    #Config models
    model_backbone_R_50_FPN_1x.config_model(backbone_R_50_FPN_1x)
    model_backbone_R_50_FPN_3x.config_model(backbone_R_50_FPN_3x)
    model_backbone_R_101_FPN_3x.config_model(backbone_R_101_FPN_3x)

    #Inferences on validation coco dataset 
    model_backbone_R_50_FPN_1x.inferences('coco_val_2017')
    model_backbone_R_50_FPN_3x.inferences('coco_val_2017')
    model_backbone_R_101_FPN_3x.inferences('coco_val_2017')

else:

    print('Invalid argument : models are "R50", "R101", "FPN".')
    print("Please use : python3 main_test_coco.py -m [model name]")
    print("By default, R50 is used.")















