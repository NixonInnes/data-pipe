from pandas import DataFrame

from app import settings
from .base import BasePipePiece, build_pieces_from_module


class PipeOutlet(BasePipePiece):
    def __call__(self, df: DataFrame) -> None:
        self.func(df)


def build_outlets():
    # module = utils.load_module_from_file(settings.get("PIPE_OUTLET_MODULE"), "imported.pipe_outlets")
    # return {
    #     utils.camelcase(func.__name__): pipe_piece_constructor(PipeOutlet, func) 
    #     for func in [getattr(module, f) for f in dir(module) if f.startswith("pipe_outlet")]
    # }
    return build_pieces_from_module(
        settings.get("PIPE_OUTLET_MODULE"),
        "imported.pipe_outlets",
        "pipe_outlet",
        PipeOutlet
    )
