import glob
import os

import nbconvert
import nbformat

# convert all notebooks to HTML
# then call this script from a Jekyll plugin

# get all notebooks
nb_files = glob.glob('notebooks/*.ipynb')

for nbf in nb_files:
    # read structured notebook file
    nb = nbformat.read(nbf,as_version=4)
    # assume the first cell as the post title on one line 
    # and the post date on the next line