"""CSP adapter for Matrix, built on chatom."""

__version__ = "0.1.0"

from chatom.matrix import (
    MATRIX_CAPABILITIES,
    MatrixBackend,
    MatrixChannel,
    MatrixConfig,
    MatrixMessage,
    MatrixPresence,
    MatrixPresenceState,
    MatrixUser,
    MockMatrixBackend,
    mention_channel,
    mention_user,
)

from .adapter import MatrixAdapter

__all__ = (
    "MATRIX_CAPABILITIES",
    "MatrixAdapter",
    "MatrixBackend",
    "MatrixChannel",
    "MatrixConfig",
    "MatrixMessage",
    "MatrixPresence",
    "MatrixPresenceState",
    "MatrixUser",
    "MockMatrixBackend",
    "mention_channel",
    "mention_user",
)
