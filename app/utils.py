import importlib.util


def load_module_from_file(filename, module_name):
    spec = importlib.util.spec_from_file_location(module_name, filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def camelcase(string):
    return "".join(
        [
            word.capitalize() if not all([char.isupper() for char in word]) else word 
            for word in string.split('_')
        ]
    )
