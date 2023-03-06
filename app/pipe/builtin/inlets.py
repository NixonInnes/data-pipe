import pandas as pd
from typing import Callable

from app import Memory

from .. import PipeInlet


class PipeInletMemory(PipeInlet):
    @staticmethod
    def read_from_memory(tablename: str) -> pd.DataFrame:
        return Memory.tables.get(tablename)

    _func: Callable = read_from_memory
