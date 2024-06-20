#! /usr/bin/bash

# Create batch recepies
DATASET=legalbench
RECIPE_DIR=./data/recipes

python src/utils/create_cookbook.py --dataset $DATASET --recipe_dir $RECIPE_DIR \
    --description "This is a cookbook that consists of a subset of datasets of LegalBench benchmark."