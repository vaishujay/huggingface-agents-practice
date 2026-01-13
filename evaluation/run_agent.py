from datasets import load_dataset
from agent.agent import solve

dataset = load_dataset("gaia-benchmark/GAIA", split="dev")

level1 = [q for q in dataset if q["level"] == 1][:20]

results = []

for q in level1:
    answer = solve(q["question"])
    results.append({
        "task_id": q["task_id"],
        "model_answer": answer
    })

print(results)
