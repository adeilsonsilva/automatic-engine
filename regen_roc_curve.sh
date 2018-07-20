#!/usr/bin/env bash

for FOLDER_NAME in $(ls -1d */ | egrep -v "example" | sed 's/\///'); do
    cp "./$FOLDER_NAME/negatives.txt" .
    cp "./$FOLDER_NAME/positives.txt" .
    python scores_to_roc_values.py
    cp "roc_values.txt" "./$FOLDER_NAME/"
    rm negatives.txt positives.txt roc_values.txt
    echo "    \"$FOLDER_NAME/roc_values.txt\" using 1:2 with lines title \"$FOLDER_NAME\",\\" >> roc_curve.gplot
    gnuplot roc_curve.gplot
done

