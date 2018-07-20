# **Wild Mask Database**

A database built to study the problem of unconstrained spoofing recognition.

## Requirements

* Python
* Gnuplot

## How to submit my results

To submit your results, all you have to do is to create a folder with the name you wish to be shown on the roc curve file. This folder must have two files `"negatives.txt"` and `"positives.txt"`. Those are the scores returned from your application for negative fake and real images, respectively.

Then, you run:

```
$ ./regen_roc_curve.sh
```

That's it!
