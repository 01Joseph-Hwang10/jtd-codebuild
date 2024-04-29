from jtd_codebuild.config.project.model import GoTarget
from .._generator import JTDCodeGenerator


class GoJTDCodeGenerator(JTDCodeGenerator):

    def _codegen_command(self, target: GoTarget) -> str:
        schema_path = self.get_schema_path(target)
        output_dir = self.get_target_path(target)
        target_language = target.language
        return (
            f"jtd-codegen {schema_path} "
            f"--{target_language}-out "
            f"--{target_language}-package {target.package}"
            f"{output_dir}"
        )

    def generate(self, target: GoTarget) -> None:
        return super().generate(target)
