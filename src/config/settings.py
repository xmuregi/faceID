import os
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FACE_CASCADE_PATH = "public/haar/haarcascade_frontalface_default.xml"


def load_env_file(env_path: Path = PROJECT_ROOT / ".env") -> None:
    if not env_path.exists():
        return

    for line in env_path.read_text().splitlines():
        line = line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def resolve_project_path(path_value: str) -> Path:
    path = Path(path_value)

    if path.is_absolute():
        return path

    return PROJECT_ROOT / path


@dataclass(frozen=True)
class Settings:
    face_cascade_path: Path

    @classmethod
    def from_env(cls) -> "Settings":
        load_env_file()

        return cls(
            face_cascade_path=resolve_project_path(
                os.getenv("FACE_CASCADE_PATH", DEFAULT_FACE_CASCADE_PATH)
            )
        )


settings = Settings.from_env()
