from pandas import DataFrame

from .base import BasePipePiece, build_pieces_from_module


class PipeOutlet(BasePipePiece):
    _pieces_attr = "outlets"
    
    def __call__(self, df: DataFrame) -> None:
        self.func(df)


def build_outlets(settings):
    return build_pieces_from_module(
        settings["PIPE_OUTLETS_MODULE"],
        "imported.pipe_outlets",
        "pipe_outlet",
        PipeOutlet,
    )
