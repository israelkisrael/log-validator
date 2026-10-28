import pytest
from unittest.mock import mock_open

from validator import validate_log_line, validate_log_file, get_text_file_validation_summary

def test_validate_log_line_success():
    line = "2026-10-28 10:00:00 INFO System started succesfully"
    assert validate_log_line(line) == True

def test_validate_log_line_failure():
    line = "2026-10-28 10:00:22 ERROR Database connection timeout"
    assert validate_log_line(line) == False

def test_get_text_file_validation_summary():
    """Checking if the method returns the right path."""
    dummy_summary = {
        "line_count": 10,
        "valid_lines": 8,
        "errors_found": 2
    }

    path = get_text_file_validation_summary(dummy_summary)

    assert path == "validation_summary_file.txt"

    with open(path, 'r') as file:
        content = file.read()

    assert "Total Lines Processed: 10" in content
    assert "Valid Lines: 8" in content
    assert "Error Lines: 2" in content


def test_validate_log_file_not_found():

    with pytest.raises(FileNotFoundError):
        validate_log_file("non_existent_file_12345.log")


def test_validate_log_file_is_a_directory(tmp_path):

    with pytest.raises(IsADirectoryError):
        validate_log_file(tmp_path)


def test_validate_log_file_permission_error(monkeypatch):

    m = mock_open()
    m.side_effect = PermissionError

    monkeypatch.setattr("builtins.open", m)

    with pytest.raises(PermissionError):
        validate_log_file("secret_log.log")