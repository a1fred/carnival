from fabric.transfer import Transfer, Result
from patchwork import files
from patchwork import transfers

from carnival.global_context import conn


def rsync(source, target, exclude=(), delete=False, strict_host_keys=True, rsync_opts='', ssh_opts=''):
    # https://fabric-patchwork.readthedocs.io/en/latest/api/transfers.html#patchwork.transfers.rsync
    return transfers.rsync(
        c=conn,
        source=source,
        target=target,
        exclude=exclude,
        delete=delete,
        strict_host_keys=strict_host_keys,
        rsync_opts=rsync_opts,
        ssh_opts=ssh_opts,
    )


def get(remote: str, local: str, preserve_mode: bool) -> Result:
    # http://docs.fabfile.org/en/2.5/api/transfer.html#fabric.transfer.Transfer.get
    t = Transfer(conn)
    return t.get(remote=remote, local=local, preserve_mode=preserve_mode)


def put(local: str, remote: str, preserve_mode: bool) -> Result:
    # http://docs.fabfile.org/en/2.5/api/transfer.html#fabric.transfer.Transfer.put
    t = Transfer(conn)
    return t.put(local=local, remote=remote, preserve_mode=preserve_mode)


def is_file_contains(filename, text, exact=False, escape=True):
    # https://fabric-patchwork.readthedocs.io/en/latest/api/files.html#patchwork.files.contains
    return files.contains(conn, runner=conn.run, filename=filename, text=text, exact=exact, escape=escape)


def is_file_exists(path) -> bool:
    # https://fabric-patchwork.readthedocs.io/en/latest/api/files.html#patchwork.files.exists
    return files.exists(conn, runner=conn.run, path=path)


def is_dir_exists(path, user=None, group=None, mode=None) -> bool:
    # https://fabric-patchwork.readthedocs.io/en/latest/api/files.html#patchwork.files.directory
    return files.directory(conn, runner=conn.run, path=path, user=user, group=group, mode=mode)
