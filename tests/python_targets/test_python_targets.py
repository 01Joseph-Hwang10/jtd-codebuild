import shutil
from os.path import dirname, exists, join
from jtd_codebuild.utils.io import read_json
from jtd_codebuild.config.project.model import ProjectConfig
from tests.helpers import run_codebuild

PROJECT_DIR = join(dirname(__file__), "project")
config = ProjectConfig(**read_json(join(PROJECT_DIR, "jtd-codebuild.json")))


def setup_module():
    shutil.rmtree(join(PROJECT_DIR, "gen"), ignore_errors=True)


def test_python_targets():
    run_codebuild(dirname(__file__))

    assert exists(join(PROJECT_DIR, config.jtdBundlePath))
    for target in config.targets:
        assert exists(join(PROJECT_DIR, target.path, "__init__.py"))
