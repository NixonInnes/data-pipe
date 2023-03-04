from app import settings

from .base import BasePipePiece, build_pieces_from_module


class PipeInlet(BasePipePiece):
    def __call__(self):
        self.last = self.func()
        return self.last


def build_inlets():
    return build_pieces_from_module(
        settings.get("PIPE_INLET_MODULE"),
        "imported.pipe_inlets",
        "pipe_inlet",
        PipeInlet
    )
