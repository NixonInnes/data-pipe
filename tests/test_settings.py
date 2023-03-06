import pytest


def test_get_setting(settings):
    assert settings.get("test") is None
    assert settings.get("test", "default") == "default"
    with pytest.raises(KeyError):
        assert settings["test"]
    
def test_set_setting(settings):
    settings.set("test", "test")
    assert settings.get("test") == "test"
    assert settings["test"] == "test"

def test_default_settings(default_settings):
    settings = default_settings
    assert settings["REPO_PATH"] == "imports"
    assert settings["REPO_ADDRESS"] == "https://github.com/NixonInnes/data-pipe-defaults.git"
    assert settings["PIPE_COMBINERS_MODULE"] == "imports/pipe_combiners.py"
    assert settings["PIPE_INLETS_MODULE"] == "imports/pipe_inlets.py"
    assert settings["PIPE_OUTLETS_MODULE"] == "imports/pipe_outlets.py"
    assert settings["PIPE_TRANSFORMERS_MODULE"] == "imports/pipe_transformers.py"

def test_test_settings(test_settings):
    settings = test_settings
    assert settings["REPO_PATH"] == "tests/test_imports"
    assert settings["REPO_ADDRESS"] == "https://github.com/NixonInnes/data-pipe-defaults.git"
    assert settings["PIPE_COMBINERS_MODULE"] == "tests/test_imports/pipe_combiners.py"
    assert settings["PIPE_INLETS_MODULE"] == "tests/test_imports/pipe_inlets.py"
    assert settings["PIPE_OUTLETS_MODULE"] == "tests/test_imports/pipe_outlets.py"
    assert settings["PIPE_TRANSFORMERS_MODULE"] == "tests/test_imports/pipe_transformers.py"
