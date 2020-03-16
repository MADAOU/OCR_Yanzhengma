import os
import cv2
import pickle as pk
from sklearn.neighbors import KNeighborsClassifier as knn


def img2vec(file_path):
    '''将图片转为向量'''
    if isinstance(file_path, str):
        img = cv2.imread(file_path)
    else:
        img = file_path
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    temp = cv2.resize(gray, (30, 30))
    vec = temp.ravel()
    return vec


tarin_img_path = 'train_data_img'


def split_data(paths):
    X = []
    y = []
    for i in os.listdir(tarin_img_path):
        path = os.path.join(tarin_img_path, i)
        fn_list = os.listdir(path)
        for name in fn_list:
            y.append(i)
            X.append(img2vec(os.path.join(path, name)))
    return X, y                 # x向量   y标签


def knn_clf(X_train, label):
    '''构建分类器'''
    clf = knn(n_neighbors=6, algorithm='auto', weights='distance', n_jobs=4)
    clf.fit(X_train, label)
    return clf


def knn_shib(test_img):
    with open('model.pkl', 'rb')as f:
        clf = pk.load(f)
    result = clf.predict([img2vec(test_img)])
    return result


def train():
    X_train, y_label = split_data(tarin_img_path)
    clf = knn_clf(X_train, y_label)
    with open('model.pkl', 'wb') as f:
        pk.dump(clf, f)
