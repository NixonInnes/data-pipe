from .base import BasePipePiece, pipe_piece_constructor
from .utils import load_module_from_file, camelcase


class PipeInlet(BasePipePiece):
    def __call__(self):
        self.last = self.func(**self.config)
        return self.last


def build_inlets():
    module = load_module_from_file("app/imports/pipe_inlets.py", "imported.pipe_inlets")
    return {
        camelcase(func.__name__): pipe_piece_constructor(PipeInlet, func) 
        for func in [getattr(module, f) for f in dir(module) if f.startswith("pipe_inlet")]
    }
