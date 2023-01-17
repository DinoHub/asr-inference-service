import logging
from nemo.core.config import hydra_runner
from typing import Any, List, Optional, Union

from config import TranscriptionConfig
import torch

from nemo.collections.asr.models import ASRModel
from nemo.utils import model_utils
import pytorch_lightning as pl

import gradio as gr

inputs: List[Union[str, gr.components.Component]] = ["text"]
outputs: List[Union[str, gr.components.Component]] = ["text"]

examples: Optional[Union[List[Any], List[List[Any]], str]] = None

@hydra_runner(config_name="TranscriptionConfig", schema=TranscriptionConfig)
def initialize_asr_model(cfg: TranscriptionConfig) -> TranscriptionConfig:

    map_location = 

    model_cfg = ASRModel.restore_from(restore_path=cfg.model_path, return_config=True)
        classpath = model_cfg.target  # original class path
        imported_class = model_utils.import_class_by_path(classpath)  # type: ASRModel
        logging.info(f"Restoring model : {imported_class.__name__}")
        asr_model = imported_class.restore_from(
            restore_path=cfg.model_path, map_location=map_location,
        )


def predict(name: str) -> str:
    # TODO: Implement this!
    return f"Hello {name}"
