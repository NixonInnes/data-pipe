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


from app import repo


def test_repo_manager():
    repo.delete()
    assert not os.path.exists(settings["REPO_PATH"])
    repo.clone()
    assert os.path.exists(settings["REPO_PATH"])
    assert os.path.exists(settings["PIPE_COMBINERS_MODULE"])
    assert os.path.exists(settings["PIPE_INLETS_MODULE"])
    assert os.path.exists(settings["PIPE_TRANSFORMERS_MODULE"])
    assert os.path.exists(settings["PIPE_OUTLETS_MODULE"])
