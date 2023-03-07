from typing import Callable
from functools import partial

from app import utils


def raise_(ex):
    raise ex


class BasePipePiece:
    _func: Callable = lambda x: raise_(
        NotImplementedError("BasePipePiece._func must be overridden")
    )

    def __init__(self, **config: dict):
        self.config = config
        self.last = None
        self.func = partial(self._func, **config)

    def __call__(self, *args, **kwargs):
        raise NotImplementedError("BasePipePiece.__call__ must be overridden")

    def __repr__(self):
        return f"<{self.__class__.__name__}(config={self.config})>"


def pipe_piece_constructor(
    PipePieceClass: type[BasePipePiece], func: Callable
) -> type[BasePipePiece]:
    class PipePiece(PipePieceClass):
        _func = staticmethod(func)

    return PipePiece


def build_pieces_from_module(
    filepath: str, module_name: str, prefix: str, PipePieceClass: type[BasePipePiece]
):
    module = utils.load_module_from_file(filepath, module_name)
    return {
        utils.camelcase(func.__name__): pipe_piece_constructor(PipePieceClass, func)
        for func in [getattr(module, f) for f in dir(module) if f.startswith(prefix)]
    }
