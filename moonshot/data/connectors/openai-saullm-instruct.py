import logging
from typing import Any

from openai import AsyncOpenAI

from moonshot.src.connectors.connector import Connector, perform_retry
from moonshot.src.connectors.connector_endpoint_arguments import (
    ConnectorEndpointArguments,
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Connector class for SaulLM_Instruct model (a legal instruct-finetuned model)
class SaulLMInstruct(Connector):
    def __init__(self, ep_arguments: ConnectorEndpointArguments):
        # Initialize super class
        super().__init__(ep_arguments)

        # System prompts
        self._pre_prompt = ""
        self._post_prompt = ""

        # Model parameters
        self.temperature = ep_arguments.params.get("temperature", 0.01)
        self.max_tokens = ep_arguments.params.get("max_tokens", 2400)
        self.top_p = ep_arguments.params.get("top_p", 1)
        # self.top_k = ep_arguments.params.get("top_k", 1)
        self.num_return_sequences = ep_arguments.params.get("num_return_sequences", 1)
        self.stop_list = ep_arguments.params.get("stop_list", [])

        # Model api endpoint
        base_url, model_path = ep_arguments.uri.split("?model=")
        self.model_path = model_path
        self.client = AsyncOpenAI(base_url=base_url, api_key=self.token)

    @Connector.rate_limited
    @perform_retry
    async def get_response(self, prompt: str) -> str:
        """
        Retrieve and return a response in chat format WITHOUT output streaming.
        This method is used to retrieve a response, typically from an object or service represented by
        the current instance.

        Returns:
            str: retrieved response data
        """
        connector_prompt = f"{self.pre_prompt}{prompt}{self.post_prompt}"
        openai_request = [{"role": "user", "content": connector_prompt}]
        response = await self.client.chat.completions.create(
            model=self.model_path,
            stream=False,  # Disable output streaming for this model
            messages=openai_request,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            # top_k=self.top_k,
            stop=self.stop_list,
            n=self.num_return_sequences,
            timeout=self.timeout,
        )
        return await self._process_response(response)

    async def _process_response(self, response: Any) -> str:
        """
        Process an HTTP response and extract relevant information as a string.

        This function takes an HTTP response object as input and processes it to extract
        relevant information as a string. The extracted information may include data
        from the response body, headers, or other attributes.

        Args:
            response (OpenAIObject): An HTTP response object containing the response data.

        Returns:
            str: A string representing the relevant information extracted from the response.
        """
        # return response["choices"][0]["message"]["content"]
        # use the latest returned OpenAIObject format and remove leading whitespace
        # return response.choices[0].message.content.lstrip()
        return response.choices[0].message.content
