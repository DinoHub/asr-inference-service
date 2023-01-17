from typing import Optional
from dataclasses import dataclass

from pydantic import BaseSettings, Field

from nemo.collections.asr.metrics.wer import CTCDecodingConfig
from nemo.collections.asr.metrics.rnnt_wer import RNNTDecodingConfig
from nemo.collections.asr.modules.conformer_encoder import ConformerChangeConfig

@dataclass
class ModelChangeConfig:

    # Sub-config for changes specific to the Conformer Encoder
    conformer: ConformerChangeConfig = ConformerChangeConfig()

@dataclass
class TranscriptionConfig:
    # Required configs
    model_path: Optional[str] = '../models/stt_en_conformer_ctc_large.nemo'  # Path to a .nemo file

    # General configs
    output_filename: Optional[str] = None
    batch_size: int = 1
    num_workers: int = 0
    append_pred: bool = False  # Sets mode of work, if True it will add new field transcriptions.
    pred_name_postfix: Optional[str] = None  # If you need to use another model name, rather than standard one.
    random_seed: Optional[int] = None  # seed number going to be used in seed_everything()

    # Set to True to output greedy timestamp information (only supported models)
    compute_timestamps: bool = False

    # Set to True to output language ID information
    compute_langs: bool = False

    # Set `cuda` to int to define CUDA device. If 'None', will look for CUDA
    # device anyway, and do inference on CPU only if CUDA device is not found.
    # If `cuda` is a negative number, inference will be on CPU only.
    cuda: Optional[int] = None
    amp: bool = False
    audio_type: str = "wav"

    # Recompute model transcription, even if the output folder exists with scores.
    overwrite_transcripts: bool = True

    # Decoding strategy for CTC models
    ctc_decoding: CTCDecodingConfig = CTCDecodingConfig()

    # Decoding strategy for RNNT models
    rnnt_decoding: RNNTDecodingConfig = RNNTDecodingConfig(fused_batch_size=-1)

    # decoder type: ctc or rnnt, can be used to switch between CTC and RNNT decoder for Joint RNNT/CTC models
    decoder_type: Optional[str] = None

    # Use this for model-specific changes before transcription
    model_change: ModelChangeConfig = ModelChangeConfig()

class BaseConfig(BaseSettings):
    """Define any config here.

    See here for documentation:
    https://pydantic-docs.helpmanual.io/usage/settings/
    """
    # KNative assigns a $PORT environment variable to the container
    port: int = Field(default=8080, env="PORT",description="Gradio App Server Port")
