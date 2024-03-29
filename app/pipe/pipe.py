import yaml
from functools import cached_property
from pandas import DataFrame

from .combiner import PipeCombiner
from .inlet import PipeInlet
from .outlet import PipeOutlet
from .transformer import PipeTransformer


class Pipe:
    def __init__(
        self,
        inlets: PipeInlet | list[PipeInlet] | tuple[PipeInlet],
        combiner: PipeCombiner | None = None,
        transformers: PipeTransformer
        | list[PipeTransformer]
        | tuple[PipeTransformer]
        | None = None,
        outlets: PipeOutlet | list[PipeOutlet] | tuple[PipeOutlet] | None = None,
    ):
        self.inlets = self.__form_tuple(inlets)
        self.combiner = combiner
        self.transformers = self.__form_tuple(transformers)
        self.outlets = self.__form_tuple(outlets)
        self.__setup_validation()

    @classmethod
    def from_dict(cls, pipe_dict: dict):
        return cls(
            inlets=tuple(PipeInlet.from_dict(inlet) for inlet in pipe_dict["inlets"]),
            combiner=PipeCombiner.from_dict(pipe_dict["combiner"]) if "combiner" in pipe_dict else None,
            transformers=tuple(
                PipeTransformer.from_dict(transformer) 
                for transformer in pipe_dict.get("transformers", tuple())
            ),
            outlets=tuple(PipeOutlet.from_dict(outlet) for outlet in pipe_dict.get("outlets", tuple()))
        )

    @classmethod
    def from_yaml(cls, filename: str):
        with open(filename, "r") as f:
            pipes_dict = yaml.safe_load(f)
        return {
            pipe_name: cls.from_dict(pipe_dict)
            for pipe_name, pipe_dict in pipes_dict.items()
        }

    @staticmethod
    def __form_tuple(item):
        if item is None:
            return tuple()
        if isinstance(item, tuple):
            return item
        if isinstance(item, list):
            return tuple(item)
        return (item,)

    def __setup_validation(self):
        if self.num_inlets == 0:
            raise AttributeError("Pipes must have at least one inlet")
        if self.num_inlets > 2:
            raise AttributeError(
                f"Pipes can only support up to two inlets, {self.num_inlets} defined"
            )
        if self.num_inlets > 1 and self.combiner is None:
            raise AttributeError("Multiple inlets defined with no combiner")
        if self.num_inlets == 1 and self.combiner is not None:
            raise AttributeError("Single inlet defined with combiner")

    @cached_property
    def num_inlets(self):
        return len(self.inlets)

    @cached_property
    def num_outlets(self):
        return len(self.outlets)

    @property
    def inlet(self):
        if self.num_inlets == 1:
            return self.inlets[0]
        return self.inlets

    @property
    def outlet(self):
        if self.num_outlets == 1:
            return self.outlets[0]
        return self.outlets

    def pull(self) -> DataFrame | tuple:
        return tuple(inlet() for inlet in self.inlets)

    def combine(self, left: DataFrame, right: DataFrame) -> DataFrame:
        if self.combiner is None:
            raise TypeError("Attempted to combine multiple inlets with no combiner")
        return self.combiner(left=left, right=right)

    def transform(self, df: DataFrame) -> DataFrame:
        for transformer in self.transformers:
            df = df.pipe(transformer)
        return df

    def push(self, df: DataFrame) -> None:
        for outlet in self.outlets:
            outlet(df)

    def __repr__(self):
        return f"<{self.__class__.__name__}(inlets={self.inlets}, combiner={self.combiner}, transformers={self.transformers}, outlets={self.outlets})>"
