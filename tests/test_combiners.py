import pandas as pd

from app.pipe import PipePieces


def test_PipeCombinerJoin():
    PipePieces.clear()
    PipePieces.update()

    PipeCombinerJoin = PipePieces.combiners.get("PipeCombinerJoin")
    assert PipeCombinerJoin is not None

    p = PipeCombinerJoin(rsuffix="_r")

    left = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
    right = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})

    df = p(left, right)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 6)
    assert df.columns.tolist() == ["A", "B", "C", "A_r", "B_r", "C_r"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
    assert df["A_r"].tolist() == [1, 2, 3]
    assert df["B_r"].tolist() == [4, 5, 6]
    assert df["C_r"].tolist() == [7, 8, 9]


def test_PipeCombinerConcat():
    PipePieces.clear()
    PipePieces.update()

    PipeCombinerConcat = PipePieces.combiners.get("PipeCombinerConcat")
    assert PipeCombinerConcat is not None

    p = PipeCombinerConcat()

    left = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
    right = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})

    df = p(left, right)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (6, 3)
    assert df.columns.tolist() == ["A", "B", "C"]
    assert df["A"].tolist() == [1, 2, 3] * 2
    assert df["B"].tolist() == [4, 5, 6] * 2
    assert df["C"].tolist() == [7, 8, 9] * 2
