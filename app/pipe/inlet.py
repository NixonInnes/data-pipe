from .base import BasePipePiece, build_pieces_from_module


class PipeInlet(BasePipePiece):
    _pieces_attr = "inlets"

    def __call__(self):
        self.last = self.func()
        return self.last


def build_inlets(settings):
    return build_pieces_from_module(
        settings["PIPE_INLETS_MODULE"], "imported.pipe_inlets", "pipe_inlet", PipeInlet
    )
