# h5x (h5-Extra)

Simple fzf or python-cli to modify .h5 or .hdf5 files

# USAGE

## Python Code (h5x.py)

Linux users use `python3`, Windows users use `python`

List all the Groups and datasets recursively:

```sh
python3 h5x.py list {filename}
```

Delete single dataset or group: Ex: `/dev/data1`

```sh
python3 h5x.py delete {filename} -d {dataset / group}
```

`NOTE:` For multiple deletion use -d following by the dataset or group name.

## Fzf Script (h5x)

**_Step-1:_** Download both the python and fzf script and keep it in same directory.

**_Step-2:_** Make h5x file executable and makesure the directory is in your $PATH

## Milestones

This repo is open for suggestion for improvement and features.
