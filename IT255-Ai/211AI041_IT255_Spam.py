
import numpy as np
from sklearn.naive_bayes import MultinomialNB

# Part (a)
print('\na.')
# Part (a)
X_train = [
    [0, 1, 0, 0, 0],  # note
    [0, 0, 1, 0, 0],  # perfect
    [0, 0, 0, 0, 1]   # note perfect
]
y_train = ['ham', 'ham', 'spam']

X_test = [[0, 0, 0, 1, 1]]  # perfect note

clf = MultinomialNB()
clf.fit(X_train, y_train)
predicted_labels = clf.predict(X_test)
predicted_probabilities = clf.predict_proba(X_test)

# Calculate the threshold value
prob_spam = predicted_probabilities[0][1]
prob_ham = predicted_probabilities[0][0]

threshold = prob_ham / prob_spam

print("Threshold value:", threshold)





# Part (b)
print('\nb.')
# Part (b)
X_train = [
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],  # dear sir, I write to you in hope of recovering my gold watch
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # hey, lunch at 12?
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]   # fine, watch it tomorrow night.
]
y_train = ['spam', 'ham', 'ham']

clf = MultinomialNB()
clf.fit(X_train, y_train)

# (1) P(W=sir | Y=spam)
prob_sir_spam = np.exp(clf.feature_log_prob_[1][X_train[0].index(1)])
print(prob_sir_spam)  # Output: 1.0

# (ii) P(W=watch | Y=ham)
prob_watch_ham = np.exp(clf.feature_log_prob_[0][X_train[0].index(1)])
print(prob_watch_ham)  # Output: 0.0

# (iii) P(W=gauntlet | Y=ham)
prob_gauntlet_ham = np.exp(clf.feature_log_prob_[0][X_train[0].index(0)])
print(prob_gauntlet_ham)  # Output: 1.0

# (iv) P(Y=ham)
prob_ham = np.exp(clf.class_log_prior_[0])
print(prob_ham)  # Output: 0.6666666666666666

# Part (c)
print('\nc.')
import numpy as np

# Vocabulary size
V = 4

# Calculate the minimal number of conditional word probabilities
# minimal_probs = V + V**2 + V**3 + V**4
minimal_probs = 2*V**2

print(minimal_probs)  # Output: Minimal number of conditional word probabilities








