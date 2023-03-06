import pandas as pd

from app.pipe import PipePieces


def test_PipeInletCSV(test_settings_and_repo):
    settings, repo = test_settings_and_repo
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
