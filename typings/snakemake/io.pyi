"""
This type stub file was generated by pyright.
"""
from __future__ import annotations

import os
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Callable, Generic, Iterable, List, Sequence, TypeVar, overload

__author__ = ...
__copyright__ = ...
__email__ = ...
__license__ = ...

class Mtime:
    __slots__ = ...
    def __init__(self, local=..., local_target=..., remote=...) -> None: ...
    def local_or_remote(self, follow_symlinks=...): ...
    def remote(self): ...
    def local(self, follow_symlinks=...): ...

def lutime(f, times): ...

if os.chmod in os.supports_follow_symlinks:
    def lchmod(f, mode): ...

else:
    def lchmod(f, mode): ...

class ExistsDict(dict):
    def __init__(self, cache) -> None: ...
    def __getitem__(self, path): ...
    def __contains__(self, path): ...

class IOCache:
    def __init__(self, max_wait_time) -> None: ...
    def mtime_inventory(self, jobs): ...
    async def collect_mtime(self, path): ...
    def clear(self): ...
    def deactivate(self): ...

def IOFile(file, rule=...): ...

class _IOFile(str):
    """
    A file that is either input or output of a rule.
    """

    __slots__ = ...
    def __new__(cls, file): ...
    def new_from(self, new_value): ...
    def iocache(func): ...
    def inventory(self): ...
    @_refer_to_remote
    def get_inventory_parent(self):  # -> _IOFile | None:
        """If eligible for inventory, get the parent of a given path.

        This code does not work on local Windows paths,
        but inventory is disabled on Windows.
        """
        ...
    @contextmanager
    def open(
        self, mode=..., buffering=..., encoding=..., errors=..., newline=...
    ):  # -> Generator[TextIOWrapper, None, None]:
        """Open this file. If necessary, download it from remote first.

        This can (and should) be used in a `with`-statement.
        """
        ...
    def contains_wildcard(self): ...
    @property
    def is_remote(self): ...
    @property
    def is_ancient(self): ...
    @property
    def is_directory(self): ...
    @property
    def is_temp(self): ...
    @property
    def is_multiext(self): ...
    @property
    def multiext_prefix(self): ...
    def update_remote_filepath(self): ...
    @property
    def should_keep_local(self): ...
    @property
    def should_stay_on_remote(self): ...
    @property
    def remote_object(self): ...
    @property
    @_refer_to_remote
    def file(self): ...
    def check(self): ...
    @property
    def exists(self): ...
    def parents(self, omit=...):  # -> Generator[_IOFile, None, None]:
        """Yield all parent paths, omitting the given number of ancestors."""
        ...
    @property
    @iocache
    def exists_local(self): ...
    @property
    @iocache
    def exists_remote(self): ...
    @property
    def protected(self):  # -> bool:
        """Returns True if the file is protected. Always False for symlinks."""
        ...
    @property
    @iocache
    def mtime(self): ...
    @property
    def mtime_uncached(self):  # -> Mtime:
        """Obtain mtime.

        Usually, this will be one stat call only. For symlinks and directories
        it will be two, for symlinked directories it will be three,
        for remote files it will additionally query the remote
        location.
        """
        ...
    @property
    def flags(self): ...
    def is_fifo(self):  # -> bool:
        """Return True if file is a FIFO according to the filesystem."""
        ...
    @property
    @iocache
    @_refer_to_remote
    def size(self): ...
    @property
    def size_local(self): ...
    def is_checksum_eligible(self): ...
    def checksum(self, force=...):  # -> str | None:
        """Return checksum if file is small enough, else None.
        Returns None if file does not exist. If force is True,
        omit eligibility check."""
        ...
    def is_same_checksum(self, other_checksum, force=...): ...
    def check_broken_symlink(self):  # -> None:
        """Raise WorkflowError if file is a broken symlink."""
        ...
    @_refer_to_remote
    def is_newer(self, time):  # -> Literal[False]:
        """Returns true of the file (which is an input file) is newer than time, or if it is
        a symlink that points to a file newer than time."""
        ...
    def download_from_remote(self): ...
    def upload_to_remote(self): ...
    def prepare(self): ...
    def protect(self): ...
    def remove(self, remove_non_empty_dir=...): ...
    def touch(self, times=...):  # -> None:
        """times must be 2-tuple: (atime, mtime)"""
        ...
    def touch_or_create(self): ...
    def apply_wildcards(self, wildcards, fill_missing=..., fail_dynamic=...): ...
    def get_wildcard_names(self): ...
    def regex(self): ...
    def wildcard_constraints(self): ...
    def constant_prefix(self): ...
    def constant_suffix(self): ...
    def match(self, target): ...
    def format_dynamic(self): ...
    def clone_flags(self, other): ...
    def clone_remote_object(self, other): ...
    def set_flags(self, flags): ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

_double_slash_regex = ...
_wildcard_regex = ...

def wait_for_files(
    files, latency_wait=..., force_stay_on_remote=..., ignore_pipe_or_service=...
):  # -> None:
    """Wait for given files to be present in the filesystem."""
    ...

def get_wildcard_names(pattern): ...
def contains_wildcard(path): ...
def contains_wildcard_constraints(pattern): ...
def remove(file, remove_non_empty_dir=...): ...
def get_wildcard_constraints(pattern): ...
def regex(filepattern): ...
def apply_wildcards(
    pattern,
    wildcards,
    fill_missing=...,
    fail_dynamic=...,
    dynamic_fill=...,
    keep_dynamic=...,
): ...
def not_iterable(value): ...
def is_callable(value): ...

class AnnotatedString(str):
    def __init__(self, value) -> None: ...
    def new_from(self, new_value): ...

def flag(value, flag_type, flag_value=...): ...
def is_flagged(value, flag): ...
def get_flag_value(value, flag_type): ...
def ancient(value):  # -> AnnotatedString | list[Unknown]:
    """
    A flag for an input file that shall be considered ancient; i.e. its timestamp shall have no effect on which jobs to run.
    """
    ...

def directory(value):  # -> AnnotatedString | list[Unknown]:
    """
    A flag to specify that output is a directory, rather than a file or named pipe.
    """
    ...

def temp(value):  # -> AnnotatedString | list[Unknown]:
    """
    A flag for an input or output file that shall be removed after usage.
    """
    ...

def pipe(value): ...
def service(value): ...
def temporary(value):  # -> AnnotatedString | list[Unknown]:
    """An alias for temp."""
    ...

def protected(value):  # -> AnnotatedString | list[Unknown]:
    """A flag for a file that shall be write-protected after creation."""
    ...

def dynamic(value):  # -> AnnotatedString | list[Unknown]:
    """
    A flag for a file that shall be dynamic, i.e. the multiplicity
    (and wildcard values) will be expanded after a certain
    rule has been run"""
    ...

def touch(value): ...
def ensure(value, non_empty=..., sha256=...): ...
def unpack(value): ...
def repeat(value, n_repeat):  # -> AnnotatedString | list[Unknown]:
    """Flag benchmark records with the number of repeats."""
    ...

def checkpoint_target(value): ...
def sourcecache_entry(value, orig_path_or_uri): ...

ReportObject = ...

def report(
    value,
    caption=...,
    category=...,
    subcategory=...,
    labels=...,
    patterns=...,
    htmlindex=...,
):  # -> AnnotatedString | list[Unknown]:
    """Flag output file or directory as to be included into reports.

    In the case of a directory, files to include can be specified via a glob pattern (default: *).

    Arguments
    value -- File or directory.
    caption -- Path to a .rst file with a textual description of the result.
    category -- Name of the (optional) category in which the result should be displayed in the report.
    subcategory -- Name of the (optional) subcategory
    columns  -- Dict of strings (may contain wildcard expressions) that will be used as columns when displaying result tables
    patterns -- Wildcard patterns for selecting files if a directory is given (this is used as
               input for snakemake.io.glob_wildcards). Pattern shall not include the path to the
               directory itself.
    """
    ...

def local(value):  # -> AnnotatedString | list[Unknown]:
    """Mark a file as a local file. This disables the application of a default remote
    provider.
    """
    ...

def expand(
    filepatterns: Sequence[Path | str] | Path | str,
    func: Callable[[Iterable[str]], Iterable[Iterable[str]]] | None = ...,
    allow_missing: bool | Sequence[str] | str = ...,
    **wildcards: Sequence[str] | str,
) -> list[str]:
    """
    Expand wildcards in given filepatterns.

    Arguments
    *args -- first arg: filepatterns as list or one single filepattern,
        second arg (optional): a function to combine wildcard values
        (itertools.product per default)
    **wildcards -- the wildcards as keyword arguments
        with their values as lists. If allow_missing=True is included
        wildcards in filepattern without values will stay unformatted.
    """
    ...

def multiext(prefix, *extensions):  # -> list[AnnotatedString | list[Unknown]]:
    """Expand a given prefix with multiple extensions (e.g. .txt, .csv, _peaks.bed, ...)."""
    ...

def limit(pattern, **wildcards):
    """
    Limit wildcards to the given values.

    Arguments:
    **wildcards -- the wildcards as keyword arguments
                   with their values as lists
    """
    ...

def glob_wildcards(pattern, files=..., followlinks=...):  # -> Wildcards:
    """
    Glob the values of the wildcards by matching the given pattern to the filesystem.
    Returns a named tuple with a list of values for each wildcard.
    """
    ...

def update_wildcard_constraints(
    pattern, wildcard_constraints, global_wildcard_constraints
):  # -> AnnotatedString | str:
    """Update wildcard constraints

    Args:
      pattern (str): pattern on which to update constraints
      wildcard_constraints (dict): dictionary of wildcard:constraint key-value pairs
      global_wildcard_constraints (dict): dictionary of wildcard:constraint key-value pairs
    """
    ...

def split_git_path(path): ...
def get_git_root(path):
    """
    Args:
        path: (str) Path a to a directory/file that is located inside the repo
    Returns:
        path to the root folder for git repo
    """
    ...

def get_git_root_parent_directory(path, input_path):
    """
    This function will recursively go through parent directories until a git
    repository is found or until no parent directories are left, in which case
    an error will be raised. This is needed when providing a path to a
    file/folder that is located on a branch/tag not currently checked out.

    Args:
        path: (str) Path a to a directory that is located inside the repo
        input_path: (str) origin path, used when raising WorkflowError
    Returns:
        path to the root folder for git repo
    """
    ...

def git_content(git_file):
    """
    This function will extract a file from a git repository, one located on
    the filesystem.
    The expected format is git+file:///path/to/your/repo/path_to_file@version

    Args:
      env_file (str): consist of path to repo, @, version, and file information
                      Ex: git+file:///home/smeds/snakemake-wrappers/bio/fastqc/wrapper.py@0.19.3
    Returns:
        file content or None if the expected format isn't meet
    """
    ...

def strip_wildcard_constraints(pattern):  # -> str:
    """Return a string that does not contain any wildcard constraints."""
    ...

_T = TypeVar("_T")

class Namedlist(List[_T | Iterable[_T]]):
    """
    A list that additionally provides functions to name items. Further,
    it is hashable, however, the hash does not consider the item names.
    """

    def __init__(
        self,
        toclone=...,
        fromdict=...,
        plainstr=...,
        strip_constraints=...,
        custom_map=...,
    ) -> None:
        """
        Create the object.

        Arguments
        toclone  -- another Namedlist that shall be cloned
        fromdict -- a dict that shall be converted to a
            Namedlist (keys become names)
        """
        ...
    def items(self): ...
    def keys(self): ...
    def get(self, key: str, default_value: _T = ...) -> _T: ...
    def __getitem__(self, key: str) -> _T: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...

class InputFiles(Namedlist[_T]):
    @property
    def size(self): ...
    @property
    def size_mb(self): ...

class OutputFiles(Namedlist[_T]): ...
class Wildcards(Namedlist[_T]): ...
class Params(Namedlist[_T]): ...
class Resources(Namedlist[_T]): ...
class Log(Namedlist[_T]): ...

def load_configfile(configpath: str) -> dict[str, Any]:
    "Loads a JSON or YAML configfile as a dict, then checks that it's a dict."
    ...

class PeriodicityDetector:
    def __init__(self, min_repeat=..., max_repeat=...) -> None:
        """
        Args:
            max_repeat (int): The maximum length of the periodic substring.
            min_repeat (int): The minimum length of the periodic substring.
        """
        ...
    def is_periodic(self, value):  # -> str | Any | None:
        """Returns the periodic substring or None if not periodic."""
        ...
