from os import getcwd
from os.path import basename
from typing import Generator, Callable
from joblib import Parallel, delayed
from toolz import pipe
from .utils.fs import resolve
from .utils.io import write_json
from .bundler import Bundler
from .inheritance import InheritanceResolver
from .component import Component
from .config.project import get_project_config
from .generators import JTDCodeGenerator


class Codebuild(Component):
    def run(
        self,
        path: str,
        cwd: str = getcwd(),
    ):
        """Generate code from the JSON Type Definition files.

        Args:
            path: The current working directory.
        """
        # Get the path of the target directory
        target_path = resolve(cwd, path)
        config = get_project_config(cwd)

        self.logger.info(f"Start building: {basename(target_path)}")

        self.logger.info("Bundling IDL files...")
        bundler = Bundler(self.logger)
        inheritance = InheritanceResolver(self.logger)
        bundled_jtd_schema = pipe(
            bundler.bundle(target_path, config),
            inheritance.resolve,
        )

        self.logger.info("Writing bundled IDL file...")
        schema_path = resolve(target_path, config.jtdBundlePath)
        write_json(schema_path, bundled_jtd_schema)

        self.logger.success("Wrote bundled IDL file...")

        self.logger.info("Generating targets...")

        def generate_targets() -> Generator[Callable[[], None], None, None]:
            for target in config.targets:
                generator = JTDCodeGenerator(target_path, logger=self.logger)

                yield lambda: generator.generate(target)

        Parallel(n_jobs=-1)(delayed(generator)() for generator in generate_targets())
        self.logger.success("Done!")
