"""OpenAI-compatible schemas for model discovery."""

from typing import Literal

from mlflow.gateway.base_models import ResponseModel


class Model(ResponseModel):
    id: str
    object: Literal["model"] = "model"
    created: int
    owned_by: str


class ListModelsResponse(ResponseModel):
    object: Literal["list"] = "list"
    data: list[Model]
