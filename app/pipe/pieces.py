from .combiner import build_combiners
from .inlet import build_inlets
from .outlet import build_outlets
from .transformer import build_transformers


class PipePiecesCollection:
    def __init__(self, builtins: dict, imported: dict):
        self.builtins = builtins
        self.imported = imported

    def __get__(self, obj, objtype=None):
        return {**self.builtins, **self.imported}


class PipePieces:
    builtin_combiners: dict = {}
    builtin_inlets: dict = {}
    builtin_outlets: dict = {}
    builtin_transformers: dict = {}

    imported_combiners: dict = {}
    imported_inlets: dict = {}
    imported_outlets: dict = {}
    imported_transformers: dict = {}

    combiners: PipePiecesCollection = PipePiecesCollection(
        builtin_combiners, imported_combiners
    )
    inlets: PipePiecesCollection = PipePiecesCollection(builtin_inlets, imported_inlets)
    outlets: PipePiecesCollection = PipePiecesCollection(
        builtin_outlets, imported_outlets
    )
    transformers: PipePiecesCollection = PipePiecesCollection(
        builtin_transformers, imported_transformers
    )

    @classmethod
    def register_combiner(cls, name):
        def register_combiner_decorator(combiner):
            cls.builtin_combiners[name] = combiner
            return combiner

        return register_combiner_decorator

    @classmethod
    def register_inlet(cls, name):
        def register_inlet_decorator(inlet):
            cls.builtin_inlets[name] = inlet
            return inlet

        return register_inlet_decorator

    @classmethod
    def register_outlet(cls, name):
        def register_outlet_decorator(outlet):
            cls.builtin_outlets[name] = outlet
            return outlet

        return register_outlet_decorator

    @classmethod
    def register_transformer(cls, name):
        def register_transformer_decorator(transformer):
            cls.builtin_transformers[name] = transformer
            return transformer

        return register_transformer_decorator

    @classmethod
    def clear(cls):
        cls.imported_combiners.clear()
        cls.imported_inlets.clear()
        cls.imported_outlets.clear()
        cls.imported_transformers.clear()

    @classmethod
    def update(cls, settings=None):
        from . import builtin

        if settings is not None:
            cls.imported_combiners.update(build_combiners(settings))
            cls.imported_inlets.update(build_inlets(settings))
            cls.imported_outlets.update(build_outlets(settings))
            cls.imported_transformers.update(build_transformers(settings))
