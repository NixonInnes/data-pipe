from pandas import DataFrame

from .base import BasePipePiece, build_pieces_from_module


class PipeCombiner(BasePipePiece):
    _pieces_attr = "combiners"
    
    def __call__(self, left: DataFrame, right: DataFrame) -> DataFrame:
        self.last = self.func(left=left, right=right)
        return self.last


def build_combiners(settings):
    return build_pieces_from_module(
        settings["PIPE_COMBINERS_MODULE"],
        "imported.pipe_combiners",
        "pipe_combiner",
        PipeCombiner,
    )
