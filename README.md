# h5extra (`h5x`)

Two ways to work inside `.h5` / `.hdf5` files without leaving the terminal:

- a **Python CLI** for scripting — list the tree, delete groups and datasets;
- a **bash + fzf** front-end for exploring by hand — browse the tree, preview any
  dataset with `h5dump`, and copy it to your clipboard.

```
h5extra
├── h5x.py   # Python CLI (typer + h5py)
└── h5x      # interactive fzf front-end
```

<p>
  <img src="https://github.com/hitaishi2222/h5extra/actions/workflows/ci.yml/badge.svg" alt="CI"/>
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/python-3.12+-3776AB?style=flat-square&logo=python&logoColor=3776AB"/>
</p>

## Requirements

- Python ≥ 3.12
- [`h5py`](https://h5py.org) and [`typer`](https://typer.tiangolo.com) (for the Python CLI)
- HDF5 command-line tools — `h5ls`, `h5dump`
- [`fzf`](https://github.com/junegunn/fzf) (for the interactive front-end)
- `wl-copy` / `xclip` / `xsel` / `pbcopy` — only for the clipboard copy in `check_data`

## Install

```bash
git clone https://github.com/hitaishi2222/h5extra.git
cd h5extra
pip install -e .
```

For the fzf script, keep it in the same directory as `h5x.py`, make it executable
and put that directory on your `$PATH`:

```bash
chmod +x h5x
export PATH="$PATH:$PWD"
```

## Python CLI

On Linux use `python3`; on Windows use `python`.

**List all groups and datasets, recursively:**

```bash
python3 h5x.py list file.h5
```

**Delete a group or dataset** — the path is the absolute path inside the file:

```bash
python3 h5x.py delete file.h5 -d /dev/data1
```

**Delete several at once** — repeat `-d`:

```bash
python3 h5x.py delete file.h5 -d /dev/data1 -d /dev/data2
```

## Interactive mode

Run `h5x` in a directory containing `.h5`/`.hdf5` files. It offers three
operations, each backed by `fzf`:

| Operation | What it does |
|---|---|
| `list` | Recursive listing of the file (same as `h5ls -lr`) |
| `check_data` | Pick a dataset, preview it with `h5dump`, copy the dump to the clipboard |
| `del` | Pick groups and/or datasets to delete (multi-select), then confirm |

## Notes

- Deletion is destructive and immediate — `h5x` does not make a backup. Copy the
  file first if it matters.
- The Python CLI opens files with `h5py` in `r+` mode for deletion, and never
  unpickles anything.
- `h5x` expects `h5x.py` to sit next to it in the same directory.

## License

MIT — see [LICENSE](LICENSE).
