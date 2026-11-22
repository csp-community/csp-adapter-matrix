"""Tests for csp-adapter-matrix."""

import pytest

import csp_adapter_matrix
from csp_adapter_matrix import MatrixAdapter, MatrixBackend, MatrixConfig


def test_exports():
    for name in csp_adapter_matrix.__all__:
        assert getattr(csp_adapter_matrix, name) is not None
    assert isinstance(csp_adapter_matrix.__version__, str)


def test_adapter_wraps_backend():
    adapter = MatrixAdapter(MatrixConfig(homeserver="https://matrix.example.org", user_id="@bot:example.org"))
    assert type(adapter.backend) is MatrixBackend
    assert adapter.backend.config.homeserver == "https://matrix.example.org"


def test_encrypted_adapter_uses_e2ee_backend():
    pytest.importorskip("matrix_sdk_python")
    from chatom.matrix import MatrixE2EEBackend

    adapter = MatrixAdapter(MatrixConfig(homeserver="https://matrix.example.org", user_id="@bot:example.org"), encrypted=True)
    assert isinstance(adapter.backend, MatrixE2EEBackend)
