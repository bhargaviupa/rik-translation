#!/usr/bin/env python3
"""Train the digit classifier: seed (reader's digit sheets, augmented) + self-labelled book glyphs + junk class (10).
usage: train.py SEED.npz BOOK_GLYPHS.npz OUT.pkl"""
import sys, numpy as np, cv2, pickle
from sklearn.svm import SVC
rng = np.random.default_rng(0)
def feat(A): return np.array([cv2.GaussianBlur(x, (3, 3), 0).ravel() / 255. for x in A], dtype=np.float32)
def aug(im):
    a = im.copy(); k = rng.integers(0, 3)
    if k == 1: a = cv2.dilate(a, np.ones((2, 2), np.uint8))
    if k == 2: a = cv2.erode(a, np.ones((2, 2), np.uint8))
    M = cv2.getRotationMatrix2D((16, 16), rng.uniform(-7, 7), rng.uniform(.9, 1.1)); a = cv2.warpAffine(a, M, (32, 32))
    a = cv2.GaussianBlur(a, (3, 3), rng.uniform(0, 1.2))
    return np.clip(a.astype(float) + rng.normal(0, 12, a.shape), 0, 255).astype(np.uint8)
s = np.load(sys.argv[1]); SX, SY = s['X'], s['y']
b = np.load(sys.argv[2]); BX, BM = b['X'], b['M']
Xs, ys = [], []
for c in range(10):
    for i in rng.choice(np.where(SY == c)[0], 400, replace=False): Xs.append(aug(SX[i])); ys.append(c)
seed = SVC(C=5, probability=True, random_state=0).fit(feat(Xs), ys)
# self-label book glyphs
asp = BM[:, 6] / np.maximum(BM[:, 7], 1)
P = seed.predict_proba(feat(BX)); pred, cf = P.argmax(1), P.max(1)
good = (cf > 0.5) & (asp > 0.45) & (asp < 1.6)
junk = (asp < 0.4) | (cf < 0.25) | (BM[:, 7] < 14)
sel_d = np.where(good)[0]; sel_j = np.where(junk & ~good)[0]
cap = 700
Xt, yt = list(Xs), list(ys)
for c in range(10):
    ids = sel_d[pred[sel_d] == c]
    for i in rng.choice(ids, min(cap, len(ids)), replace=False): Xt.append(BX[i]); yt.append(c)
for i in rng.choice(sel_j, min(1500, len(sel_j)), replace=False): Xt.append(BX[i]); yt.append(10)
clf = SVC(C=5, probability=True, random_state=0).fit(feat(Xt), yt)
pickle.dump(clf, open(sys.argv[3], 'wb'))
print('trained on', len(yt), 'samples; book digits per class', [int((pred[sel_d] == c).sum()) for c in range(10)], 'junk', len(sel_j))
