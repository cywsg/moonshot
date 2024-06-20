import argparse
import asyncio
import os
import sys

from typing import List

sys.path.insert(0, "../")

from moonshot.api import (
    api_create_recipe_executor,
    api_create_cookbook_executor,
    api_set_environment_variables,
)


async def async_run_benchmarking(
    dataset_name: str,
    input_type: str,
    inputs: List[str],
    endpoints: List[str],
    num_prompts: int = 0,
):
    """
    A coroutine that runs benchmarking for different APIs based on input_type (either recipes or cookbooks).

    Args:
        input_type (str): The type of API to benchmark, either "recipe" or "cookbook".
        inputs (List[str]): List of input data (recipes or cookbooks) for the benchmarking.
        endpoints (List[str]): List of API endpoints to test.
        num_prompts (int): Number of prompts to run for each API call.
    """
    executor_func = {
        "recipe": api_create_recipe_executor,
        "cookbook": api_create_cookbook_executor,
    }.get(input_type, None)

    if executor_func is None:
        print("Error: the input_type must be either 'recipe' or 'cookbook'.")
        return

    executor = executor_func(
        f"executor of {dataset_name}",
        inputs,
        endpoints,
        num_prompts,
    )
    await executor.execute()
    executor.close_executor()


def parse_arguments():
    """
    A function to parse arguments using argparse and return the parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Run API and show results")
    parser.add_argument(
        "--input_type",
        type=str,
        choices=["recipe", "cookbook"],
        required=True,
        help="Choose the type of task (recipe or cookbook)",
    )
    parser.add_argument(
        "--dataset_name",
        type=str,
        required=True,
        help="Dataset where the recipes or cookbooks created from",
    )
    parser.add_argument(
        "--inputs", nargs="+", required=True, help="A list of recipes or cookbooks"
    )
    parser.add_argument(
        "--endpoints", nargs="+", required=True, help="A list of endpoints to use"
    )
    parser.add_argument(
        "--num_prompts",
        type=int,
        default=0,
        required=False,
        help="Number of prompts (samples) to use",
    )
    return parser.parse_args()


async def main():
    """
    A function that serves as the main entry point.
    It parses arguments, sets up the environment variables, and runs benchmarking asynchronously.
    """
    args = parse_arguments()
    print(args)

    moonshot_path = "../moonshot/data/"
    env = {
        f"{name.upper()}": os.path.join(moonshot_path, f"{name.lower()}")
        for name in [
            "connectors-endpoints",
            "connectors",
            "recipes",
            "cookbooks",
            "datasets",
            "prompt-templates",
        ]
    }
    api_set_environment_variables(env)

    await async_run_benchmarking(
        args.dataset_name,
        args.input_type,
        args.inputs,
        args.endpoints,
        args.num_prompts,
    )


asyncio.run(main())

# Example:
# python benchmarking.py --input_type recipe --dataset_name legalbench --inputs citation-prediction-classification \
#  --endpoints openai-saullm-instruct-endpoint

# python benchmarking.py --input_type cookbook --dataset_name legalbench --inputs legalbench-cookbook \
#  --endpoints openai-saullm-instruct-endpoint
