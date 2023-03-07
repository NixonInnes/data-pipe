__all__ = ["PipeCombinerJoin", "PipeCombinerConcat"]

import pandas as pd
from typing import Callable

from .. import PipeCombiner, PipePieces


@PipePieces.register_combiner("PipeCombinerJoin")
class PipeCombinerJoin(PipeCombiner):
    @staticmethod
    def join(left: pd.DataFrame, right: pd.DataFrame, **kwargs) -> pd.DataFrame:
        return left.join(right, **kwargs)

    _func: Callable = join


@PipePieces.register_combiner("PipeCombinerConcat")
class PipeCombinerConcat(PipeCombiner):
    @staticmethod
    def concat(left: pd.DataFrame, right: pd.DataFrame, **kwargs) -> pd.DataFrame:
        return pd.concat((left, right), **kwargs)

    _func: Callable = concat
