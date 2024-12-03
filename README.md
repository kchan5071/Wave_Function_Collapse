# Wave Function Collapse

based off of [this algorithm], implemented in python

## Algorithm Steps
 - parse Image in Assets folder into NxN squares
 - create rotation variations
 - determine edge hex values
 - initialize empty map filled with nodes that have null edges
 - collapse states and propagate until done

### Collapsing States
* find the node with the lowest entropy(number of possible states)
* if there is more than 1 possible state, pick one at random


### Propagating change
* change edges on nearby neighbors
* prune invalid states based on those edges


## Required Packages
* PIL
* numpy
* opencv(used for image manipulation)

## How to run
* put the input image in the /Assets folder
* run main.py script with optional arguments

## Arguments
* -n (pattern size, default = 16)
* -o (output path, default is current working directory)
* -i (input path, default is /Assets)
* -s (size of the output image, default = 5)
* -v (view the output image, default = False)
* -p (print debug info, default - False)

[this algorithm]: https://github.com/mxgmn/WaveFunctionCollapse 

