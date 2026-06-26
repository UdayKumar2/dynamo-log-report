#!/bin/bash
set -euo pipefail

# Run the solution to generate report.json
python /app/solution/solve.py

# Create the logs directory for Harbor verifier output
mkdir -p /logs/verifier

# Run tests
pytest /app/tests/test_outputs.py -v

# Report reward to Harbor
if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi