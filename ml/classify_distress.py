import numpy as np
from PIL import Image



# Supervised
def naive_bayes_learner(X, y):
    from sklearn.naive_bayes import MultinomialNB
    return MultinomialNB().fit(X,y)

def gaussianNB_learner(X, y):
    from sklearn.naive_bayes import GaussianNB
    return GaussianNB().fit(X,y)

def tree_learner(X, y):
    from sklearn import tree
    return tree.DecisionTreeRegressor().fit(X,y)

def sgdClassifier_learner(X, y):
    from sklearn.linear_model import SGDClassifier
    return SGDClassifier(loss="hinge", penalty="l2").fit(X,y)

def svm_learner(X, y):
    from sklearn import svm
    return svm.SVC().fit(X,y)

def knn_learner(X, y):
    from sklearn.neighbors import KNeighborsClassifier
    neigh = KNeighborsClassifier(n_neighbors=3)
    return neigh.fit(X, y)


with open('results.txt', 'rb') as f:
    lines = f.read().split('\n')

# files = [[int(x) for x in list('100101011')] for l in lines]
files = [l.split(' ')[0] for l in lines]
labels = [int(l.split(' ')[1]) for l in lines]

print files
print labels

examples = []
size = (50, 50)
avg = lambda x : int(round(1.0*sum(x)/len(x)))
imgdir = '../bing_facecrop/cropped_faces/'
for f in files:
    im = Image.open(imgdir+f)
    im = im.resize(size)
    pixels = list(im.getdata())
    intensities = [avg(p) for p in pixels]

    example = []
    for num in intensities:
        part = bin(num)[2:]
        part = '0'*(8-len(part)) + part
        example += [int(x) for x in list(part)]

    print len(example), example[0]
    examples.append(example)
examples = np.array(examples)



# clf = naive_bayes_learner(examples[:3], labels[:3])
clf = knn_learner(examples[:3], labels[:3])
print clf.predict_proba(examples)
