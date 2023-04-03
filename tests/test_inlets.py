import pandas as pd

from app.pipe import PipePieces
from app.pipe.inlet import PipeInlet
from app import Memory


def test_PipeInletCSV(test_settings):
    settings = test_settings
    PipePieces.clear()
    PipePieces.update(settings)

    PipeInletCSV = PipePieces.inlets.get("PipeInletCsv")
    assert PipeInletCSV is not None

    p = PipeInletCSV(filename="tests/example.csv")
    df = p()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["A", "B", "C"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]


def test_PipeInletCSV_with_config(test_settings):
    settings = test_settings
    PipePieces.clear()
    PipePieces.update(settings)

    PipeInletCSV = PipePieces.inlets.get("PipeInletCsv")
    assert PipeInletCSV is not None

    p = PipeInletCSV(filename="tests/example.csv", usecols=["A", "B"], skiprows=[1])
    df = p()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert df.columns.tolist() == ["A", "B"]
    assert df["A"].tolist() == [2, 3]
    assert df["B"].tolist() == [5, 6]


def test_PipeInletMemory():
    PipePieces.clear()
    PipePieces.update()

    PipeInletMemory = PipePieces.inlets.get("PipeInletMemory")
    assert PipeInletMemory is not None

    Memory.tables["test"] = pd.DataFrame(
        {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}
    )
    p = PipeInletMemory(tablename="test")
    df = p()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["A", "B", "C"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]

def test_PipeInletCSV_from_dict(test_settings):
    PipePieces.clear()
    PipePieces.update(test_settings)

    d = {
        "type": "PipeInletCsv",
        "config": {"filename": "tests/example.csv"},
    }

    p = PipeInlet.from_dict(d)
    assert p is not None
    df = p()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["A", "B", "C"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]