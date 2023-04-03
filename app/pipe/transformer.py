from pandas import DataFrame

from .base import BasePipePiece, build_pieces_from_module


class PipeTransformer(BasePipePiece):
    _pieces_attr = "transformers"
    
    def __call__(self, df: DataFrame) -> DataFrame:
        self.last = self.func(df)
        return self.last


def build_transformers(settings):
    return build_pieces_from_module(
        settings["PIPE_TRANSFORMERS_MODULE"],
        "imported.pipe_transformers",
        "pipe_transformer",
        PipeTransformer,
    )
