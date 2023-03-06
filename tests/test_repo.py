from app.repo_manager import RepoManager


def test_repo_manager(test_settings_and_repo):
    _, repo = test_settings_and_repo
    assert repo.repo_path == "tests/test_imports"
    assert repo.repo_url == "https://github.com/NixonInnes/data-pipe-defaults.git"
    assert repo.exists()
