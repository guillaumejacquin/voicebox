from pathlib import Path


def test_server_image_installs_cpu_only_torch() -> None:
    dockerfile = Path(__file__).parents[1] / "Dockerfile.server"
    contents = dockerfile.read_text(encoding="utf-8")

    assert "https://download.pytorch.org/whl/cpu" in contents
    assert '"torch==2.9.1+cpu"' in contents
    assert '"torchaudio==2.9.1+cpu"' in contents
    assert (
        "pip install --no-cache-dir --no-deps "
        "git+https://github.com/QwenLM/Qwen3-TTS.git"
    ) in contents
