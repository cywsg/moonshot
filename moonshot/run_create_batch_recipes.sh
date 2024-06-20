#! /usr/bin/bash

# Create batch recepies
DATASET=legalbench
DATA_DIR=./data/datasets/legalbench
METRIC1=exactstrmatch
METRIC2=balancedaccuracy

python src/utils/create_batch_recipes.py --dataset $DATASET --data_dir $DATA_DIR --metrics $METRIC1  $METRIC2