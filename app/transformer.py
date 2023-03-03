from pandas import DataFrame

from .base import BasePipePiece, pipe_piece_constructor
from .utils import load_module_from_file, camelcase


class PipeTransformer(BasePipePiece):
    def __call__(self, df: DataFrame) -> DataFrame:
        self.last = self.func(df, **self.config)
        return self.last


def build_transformers():
    module = load_module_from_file("app/imports/pipe_transformers.py", "imported.pipe_transformers")
    return {
        camelcase(func.__name__): pipe_piece_constructor(PipeTransformer, func) 
        for func in [getattr(module, f) for f in dir(module) if f.startswith("pipe_transformer")]
    }
