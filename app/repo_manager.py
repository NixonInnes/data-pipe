import os
import shutil
from git import Repo


class RepoManager:
    def __init__(self, settings):
        self.settings = settings

    @property
    def repo_path(self):
        return self.settings["REPO_PATH"]
    
    @property
    def repo_url(self):
        return self.settings["REPO_ADDRESS"]

    def clone(self):
        if not os.path.exists(self.repo_path):
            os.makedirs(self.repo_path)
        repo = Repo.clone_from(self.repo_url, self.repo_path)
        return repo

    def pull(self):
        repo = Repo(self.repo_path)
        repo.remotes.origin.pull()
        return repo

    def exists(self):
        return os.path.exists(self.repo_path)

    def delete(self):
        if os.path.exists(self.repo_path):
            shutil.rmtree(self.repo_path)
