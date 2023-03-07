__all__ = ["PipeOutletMemory"]

import pandas as pd
from typing import Callable

from app import Memory

from .. import PipeOutlet, PipePieces


@PipePieces.register_outlet("PipeOutletMemory")
class PipeOutletMemory(PipeOutlet):
    @staticmethod
    def write_to_memory(df: pd.DataFrame, tablename: str):
        Memory.tables[tablename] = df

    _func: Callable = write_to_memory
