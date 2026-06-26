#!/bin/bash
set -euo pipefail

# Create the logs directory for Harbor verifier output
mkdir -p /logs/verifier

# Run tests with JSON CTRF output
pytest /tests/test_outputs.py -rA --ctrf-report=/logs/verifier/ctrf.json

# Report reward to Harbor
if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi