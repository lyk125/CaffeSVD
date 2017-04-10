import numpy as np
import sys
from base import *

if len(sys.argv) == 1:
    PREDICT_FILENAME = "net_normal.npy"
else:
    PREDICT_FILENAME = sys.argv[1]

print ("Compare with Real Label and %s" % PREDICT_FILENAME)

num_kinds = 10
pre   = np.load(PREDICT_FILENAME)
label = np.load("label.npy")
n = len(label)

for k in range(num_kinds):
    print ("Kind: %d" % k)
    eval_result(label, pre, k)
    print ("========")

acc = np.sum(pre == label) * 1.0 / n
print ("Total Accuracy: %f", acc)
