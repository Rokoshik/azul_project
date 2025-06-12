import subprocess
import json
import csv
import os
import sys
import pytest

CLI_SCRIPT = os.path.join(os.path.dirname(
    __file__), '..', 'azul', 'process_reporter.py')


def run_cli(args):
    """Run CLI with given args, return (stdout, stderr)."""
    result = subprocess.run(
        [sys.executable, CLI_SCRIPT] + args,
        capture_output=True,
        text=True
    )
    return result.stdout, result.stderr, result.returncode


def test_cli_help():
    stdout, stderr, code = run_cli(['--help'])
    assert code == 0
    assert "usage" in stdout.lower()


def test_generate_csv_report(tmp_path):
    output_file = tmp_path / "report.csv"
    stdout, stderr, code = run_cli(
        ['--output-format', 'csv', '--output', str(output_file)])
    assert code == 0
    assert output_file.exists()

    # Check CSV content has expected columns
    with open(output_file, newline='') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        assert "pid" in headers
        assert "name" in headers
        assert "username" in headers
        assert "cpu_percent" in headers
        assert "memory_usage" in headers


def test_generate_json_report(tmp_path):
    output_file = tmp_path / "report.json"
    stdout, stderr, code = run_cli(
        ['--output-format', 'json', '--output', str(output_file)])
    assert code == 0
    assert output_file.exists()

    with open(output_file) as f:
        data = json.load(f)
    assert isinstance(data, list)
    if data:
        item = data[0]
        assert "pid" in item
        assert "name" in item
        assert "username" in item
        assert "cpu_percent" in item
        assert "memory_usage" in item
