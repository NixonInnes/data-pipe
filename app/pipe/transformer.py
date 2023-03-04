from pandas import DataFrame

from app import settings
from .base import BasePipePiece, build_pieces_from_module


class PipeTransformer(BasePipePiece):
    def __call__(self, df: DataFrame) -> DataFrame:
        self.last = self.func(df)
        return self.last


def build_transformers():
    # module = utils.load_module_from_file(settings.get("PIPE_TRANSFORMER_MODULE"), "imported.pipe_transformers")
    # return {
    #     utils.camelcase(func.__name__): pipe_piece_constructor(PipeTransformer, func) 
    #     for func in [getattr(module, f) for f in dir(module) if f.startswith("pipe_transformer")]
    # }
    return build_pieces_from_module(
        settings.get("PIPE_TRANSFORMER_MODULE"),
        "imported.pipe_transformers",
        "pipe_transformer",
        PipeTransformer
    )
