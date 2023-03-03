from pandas import DataFrame

from .base import BasePipePiece, pipe_piece_constructor
from .utils import load_module_from_file, camelcase


class PipeCombiner(BasePipePiece):
    def __call__(self, left: DataFrame, right: DataFrame) -> DataFrame:
        self.last = self.func(left=left, right=right, **self.config)
        return self.last


def build_combiners():
    module = load_module_from_file("app/imports/pipe_combiners.py", "imported.pipe_combiners")
    return {
        camelcase(func.__name__): pipe_piece_constructor(PipeCombiner, func) 
        for func in [getattr(module, f) for f in dir(module) if f.startswith("pipe_combiner")]
    }
