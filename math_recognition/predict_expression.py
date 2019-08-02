from PIL import Image
from math_recognition import preprocess, segment
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np

classifier = joblib.load("classifier_DecisionTree.pkl")

def predict_expression(expression_path):
    elements = segment.segment_image(expression_path)
    for el in elements:
        el.save_img()
        symbol_path = el.get_img_path()
        img_arr, img_features = prepare_for_predict(symbol_path)
        el.set_label(classifier.predict(img_features))
        el.delete_img()
    return elements


def prepare_for_predict(img_path):
    img_to_resize = Image.open(img_path).convert('L')
    preprocess.resize(img_to_resize)
    img_to_resize = preprocess.im_grayscale_to_binary(img_to_resize)
    img_to_resize = preprocess.fill_edges(img_to_resize)
    img_to_resize = img_to_resize.astype(np.uint8)
    hog_descriptors = hog(img_to_resize)
    hu_moments = []
    hu_moments.extend(hog_descriptors)
    return img_to_resize,[hu_moments]