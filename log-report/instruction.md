There is an access log file in the working directory. Analyze the traffic and generate a JSON report at `/app/report.json` summarizing your findings.

Success criteria:

1. Report file exists at `/app/report.json` and contains valid JSON.
2. The JSON includes a `total_requests` field with the count of all HTTP requests in the log.
3. The JSON includes a `unique_ips` field with the count of distinct client IP addresses.
4. The JSON includes a `top_path` field with the most frequently requested path.

Example output:
```json
{"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}
```