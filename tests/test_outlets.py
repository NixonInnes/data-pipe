import pandas as pd

from app.pipe import PipePieces
from app import Memory


def test_PipeOutletMemory():
    PipePieces.clear()
    PipePieces.update()

    PipeOutletMemory = PipePieces.outlets.get("PipeOutletMemory")
    assert PipeOutletMemory is not None

    p = PipeOutletMemory(tablename="test")
    p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    df = Memory.tables["test"]

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["A", "B", "C"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
