from classifier_build import load_data
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

train_data_path = "../data/handwritten_images/train"
test_data_path = "../data/handwritten_images/test"

features, labels = load_data.get_labels_and_features(train_data_path)
test_features, test_labels = load_data.get_labels_and_features(test_data_path)

classifier = DecisionTreeClassifier()
fit = classifier.fit(features,labels)
score = classifier.score(test_features, test_labels)
joblib.dump(classifier, "classifier_DecisionTree.pkl")
print(score)

