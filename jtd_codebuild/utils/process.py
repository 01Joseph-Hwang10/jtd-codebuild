import subprocess
from typing import List


def wait_for_processes(
    processes: List[subprocess.Popen],
    print_stdout: bool = True,
    print_stderr: bool = True,
) -> None:
    """Wait for all processes to finish.

    Args:
        processes: The list of processes.
        print_stdout: Whether to print stdout.
        print_stderr: Whether to print stderr.
    """
    # Wait for existing processes to finish before starting the modification
    for process in processes:
        process.wait()

        # Print stdout and stderr
        stdout, stderr = process.communicate()

        if stdout and print_stdout:
            # Print stdout if it exists and `print_stdout` is set to true
            print(stdout.decode("utf-8"))
        if stderr:
            if print_stderr:
                # Print stderr if it exists and `print_stderr` is set to true
                print(stderr.decode("utf-8"))
            # Raise an exception if stderr exists
            exit(1)
