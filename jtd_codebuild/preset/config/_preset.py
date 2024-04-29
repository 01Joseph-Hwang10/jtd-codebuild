from os.path import join, relpath
from shutil import copyfile
from jtd_codebuild.values import CONFIG_NAME
from .._preset import Preset


class ConfigPreset(Preset):
    def generate(self, cwd: str, **options):
        copy_config = [
            {
                "src": join(cwd, "templates", CONFIG_NAME),
                "dest": join(cwd, CONFIG_NAME),
            }
        ]
        for config in copy_config:
            copyfile(config["src"], config["dest"])
            self.logger.info(f"Created: {relpath(config['dest'], cwd)}")
