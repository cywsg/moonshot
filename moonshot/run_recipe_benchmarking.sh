#! /usr/bin/bash

# Must run in Moonshot cli interactive mode

# # Link data folder
# CONNECTORS = "/path/to/your/connectors"
# RECIPES = "/path/to/your/recipes"
# COOKBOOKS = "/path/to/your/cookbooks"
# DATASETS = "/path/to/your/datasets"
# PROMPT_TEMPLATES = "/path/to/your/prompt-templates"
# METRICS = "/path/to/your/metrics"
# METRICS_CONFIG = "/path/to/your/metrics/metrics_config.json"
# CONTEXT_STRATEGY = "/path/to/your/context-strategy"
# RESULTS = "/path/to/your/results"
# DATABASES = "/path/to/your/databases"
# SESSIONS = "/path/to/your/sessions"

# run benchmarking using selected recipes
# Usage: run_recipe [-h] [-n NUM_OF_PROMPTS] name recipes endpoints
# run_recipe saullm-instruct-arc-balanced-acc-all "['arc-balanced-acc']" "['openai-saullm-instruct-endpoint']"
# run_recipe saullm-instruct-abercrombie "['legalbench/abercrombie']" "['openai-saullm-instruct-endpoint']"
run_recipe saullm-instruct-maud-knowledge-definition "['legalbench/maud-knowledge-definition']" "['openai-saullm-instruct-endpoint']"

