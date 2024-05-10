import subprocess


def run_codebuild(
    cwd: str,
    project: str = "project",
) -> None:
    subprocess.check_call(
        f"jtd-codebuild {project}",
        shell=True,
        cwd=cwd,
    )
