import json
from pathlib import Path


def test_report_file_and_json_validity():
    """Criterion 1: Report file exists at /app/report.json and contains valid JSON."""
    report_path = Path("/app/report.json")
    assert report_path.exists(), "report.json not found at /app/report.json"
    
    with open(report_path) as f:
        try:
            json.load(f)
        except json.JSONDecodeError as e:
            raise AssertionError(f"report.json is not valid JSON: {e}")


def test_total_requests_field():
    """Criterion 2: JSON includes total_requests field with the count of all HTTP requests in the log."""
    with open("/app/report.json") as f:
        data = json.load(f)
    
    assert "total_requests" in data, "Missing required field: total_requests"
    assert isinstance(data["total_requests"], int), "total_requests must be an integer"
    assert data["total_requests"] == 6, f"Expected 6 total requests, got {data['total_requests']}"


def test_unique_ips_field():
    """Criterion 3: JSON includes unique_ips field with the count of distinct client IP addresses."""
    with open("/app/report.json") as f:
        data = json.load(f)
    
    assert "unique_ips" in data, "Missing required field: unique_ips"
    assert isinstance(data["unique_ips"], int), "unique_ips must be an integer"
    assert data["unique_ips"] == 3, f"Expected 3 unique IPs, got {data['unique_ips']}"


def test_top_path_field():
    """Criterion 4: JSON includes top_path field with the most frequently requested path."""
    with open("/app/report.json") as f:
        data = json.load(f)
    
    assert "top_path" in data, "Missing required field: top_path"
    assert isinstance(data["top_path"], str), "top_path must be a string"
    assert data["top_path"] == "/index.html", f"Expected '/index.html' as top path, got '{data['top_path']}'"