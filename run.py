from __future__ import division


import numpy as np
dataset_filename = "affinity_dataset.txt"
X = np.loadtxt(dataset_filename)
n_samples, n_features = X.shape
print("This dataset has {0} samples and {1} features".format(n_samples, n_features))
print(X[:1])
# The names of the features, for your reference.
features = ["action", "horror", "animated", "sci fi", "comedy"]
# First, how many rows contain our premise: that a person is buying apples
a_m_c = 0
h_m_c = 0
an_m_c = 0
s_m_c = 0
c_m_c = 0
for sample in X:
    if sample[0] == 1:  # This person chose action 0
        a_m_c += 1
    if sample[1] == 1:  # This person chose horror 1
        h_m_c += 1
    if sample[2] == 1:  # This person chose animated 2
        an_m_c += 1
    if sample[3] == 1:  # This person chose sci fi 3
        s_m_c += 1
    if sample[4] == 1:  # This person chose comedy 4
        c_m_c += 1
print("{0} people chose action movies".format(a_m_c))
print("{0} people chose horror movies".format(h_m_c))
print("{0} people chose animated movies".format(an_m_c))
print("{0} people chose sci fi movies".format(s_m_c))
print("{0} people chose comedy movies".format(c_m_c))


# How many of the cases that a person chose animated movies involved the people choosing sci fi too?
# Record both cases where the rule is valid and is invalid.
rule_valid = 0
rule_invalid = 0
for sample in X:
    if sample[1] == 1:  # This person chose sci fi
        if sample[4] == 1:
            # This person chose both sci fi and comedy
            rule_valid += 1
        else:
            # This person bought sci fi, but not comedy
            rule_invalid += 1
print("-----------------------------------------------------------------------------------")
print("{0} This person chose both sci fi and comedy cases of the rule being valid were discovered".format(rule_valid))
print("{0} This person bought sci fi, but not comedy cases of the rule being invalid were discovered".format(rule_invalid))


support = rule_valid  # The Support is the number of times the rule is discovered.
confidence = rule_valid / c_m_c
print("-----------------------------------------------------------------------------------")
print("The amount chosen both is {0} and the confidence is {1:.3f}.".format(support, confidence))
# Confidence can be thought of as a percentage using the following:
print("As a percentage, that is {0:.1f}%.".format(100 * confidence))











# Now we have all the information needed to compute Support and Confidence
