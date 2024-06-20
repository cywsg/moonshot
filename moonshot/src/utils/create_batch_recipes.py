import argparse
# import json
import sys
import os

from typing import List

sys.path.insert(0, '../')

from moonshot.src.configs.env_variables import EnvironmentVars
from moonshot.api import (
    api_create_recipe,
    # api_create_cookbook,
    # api_create_endpoint,
    # api_create_recipe_executor,
    # api_create_cookbook_executor,
    # api_create_session,
    # api_get_session,
    # api_get_all_connector_type,
    # api_get_all_endpoint,
    # api_get_all_cookbook,
    # api_get_all_recipe,
    # api_get_all_executor,
    # api_get_all_session_detail,
    # api_get_all_prompt_template_detail,
    # api_get_all_context_strategy_name,
    # api_get_session_chats_by_session_id,
    # api_load_executor,
    api_set_environment_variables,
    # api_send_prompt,
    # api_update_context_strategy,
    # api_update_prompt_template,
)


def get_json_list(folder_path: List) -> List:
    """
    Obtain the list of JSON files in the specified folder.

    Args:
    - folder_path (str): The path to the folder containing the JSON files.

    Returns:
    - list: A list of JSON file names.
    """
    json_list = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.json'):
            json_list.append(file_name)
    return json_list


def create_batch_recepices(
        dataset: str,
        data_folder: str,
        metrics: List[str]
) -> None:
    """
    Generate a recepie for each dataset in the specified folder and save it to another folder.

    Args:
    - dataset_folder (str): The path to the folder containing the datasets.
    """
    # Get list of datasets
    json_list = get_json_list(data_folder)
    # json_list.sort()  # sort the list in alphabetical order

    # Iterate over dataset JSON files
    for file in json_list:
        dataset_name = os.path.splitext(file)[0]  # Extract filename without extension
        dataset_prompt = f"{dataset}/{dataset_name}"  # include the folder to store datasets and prompts

        # Create recepice
        api_create_recipe(
            name=dataset_name,
            description="",
            tags=[],
            datasets=[dataset_prompt],
            prompt_templates=[dataset_prompt],
            metrics=metrics
        )


def parse_arguments():
    """
    A function to parse arguments and return the parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Script to process input arguments")
    parser.add_argument("--dataset", type=str, help="Dataset to process", required=True)
    parser.add_argument("--data_dir", type=str, help="Path to the dataset directory", required=True)
    # parser.add_argument("--save_dir", type=str, help="Path to save the transformed dataset", required=True)
    parser.add_argument("--metrics", nargs="+", type=str, help="Evaluation metrics", required=True)
    return parser.parse_args()


if __name__ == "__main__":
    # Parse arguments
    args = parse_arguments()

    # Set environment variables
    # print(f"Current path: {os.getcwd()}")
    moonshot_path = "../moonshot/data/"

    env = {
        # "CONNECTORS_ENDPOINTS": os.path.join(moonshot_path, "connectors-endpoints"),
        # "CONNECTORS": os.path.join(moonshot_path, "connectors"),
        "RECIPES": os.path.join(moonshot_path, f"recipes/{args.dataset}"),
        # "COOKBOOKS": os.path.join(moonshot_path, "cookbooks"),
        "DATASETS": os.path.join(moonshot_path, f"datasets/{args.dataset}"),
        # "PROMPT_TEMPLATES": os.path.join(moonshot_path, "prompt-templates"),
        # "METRICS": os.path.join(moonshot_path, "metrics"),
        # "METRICS_CONFIG": os.path.join(moonshot_path, "metrics/metrics_config.json"),
        # "CONTEXT_STRATEGY": os.path.join(moonshot_path, "context-strategy"),
        # "RESULTS": os.path.join(moonshot_path, "results"),
        # "DATABASES": os.path.join(moonshot_path, "databases"),
        # "SESSIONS": os.path.join(moonshot_path, "sessions"),
    }

    api_set_environment_variables(env)
    print(f"Recipe folder: {EnvironmentVars.RECIPES}")

    # Create recepices
    create_batch_recepices(
        dataset=args.dataset,
        data_folder=args.data_dir,
        metrics=args.metrics
    )

# Example:
# In moonshot folder:
# python -m moonshot.utils.create_batch_recipes --dataset legalbench --data_dir ./data/datasets/legalbench \
#   --metrics exactstrmatch balancedaccuracy
