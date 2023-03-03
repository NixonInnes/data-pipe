from typing import Callable
from functools import partial


def raise_(ex):
    raise ex

class BasePipePiece:
    _func: Callable = lambda x: raise_(NotImplementedError("BasePipePiece._func must be overridden"))
    
    def __init__(self, **config: dict):    
        self.config = config
        self.last = None
        self.func = partial(self._func, **self.config)

    def __repr__(self):
        return f"<{self.__class__.__name__}(config={self.config})>"


def pipe_piece_constructor(PipePieceClass: type[BasePipePiece], func: Callable) -> type[BasePipePiece]:
    class PipePiece(PipePieceClass):
        _func = staticmethod(func)
    return PipePiece
