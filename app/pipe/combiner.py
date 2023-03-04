from pandas import DataFrame

from app import utils, settings

from .base import BasePipePiece, build_pieces_from_module


class PipeCombiner(BasePipePiece):
    def __call__(self, left: DataFrame, right: DataFrame) -> DataFrame:
        self.last = self.func(left=left, right=right)
        return self.last


def build_combiners():
    return build_pieces_from_module(
        settings.get("PIPE_COMBINER_MODULE"), 
        "imported.pipe_combiners", 
        "pipe_combiner", 
        PipeCombiner
    )
