from jtd_codebuild.config.project.model import RubyTarget
from .._generator import JTDCodeGenerator


class RubyJTDCodeGenerator(JTDCodeGenerator):

    def _codegen_command(self, target: RubyTarget) -> str:
        schema_path = self.get_schema_path(target)
        output_dir = self.get_target_path(target)
        target_language = target.language
        return (
            f"jtd-codegen {schema_path} "
            f"--{target_language}-out "
            f"--{target_language}-module {target.module}"
            f"{output_dir}"
        )

    def generate(self, target: RubyTarget) -> None:
        return super().generate(target)
