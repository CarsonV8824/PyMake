"""
MIT License

Copyright (c) 2026 CarsonV

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import subprocess
from pathlib import Path
import sys
from typing import NoReturn
import json
import os
import platform


def folder_find(
    path: Path, files: list[str], file_type: list[str] = [".cpp", ".c"]
) -> None:
    """Recursive file system that finds all files that start with .cpp and adds them to compile list"""

    for file in path.iterdir():
        if file.name.startswith("."):
            continue
        if file.is_file() and any(
            [check_file for check_file in file_type if file.name.endswith(check_file)]
        ):
            files.append(str(file))

        if file.is_dir():
            folder_find(file, files, file_type)


def main() -> NoReturn:

    current_os = platform.system().lower()
    with open(Path("PyMake.json").absolute(), "r") as f:
        config_data: dict = json.load(f)

    if config_data.get("wipe"):
        delete_files_path = Path(".")
        match current_os:
            case "linux":
                for file in delete_files_path.iterdir():
                    if file.name.endswith(".out"):
                        os.remove(file)
            case "windows":
                for file in delete_files_path.iterdir():
                    if file.name.endswith(".exe"):
                        os.remove(file)
            case "darwin":
                for file in delete_files_path.iterdir():
                    if file.name.endswith(".app"):
                        os.remove(file)

    folder = Path(".")

    files: list[str] = []

    folder_find(
        path=folder,
        files=files,
        file_type=config_data["file_types"],
    )

    files: list[str] = list(set(files))
    files.sort()

    file_names = " ".join(str(file) for file in files)

    output_file_name = f" -o {config_data.get("out")}" if config_data.get("out") else ""

    wall_text = " -Wall" if config_data["warnings"] else ""
    libary_text = (
        " " + " ".join(f"-l{lib}" for lib in config_data["libs"])
        if config_data.get("libs")
        else " "
    )
    command = (
        config_data["compiler"]
        + wall_text
        + " -g -O0 "
        + file_names
        + f" -std={config_data["version"]}"
        + output_file_name
        + libary_text
    )

    print(command)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("\n------------------------------------\n")

    print(
        f"Command errors/Writing errors: {result.stderr if result.stderr else "None"}"
    )
    print(f"Sucess with command script: {not bool(result.returncode)}")
    if bool(result.returncode):
        sys.exit(1)

    print("\n------------------------------------\n")

    if output_file_name != "":
        run = subprocess.run(f"./{config_data.get("out")}")
    else:
        match current_os:
            case "linux":
                run = subprocess.run(f"./a.out")

            case "windows":
                run = subprocess.run(f"./a.exe")

            case "darwin":
                run = subprocess.run(f"./a.app")

            case _:
                raise RuntimeError(
                    "Error determining your operating system when making executable"
                )

    print(f"Runtime errors: {run.stderr if run.stderr else "None"}")
    print(f"Runtime Sucess: {not bool(run.returncode)}")

    sys.exit(0) if not result.stderr and not run.stderr else sys.exit(1)


if __name__ == "__main__":
    main()
