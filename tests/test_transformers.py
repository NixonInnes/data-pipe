import pandas as pd

from app.pipe import PipePieces


def test_PipeTransformerAdd():
    PipePieces.clear()
    PipePieces.update()
    
    PipeTransformerAdd = PipePieces.transformers.get("PipeTransformerAdd")
    assert PipeTransformerAdd is not None
    
    p = PipeTransformerAdd(source="A", value=1)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["A", "B", "C"]
    assert df["A"].tolist() == [2, 3, 4]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]

    p = PipeTransformerAdd(source="A", result="a", value=1)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == ["A", "B", "C", "a"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
    assert df["a"].tolist() == [2, 3, 4]

    p = PipeTransformerAdd(source="A", result="AB", value="B", value_is_column=True)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == ["A", "B", "C", "AB"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
    assert df["AB"].tolist() == [5, 7, 9]


def test_PipeTransformerSubtract():
    PipePieces.clear()
    PipePieces.update()
    
    PipeTransformerSubtract = PipePieces.transformers.get("PipeTransformerSubtract")
    assert PipeTransformerSubtract is not None
    
    p = PipeTransformerSubtract(source="A", value=1)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["A", "B", "C"]
    assert df["A"].tolist() == [0, 1, 2]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]

    p = PipeTransformerSubtract(source="A", result="a", value=1)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == ["A", "B", "C", "a"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
    assert df["a"].tolist() == [0, 1, 2]

    p = PipeTransformerSubtract(source="A", result="AB", value="B", value_is_column=True)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == ["A", "B", "C", "AB"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
    assert df["AB"].tolist() == [-3, -3, -3]


def test_PipeTransformerMultiply():
    PipePieces.clear()
    PipePieces.update()
    
    PipeTransformerMultiply = PipePieces.transformers.get("PipeTransformerMultiply")
    assert PipeTransformerMultiply is not None
    
    p = PipeTransformerMultiply(source="A", value=2)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["A", "B", "C"]
    assert df["A"].tolist() == [2, 4, 6]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]

    p = PipeTransformerMultiply(source="A", result="a", value=2)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == ["A", "B", "C", "a"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
    assert df["a"].tolist() == [2, 4, 6]

    p = PipeTransformerMultiply(source="A", result="AB", value="B", value_is_column=True)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == ["A", "B", "C", "AB"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
    assert df["AB"].tolist() == [4, 10, 18]


def test_PipeTransformerDivide():
    PipePieces.clear()
    PipePieces.update()
    
    PipeTransformerDivide = PipePieces.transformers.get("PipeTransformerDivide")
    assert PipeTransformerDivide is not None
    
    p = PipeTransformerDivide(source="A", value=2)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["A", "B", "C"]
    assert df["A"].tolist() == [0.5, 1, 1.5]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]

    p = PipeTransformerDivide(source="A", result="a", value=2)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == ["A", "B", "C", "a"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
    assert df["a"].tolist() == [0.5, 1, 1.5]

    p = PipeTransformerDivide(source="A", result="AB", value="B", value_is_column=True)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == ["A", "B", "C", "AB"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
    assert df["AB"].tolist() == [0.25, 0.4, 0.5]


def test_PipeTransformerFloorDivide():
    PipePieces.clear()
    PipePieces.update()
    
    PipeTransformerFloorDivide = PipePieces.transformers.get("PipeTransformerFloorDivide")
    assert PipeTransformerFloorDivide is not None
    
    p = PipeTransformerFloorDivide(source="A", value=2)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["A", "B", "C"]
    assert df["A"].tolist() == [0, 1, 1]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]

    p = PipeTransformerFloorDivide(source="A", result="a", value=2)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == ["A", "B", "C", "a"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
    assert df["a"].tolist() == [0, 1, 1]

    p = PipeTransformerFloorDivide(source="B", result="AB", value="A", value_is_column=True)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == ["A", "B", "C", "AB"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
    assert df["AB"].tolist() == [4, 2, 2]


def test_PipeTransformerPower():
    PipePieces.clear()
    PipePieces.update()
    
    PipeTransformerPower = PipePieces.transformers.get("PipeTransformerPower")
    assert PipeTransformerPower is not None
    
    p = PipeTransformerPower(source="A", value=2)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["A", "B", "C"]
    assert df["A"].tolist() == [1, 4, 9]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]

    p = PipeTransformerPower(source="A", result="a", value=2)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == ["A", "B", "C", "a"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
    assert df["a"].tolist() == [1, 4, 9]

    p = PipeTransformerPower(source="A", result="AB", value="B", value_is_column=True)
    df = p(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == ["A", "B", "C", "AB"]
    assert df["A"].tolist() == [1, 2, 3]
    assert df["B"].tolist() == [4, 5, 6]
    assert df["C"].tolist() == [7, 8, 9]
    assert df["AB"].tolist() == [1, 32, 729]
