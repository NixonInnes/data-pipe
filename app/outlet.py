from pandas import DataFrame

from .base import BasePipePiece, pipe_piece_constructor
from .utils import load_module_from_file, camelcase


class PipeOutlet(BasePipePiece):
    def __call__(self, df: DataFrame) -> None:
        self.func(df, **self.config)


def build_outlets():
    module = load_module_from_file("app/imports/pipe_outlets.py", "imported.pipe_outlets")
    return {
        camelcase(func.__name__): pipe_piece_constructor(PipeOutlet, func) 
        for func in [getattr(module, f) for f in dir(module) if f.startswith("pipe_outlet")]
    }
