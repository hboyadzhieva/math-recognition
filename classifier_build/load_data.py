from os import listdir, walk
from math_recognition import preprocess
from skimage.feature import hog


def get_file_extension(str_path):
    return str_path[str_path.index('.')+1:]

# --- The function extracts the labels and features of train and test data ---
# --- Labels are the names of the subfolders - '1', '-', '2', etc, where data images are stored ---
# --- The features are the computed hog descriptors of the images ---
# --- hog - occurrences of gradient orientation in localized portions of an image. ---
def get_labels_and_features(folder_path):
    # listdir returns the names of the subfolders in a directory
    all_labels = []
    all_features = []
    subfolders = listdir(folder_path)

    #iterate over subfolders, create paths for them
    for subfolder in subfolders:
        subpath = folder_path + "/" + subfolder
        #os walk returns array of size 3 - first element is path name, second names of folders, and third name of files.
        #since I need the images I will access only the [2] elements
        for img_arr in walk(subpath):
            for img_file in img_arr[2]:
                if(get_file_extension(img_file) in ['jpg', 'png', 'jpeg']):
                    img_path = subpath + "/" + img_file
                    binary_img = preprocess.grayscale_to_binary(img_path)
                    hog_descriptors = hog(binary_img)
                    label = subpath[-1:]
                    all_features.append(hog_descriptors)
                    all_labels.append(label)

    return all_features, all_labels




