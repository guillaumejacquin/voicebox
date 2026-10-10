import pytest

from backend.backends.chatterbox_mlx_backend import _delivery_settings


def test_audiobook_delivery_overrides_mlx_defaults() -> None:
    settings = _delivery_settings(
        'audiobook:{"exaggeration":0.66,"cfg_weight":0.62}'
    )

    assert settings["exaggeration"] == 0.66
    assert settings["cfg_weight"] == 0.62
    assert settings["temperature"] == 0.8


def test_audiobook_delivery_rejects_out_of_range_values() -> None:
    with pytest.raises(ValueError, match="Invalid audiobook exaggeration"):
        _delivery_settings('audiobook:{"exaggeration":1.1}')
