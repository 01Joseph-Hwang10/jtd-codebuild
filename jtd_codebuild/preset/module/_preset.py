from os import mkdir
from os.path import join, relpath
from shutil import copyfile
from jtd_codebuild.values import CONFIG_NAME
from .._preset import Preset


class ModulePreset(Preset):
    def generate(self, cwd: str, **options):
        copy_config = [
            {
                "src": join(cwd, "templates", CONFIG_NAME),
                "dest": join(cwd, CONFIG_NAME),
            },
            {
                "src": join(cwd, "templates", ".gitignore"),
                "dest": join(cwd, ".gitignore"),
            },
        ]
        for config in copy_config:
            copyfile(config["src"], config["dest"])
            self.logger.info(f"Created: {relpath(config['dest'], cwd)}")

        mkdir_config = [
            join(cwd, "src"),
            join(cwd, "gen"),
        ]
        for directory in mkdir_config:
            mkdir(directory)
            self.logger.info(f"Created: {relpath(directory, cwd)}")
