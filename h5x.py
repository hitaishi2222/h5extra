import subprocess
import typer
import h5py
from typing import List
from typing_extensions import Annotated

app = typer.Typer(no_args_is_help=True)


# h5ls wrapper
@app.command()
def list(
    file: Annotated[str, typer.Argument(help=".h5 or .hdf5 file", resolve_path=True)],
):

    command = ["h5ls", "-r", file]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error running h5ls:")
        print(e.stderr)


# Delete: supports MULTIPLE nodes
@app.command()
def delete(
    file: Annotated[str, typer.Argument(help=".h5 or .hdf5 file", resolve_path=True)],
    node: Annotated[
        List[str],
        typer.Option(
            "-d",
            "--delete",
            help="Path(s) of group or dataset to delete. Example: -d /g1 -d /g1/sub",
        ),
    ] = [],
):

    if not node:
        print("No delete paths provided. Use --delete /group/path")
        raise typer.Exit()

    for n in node:
        delete_node(file, n)


# Helper
def delete_node(filepath: str, name: str):
    name = name.rstrip("/")  # normalize

    with h5py.File(filepath, "r+") as f:
        if name in f:
            del f[name]
            print(f"✔  Deleted: {name}")
        else:
            print(f"✖  Not found: {name}")


if __name__ == "__main__":
    app()
