import os

os.environ["ENV"] = "test"
os.environ["SETUP"] = "no"


from app import settings

TEST_SETTINGS = {
    "REPO_PATH": "imports",
    "REPO_ADDRESS": "https://github.com/NixonInnes/data-pipe-defaults.git",
    "PIPE_COMBINERS_MODULE": "imports/pipe_combiners.py",
    "PIPE_INLETS_MODULE": "imports/pipe_inlets.py",
    "PIPE_OUTLETS_MODULE": "imports/pipe_outlets.py",
    "PIPE_TRANSFORMERS_MODULE": "imports/pipe_transformers.py",
}

settings.load_dict(TEST_SETTINGS)

import pandas as pd

from app.pipe import PipePieces

PipePieces.update()


def test_PipeInletCSV():
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
