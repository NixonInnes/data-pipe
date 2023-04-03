import pandas as pd

from app import Memory
from app.pipe import PipePieces, Pipe


def test_pipe(test_settings):
    settings = test_settings
    PipePieces.clear()
    PipePieces.update(settings)

    Memory.tables["test"] = pd.DataFrame(
        {"A": [10, 20, 30], "B": [40, 50, 60], "C": [70, 80, 90]}
    )

    pipe = Pipe(
        inlets=[
            PipePieces.inlets["PipeInletCsv"](filename="tests/example.csv"),
            PipePieces.inlets["PipeInletMemory"](tablename="test"),
        ],
        combiner=PipePieces.combiners["PipeCombinerJoin"](rsuffix="_r"),
        transformers=[
            PipePieces.transformers["PipeTransformerMath"](
                source="A", value=100, operation="add", result="A"
            ),
            PipePieces.transformers["PipeTransformerMath"](
                source="B_r", value=2, operation="subtract", result="B_r-2"
            )
        ],
        outlets=[PipePieces.outlets["PipeOutletMemory"](tablename="test-out")],
    )

    pull_result = pipe.pull()
    assert len(pull_result) == 2
    pull_result_left = pull_result[0]
    pull_result_right = pull_result[1]

    assert isinstance(pull_result_left, pd.DataFrame)
    assert isinstance(pull_result_right, pd.DataFrame)

    assert pull_result_left.shape == (3, 3)
    assert pull_result_right.shape == (3, 3)

    assert pull_result_left.columns.tolist() == ["A", "B", "C"]
    assert pull_result_left["A"].tolist() == [1, 2, 3]
    assert pull_result_left["B"].tolist() == [4, 5, 6]
    assert pull_result_left["C"].tolist() == [7, 8, 9]

    assert pull_result_right.columns.tolist() == ["A", "B", "C"]
    assert pull_result_right["A"].tolist() == [10, 20, 30]
    assert pull_result_right["B"].tolist() == [40, 50, 60]
    assert pull_result_right["C"].tolist() == [70, 80, 90]

    combine_result = pipe.combine(*pull_result)

    assert isinstance(combine_result, pd.DataFrame)
    assert combine_result.shape == (3, 6)
    assert combine_result.columns.tolist() == ["A", "B", "C"] + ["A_r", "B_r", "C_r"]
    assert combine_result["A"].tolist() == [1, 2, 3]
    assert combine_result["B"].tolist() == [4, 5, 6]
    assert combine_result["C"].tolist() == [7, 8, 9]
    assert combine_result["A_r"].tolist() == [10, 20, 30]
    assert combine_result["B_r"].tolist() == [40, 50, 60]
    assert combine_result["C_r"].tolist() == [70, 80, 90]

    transform_result = pipe.transform(combine_result)
    assert isinstance(transform_result, pd.DataFrame)
    assert transform_result.shape == (3, 7)
    assert transform_result.columns.tolist() == ["A", "B", "C"] + ["A_r", "B_r", "C_r"] + ["B_r-2"]
    assert transform_result["A"].tolist() == [101, 102, 103]
    assert transform_result["B"].tolist() == [4, 5, 6]
    assert transform_result["C"].tolist() == [7, 8, 9]
    assert transform_result["A_r"].tolist() == [10, 20, 30]
    assert transform_result["B_r"].tolist() == [40, 50, 60]
    assert transform_result["C_r"].tolist() == [70, 80, 90]
    assert transform_result["B_r-2"].tolist() == [38, 48, 58]

    pipe.push(transform_result)

    assert "test-out" in Memory.tables
    push_result = Memory.tables["test-out"]
    assert push_result.shape == (3, 7)
    assert push_result.columns.tolist() == ["A", "B", "C"] + ["A_r", "B_r", "C_r"] + ["B_r-2"]
    assert push_result["A"].tolist() == [101, 102, 103]
    assert push_result["B"].tolist() == [4, 5, 6]
    assert push_result["C"].tolist() == [7, 8, 9]
    assert push_result["A_r"].tolist() == [10, 20, 30]
    assert push_result["B_r"].tolist() == [40, 50, 60]
    assert push_result["C_r"].tolist() == [70, 80, 90]
    assert push_result["B_r-2"].tolist() == [38, 48, 58]


def test_pipe_from_yaml():
    Memory.tables["test"] = pd.DataFrame(
        {"A": [10, 20, 30], "B": [40, 50, 60], "C": [70, 80, 90]}
    )

    pipes = Pipe.from_yaml("tests/test-pipe-config.yaml")

    assert len(pipes) == 1
    assert "test-pipe" in pipes

    pipe = pipes["test-pipe"]

    assert len(pipe.inlets) == 2
    assert pipe.combiner is not None
    assert len(pipe.transformers) == 2
    assert len(pipe.outlets) == 1

    pull_result = pipe.pull()
    assert len(pull_result) == 2
    pull_result_left = pull_result[0]
    pull_result_right = pull_result[1]

    assert isinstance(pull_result_left, pd.DataFrame)
    assert isinstance(pull_result_right, pd.DataFrame)

    assert pull_result_left.shape == (3, 3)
    assert pull_result_right.shape == (3, 3)

    assert pull_result_left.columns.tolist() == ["A", "B", "C"]
    assert pull_result_left["A"].tolist() == [1, 2, 3]
    assert pull_result_left["B"].tolist() == [4, 5, 6]
    assert pull_result_left["C"].tolist() == [7, 8, 9]

    assert pull_result_right.columns.tolist() == ["A", "B", "C"]
    assert pull_result_right["A"].tolist() == [10, 20, 30]
    assert pull_result_right["B"].tolist() == [40, 50, 60]
    assert pull_result_right["C"].tolist() == [70, 80, 90]

    combine_result = pipe.combine(*pull_result)

    assert isinstance(combine_result, pd.DataFrame)
    assert combine_result.shape == (3, 6)
    assert combine_result.columns.tolist() == ["A", "B", "C"] + ["A_r", "B_r", "C_r"]
    assert combine_result["A"].tolist() == [1, 2, 3]
    assert combine_result["B"].tolist() == [4, 5, 6]
    assert combine_result["C"].tolist() == [7, 8, 9]
    assert combine_result["A_r"].tolist() == [10, 20, 30]
    assert combine_result["B_r"].tolist() == [40, 50, 60]
    assert combine_result["C_r"].tolist() == [70, 80, 90]

    transform_result = pipe.transform(combine_result)
    assert isinstance(transform_result, pd.DataFrame)
    assert transform_result.shape == (3, 7)
    assert transform_result.columns.tolist() == ["A", "B", "C"] + ["A_r", "B_r", "C_r"] + ["2B_r"]
    assert transform_result["A"].tolist() == [2, 3, 4]
    assert transform_result["B"].tolist() == [4, 5, 6]
    assert transform_result["C"].tolist() == [7, 8, 9]
    assert transform_result["A_r"].tolist() == [10, 20, 30]
    assert transform_result["B_r"].tolist() == [40, 50, 60]
    assert transform_result["C_r"].tolist() == [70, 80, 90]
    assert transform_result["2B_r"].tolist() == [80, 100, 120]

    pipe.push(transform_result)

    assert "test-out" in Memory.tables
    push_result = Memory.tables["test-out"]
    assert push_result.shape == (3, 7)
    assert push_result.columns.tolist() == ["A", "B", "C"] + ["A_r", "B_r", "C_r"] + ["2B_r"]
    assert push_result["A"].tolist() == [2, 3, 4]
    assert push_result["B"].tolist() == [4, 5, 6]
    assert push_result["C"].tolist() == [7, 8, 9]
    assert push_result["A_r"].tolist() == [10, 20, 30]
    assert push_result["B_r"].tolist() == [40, 50, 60]
    assert push_result["C_r"].tolist() == [70, 80, 90]
    assert push_result["2B_r"].tolist() == [80, 100, 120]