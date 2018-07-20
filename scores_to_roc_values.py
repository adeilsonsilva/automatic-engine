# This short program reads two data files called "positives.txt" and "negatives.txt"
# then we parse this file to calculate TPR and FPR, saving the results to "roc_values.txt"
import collections

# Python builtin "range" function does not accept floats
# Loops from start to stop (inclusive) with a step increment
# @param start  number  Number to start from
# @param stop   number  Number to stop at (inclusive)
# @param step   number  Number to be used as increment
def my_range(start, stop, step = 1.0):
    while start < (stop+step): # The way Python handles float numbers forbids "<=" usage
        yield start
        start +=step

# Wrapper function just to return a list
# @param start  number  Number to start from
# @param stop   number  Number to stop at (inclusive)
# @param step   number  Number to be used as increment
# @return       list    List of numbers
def frange(start, stop, step = 1.0):
    return list(my_range(start, stop, step))

# Read file with positive scores
p = []
with open("positives.txt") as f:
    p = [ line.strip("\n") for line in f.readlines() ]

# Read file with negative scores
n = []
with open("negatives.txt") as f:
    n = [ line.strip("\n") for line in f.readlines() ]

POSITIVE_SAMPLES = len(p)
NEGATIVE_SAMPLES = len(n)

# Create dicts with count of occurrences for each score
positives_counter = collections.Counter(x for x in p)
negatives_counter = collections.Counter(x for x in n)

# Open output file
result_file = open("roc_values.txt", "w")

# Loop through thresholds (0 to 1)
for threshold in frange(0, 1, 0.05):
    TP = 0
    FP = 0

    # Count how many scores are greater than current threshold
    for score in positives_counter.keys():
        TP += positives_counter[score] if float(score) >= threshold else 0
    for score in negatives_counter.keys():
        FP += negatives_counter[score] if float(score) >= threshold else 0

    # Calculate the rate, dividing the counter for amount of samples
    TPR = TP / POSITIVE_SAMPLES
    FPR = FP / NEGATIVE_SAMPLES

    # Print to file
    result = "{0:.5f} {1:.5f}\n".format(FPR, TPR)
    result_file.write(result)
    
result_file.close()
