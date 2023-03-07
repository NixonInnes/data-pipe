__all__ = ["PipeInletMemory"]

import pandas as pd
from typing import Callable

from app import Memory

from .. import PipeInlet, PipePieces


@PipePieces.register_inlet("PipeInletMemory")
class PipeInletMemory(PipeInlet):
    @staticmethod
    def read_from_memory(tablename: str) -> pd.DataFrame:
        return Memory.tables.get(tablename)

    _func: Callable = read_from_memory
