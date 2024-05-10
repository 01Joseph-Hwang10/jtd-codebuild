import shutil
from os.path import dirname, exists, join
from jtd_codebuild.utils.io import read_json
from jtd_codebuild.utils.fs import resolve
from jtd_codebuild.config.project.model import ProjectConfig
from tests.helpers import run_codebuild

LIB_DIR = join(dirname(__file__), "workspace/packages/lib")
PROJECT_DIR = join(dirname(__file__), "workspace/packages/app")

config = ProjectConfig(**read_json(join(PROJECT_DIR, "jtd-codebuild.json")))


def setup_module():
    shutil.rmtree(join(LIB_DIR, "gen"), ignore_errors=True)
    shutil.rmtree(join(PROJECT_DIR, "gen"), ignore_errors=True)


def test_workspace():
    run_codebuild(dirname(__file__), project="workspace/packages/app")

    assert exists(resolve(PROJECT_DIR, config.jtdBundlePath))
