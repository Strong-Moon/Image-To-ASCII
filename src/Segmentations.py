import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation
import torch, torchvision
from detectron2.engine.defaults import DefaultPredictor
from adet.config import get_cfg

class HumanSegmenter: 
    
    def human_selection(image):
        BG_COLOR = (0, 0, 0) # black
        MASK_COLOR = (255, 255, 255) # white
        with mp_selfie_segmentation.SelfieSegmentation(model_selection = 0) as selfie_segmentation:
            for idx, file in enumerate([image]):
                image_height, image_width, _ = image.shape
                results = selfie_segmentation.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
                foreground_image = np.zeros(image.shape, dtype=np.uint8)
                foreground_image[:] = MASK_COLOR
                background_image = np.zeros(image.shape, dtype=np.uint8)
                background_image[:] = BG_COLOR
                output_image = np.where(condition, image, background_image)
                # cv2.imwrite('D:/Visual_Studio_Project/Python/ASCII/' + str(idx) + '.png', output_image)
        return output_image

class AnimationSegmenter:

    def __init__(self):
        CONFIG_FILENAME  = "./conf/SOLOv2.yaml"
        MODEL_FILENAME  = "./conf/model_final.pth"
        cfg = get_cfg()
        cfg.merge_from_file(CONFIG_FILENAME)
        cfg.MODEL.WEIGHTS = MODEL_FILENAME 
        cfg.MODEL.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
        cfg.freeze()
        self.model = DefaultPredictor(cfg)
        self.model.score_threshold = 0.1
        self.model.mask_threshold = 0.5
    
    def run(self, image):
        preds = self.model(image)
        mask = preds['instances'].pred_masks.cpu().numpy().astype(int).max(axis=0)
        output = image.copy()[:, :, ::-1]
        output[mask == 0] = 0
        return output

    