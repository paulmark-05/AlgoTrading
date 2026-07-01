from zipfile import ZipFile

import pytest

from reporting.archive_reporter import ArchiveReporter


def test_archive_reporter_creates_zip(tmp_path):

    source = tmp_path / "report"
    source.mkdir()

    (source / "report.json").write_text(
        "{}",
        encoding="utf-8",
    )

    (source / "report.csv").write_text(
        "Metric,Value",
        encoding="utf-8",
    )

    archive_path = tmp_path / "report.zip"

    reporter = ArchiveReporter()

    result = reporter.archive(
        source_directory=source,
        archive_path=archive_path,
    )

    assert result == archive_path
    assert archive_path.exists()

    with ZipFile(archive_path, "r") as zip_file:
        names = zip_file.namelist()

    assert "report.json" in names
    assert "report.csv" in names


def test_archive_reporter_missing_source():

    reporter = ArchiveReporter()

    with pytest.raises(FileNotFoundError):
        reporter.archive(
            source_directory="missing",
            archive_path="output.zip",
        )