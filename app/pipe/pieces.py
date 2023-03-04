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
    def update(cls):
        cls.combiners.update(build_combiners())
        cls.inlets.update(build_inlets())
        cls.outlets.update(build_outlets())
        cls.transformers.update(build_transformers())