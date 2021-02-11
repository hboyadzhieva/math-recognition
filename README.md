# math-recognition

*The project is created at school for learning purposes*

## Getting Started
### Prerequisites
 External Libraries needed:
  - PyQt5
  - PIL
  - sklearn
  - skimage
  
### How to Start
***Note! The project creates and deletes png files on the file system in the current project directory***
1. Clone project and make sure to keep directory structure (*./data/segmented* will be used by the project)
2. Install needed external libraries
3. Run main.py

## Description
### Gui
Symbols recognized
 - digits [0,1,2,3,4,5,7,8,9]
 - operators [+,-]
 - division line 
 
Buttons
- **Submit** button will send the image for prediction and will display the separate symbols in order from top-most element on the bottom right window.
- **Make expression** button will display the whole expression on the bottom left window.
- **Pen** and **Eraser** switch between pen and eraser on the canvas depending on which one is clicked last. If a symbol is not recognized correctly it can be deleted and drawn again to reconstruct the expression.
.
### Source 
**math_recognition** subfolder holds all the source files needed for the program to run and the pickled classifier file 
 - **gui_layout.py** - description of the main user interface window, all widgets, text boxes, buttons, their positioning and style
 - **gui_functionality.py** - connect the windows and widgets to events - draw on canvas, clear canvas, erase, send expression for recognition
 - **make_expression.py** - functions that construct the text expression - using the elements on the image and their positioning, decides where the parantheses need to be added, which part of the expression is above the division line and which below, which element is operand and which element is digit
 - **segment.py** - segments the image into separate elements by going through connected black pixels and fixing a square around them
 - **preprocess.py** - functions for preprocessing of the images like conversion to grayscale and binary images and resizing in order for the input images to resemble the classifier's training set
 - **predict_expressions** - functions to link the segmentation, preprocess, and making of expression
 
 ### Additional - creating the classifier_DecisionTree.pkl
The data set used for the classificator is from Kaggle:  https://www.kaggle.com/xainano/handwrittenmathsymbols
 
Data was kept in directories - **data/handwritten_images/test** and **data/handwritten_images/train**. In each of them there were subdirectories for each symbol - '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+' and '-'. In **test** subdirectories I kept 70% of the images, and in **train** 30% of the images.

Here, in subdirectory **classifier_build** are the source files for creating the test and train features and labels for building and testing the decision tree classifier.

For feature set, after testing with image moments, pixel values, hu moments, the feature set that gave the best result was the HOG descriptors. HOG (histogram of oriented gradients) is a technique that counts occurrences of gradient orientation in localized portions of an image.

After loading the images, test feature set and train feature set, the classifier was tested and dumped in a pkl file. This pkl file **classifier_DecisionTree.pkl** is then loaded by the main program and used to predict the values of the drawn images. 

***Note! The files in subdirectory classifier_build are just for reference of how the classifier was created. The train and test data is not uploaded in this repository.***
