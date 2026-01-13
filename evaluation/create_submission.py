import json
from evaluation.run_agent import results

with open("submission/submission.jsonl", "w") as f:
    for r in results:
        f.write(json.dumps(r) + "\n")
