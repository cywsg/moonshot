import argparse
import sys
import os

from typing import Any, List

sys.path.insert(0, '../')

from moonshot.src.configs.env_variables import EnvironmentVars
from moonshot.api import (
    # api_create_recipe,
    api_create_cookbook,
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


def create_cookbook(name: str, description: str, recipe_dir: str) -> None:
    """
    Generate a cookbook for all recipes in the specified folder.

    Args:
    - dataset_folder (str): The path to the folder containing the datasets.
    """

    # Get list of recipes
    recipes_list = get_json_list(f"{recipe_dir}/{name}")
    recipes_list.sort()
    print(recipes_list)
    recipes = [f"{name}/{os.path.splitext(file)[0]}" for file in recipes_list]

    # Create recepice
    api_create_cookbook(
        name=name,
        description=description,
        recipes=recipes
    )


def parse_arguments():
    """
    A function to parse arguments and return the parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Script to process input arguments")
    parser.add_argument("--dataset", type=str, help="Dataset to process", required=True)
    parser.add_argument("--description", type=str, help="Description of cookbook", required=False)
    parser.add_argument("--recipe_dir", type=str, help="Path to the recipe directory", required=True)
    return parser.parse_args()


if __name__ == "__main__":
    # Parse arguments
    args = parse_arguments()

    if args.description is None:
        description = f"This is a cookbook that consists of (a subset of) datasets of {args.dataset} benchmark."

    # Create cookbook
    create_cookbook(
        name=args.dataset,
        description=args.description,
        recipe_dir=args.recipe_dir
    )

# Example:
# In moonshot folder:
# python -m moonshot.utils.create_cookbook --dataset LegalBench --recipe_dir ./data/recipes/legalbench \
#   --description "Cookbook for legalbench dataset"
