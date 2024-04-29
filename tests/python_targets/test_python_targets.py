import subprocess
from os.path import dirname, exists, join
from jtd_codebuild.utils.io import read_json
from jtd_codebuild.config.project.model import ProjectConfig

PROJECT_DIR = join(dirname(__file__), "project")


def test_python_targets():
    config = ProjectConfig(**read_json(join(PROJECT_DIR, "jtd-codebuild.json")))
    subprocess.check_call(
        "jtd-codebuild project",
        shell=True,
        cwd=dirname(__file__),
    )

    assert exists(join(PROJECT_DIR, config.jtdBundlePath))
    for target in config.targets:
        assert exists(join(PROJECT_DIR, target.path, "__init__.py"))
