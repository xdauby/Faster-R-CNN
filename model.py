import sys, os
sys.path.insert(0, os.path.abspath('./detectron2'))

import torch, detectron2
# Some basic setup:
# Setup detectron2 logger

# Some basic setup:
# Setup detectron2 logger
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import os, json, random

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.utils.visualizer import ColorMode, Visualizer
from detectron2.evaluation import COCOEvaluator, inference_on_dataset
from detectron2.data import build_detection_test_loader
from detectron2.evaluation import COCOEvaluator, inference_on_dataset


from detectron2.data.datasets import register_coco_instances
from detectron2.evaluation import COCOEvaluator, inference_on_dataset
from detectron2.data import build_detection_test_loader
from detectron2.engine import DefaultTrainer

class Model:

  #Model configuration
  def config_model(self, model=None, bool_pre_trained_weights = True, roi_threshold = 0.5):

    self.cfg = get_cfg()
    self.cfg.MODEL.DEVICE = "cuda:6"
    self.cfg.merge_from_file(model_zoo.get_config_file(model))
    
    self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = roi_threshold

    if bool_pre_trained_weights:
      self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(model)

  #Model trainning
  def train_model(self, train_set, batchsize = 128, lr = 0.00025, iteration = 200):

    self.cfg.DATASETS.TRAIN = (train_set,)
    self.cfg.DATALOADER.NUM_WORKERS = 2
    self.cfg.SOLVER.IMS_PER_BATCH = 16  
    self.cfg.SOLVER.BASE_LR = lr
    self.cfg.SOLVER.MAX_ITER = iteration    
    self.cfg.SOLVER.STEPS = []       
    self.cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = batchsize   
    self.cfg.MODEL.ROI_HEADS.NUM_CLASSES = 80  

    trainer = DefaultTrainer(self.cfg)
    trainer.resume_or_load(resume=False)
    trainer.train()

  #Model inferences
  def inferences(self, dataset_name):

    predictor = DefaultPredictor(self.cfg)
    evaluator = COCOEvaluator(dataset_name, self.cfg, False)
    val_loader = build_detection_test_loader(self.cfg, dataset_name)
    print(inference_on_dataset(predictor.model, val_loader, evaluator))

                                                                


