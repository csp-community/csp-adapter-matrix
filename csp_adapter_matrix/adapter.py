"""Matrix CSP adapter using chatom's Matrix backends."""

from chatom.csp import BackendAdapter
from chatom.matrix import MatrixBackend, MatrixConfig

__all__ = ("MatrixAdapter",)


# chatom declares BackendAdapter conditionally: a placeholder function when csp is
# missing, the real class otherwise. csp is a hard dependency here, so it is always
# the class at runtime, but ty sees the union of both branches.
class MatrixAdapter(BackendAdapter):  # ty: ignore[invalid-base]
    """CSP adapter for Matrix, wrapping a chatom Matrix backend.

    ``subscribe()`` returns a time series of incoming messages and ``publish()``
    sends them. With ``encrypted=True`` the adapter uses chatom's
    ``MatrixE2EEBackend`` so it can read and post in end-to-end encrypted rooms;
    that needs the ``e2ee`` extra and ``config.store_path``.
    """

    def __init__(self, config: MatrixConfig, encrypted: bool = False):
        if encrypted:
            from chatom.matrix import MatrixE2EEBackend

            backend = MatrixE2EEBackend(config=config)
        else:
            backend = MatrixBackend(config=config)
        super().__init__(backend)
