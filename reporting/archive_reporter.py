from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


class ArchiveReporter:

    def archive(
        self,
        *,
        source_directory: str | Path,
        archive_path: str | Path,
    ) -> Path:

        source_directory = Path(source_directory)
        archive_path = Path(archive_path)

        if not source_directory.exists():
            raise FileNotFoundError(source_directory)

        archive_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with ZipFile(
            archive_path,
            "w",
            ZIP_DEFLATED,
        ) as zip_file:

            for file_path in source_directory.rglob("*"):

                if file_path.is_file():
                    zip_file.write(
                        file_path,
                        file_path.relative_to(source_directory),
                    )

        return archive_path