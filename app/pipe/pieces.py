from .combiner import build_combiners
from .inlet import build_inlets
from .outlet import build_outlets
from .transformer import build_transformers


class PipePieces:
    combiners: dict = {}
    inlets: dict = {}
    outlets: dict = {}
    transformers: dict = {}

    @classmethod
    def clear(cls):
        cls.combiners.clear()
        cls.inlets.clear()
        cls.outlets.clear()
        cls.transformers.clear()

    @classmethod
    def update(cls, settings):
        cls.combiners.update(build_combiners(settings))
        cls.inlets.update(build_inlets(settings))
        cls.outlets.update(build_outlets(settings))
        cls.transformers.update(build_transformers(settings))
