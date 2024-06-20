#! /usr/bin/bash

# # Run benchmarking
# TYPE=recipe
# DATASET_NAME=legalbench
# RECIPES=$DATASET_NAME/citation-prediction-classification
# ENDPOINTS=openai-saullm-instruct-endpoint

# python benchmarking_2.py --type $TYPE --dataset_name $DATASET_NAME --inputs $RECIPES --endpoints $ENDPOINTS


# Run benchmarking
INPUT_TYPE=cookbook
DATASET_NAME=legalbench
COOKBOOKS=legalbench-cookbook
ENDPOINTS=openai-saullm-instruct-endpoint

python benchmarking.py --input_type $INPUT_TYPE --dataset_name $DATASET_NAME --inputs $COOKBOOKS --endpoints $ENDPOINTS
