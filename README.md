
---
title: Fuel Crisis Allocation Environment
emoji: 🔥
colorFrom: red
colorTo: yellow
sdk: docker
app_file: app.py
pinned: false
---



## 🔗 Deployment Links

### 🌐 Hugging Face Space

https://ayush7662-fuelenv.hf.space

---

### 💻 GitHub Repository

https://github.com/ayush7662/fuel_crisis_env

---

### 📄 API Documentation (Swagger UI)

https://ayush7662-fuelenv.hf.space/docs

---

## 🧪 How to Test

1. Open the API Docs link
2. Use `/reset` to initialize environment
3. Use `/step` to send allocation action
4. Use `/state` to check current state

---

## ✅ Status

✔ Fully deployed on Hugging Face
✔ OpenEnv compliant
✔ APIs working (`/reset`, `/step`, `/state`)
✔ Inference script reproducible
✔ Dockerized environment

---





# Fuel Crisis Allocation Environment (OpenEnv)

## Overview

This project implements an **OpenEnv-compatible environment** that simulates a **fuel crisis scenario during geopolitical conflict**. In situations such as global tensions involving oil-producing regions, petroleum supply chains can be disrupted. Governments must allocate limited fuel resources across critical sectors.

This environment models that decision-making process and evaluates how well an agent distributes fuel among essential services.

The environment is designed to test **resource allocation strategies** under constrained supply and competing demand.

---

## Problem Statement

During geopolitical conflicts, disruptions in oil and LPG supply can create severe shortages. Governments must prioritize critical sectors such as:

* Hospitals and emergency services
* Public transportation and logistics
* Civilian/public usage

The goal of the agent is to **allocate limited fuel resources efficiently** while maximizing societal impact.

---

## Environment Design

### Observation

The environment returns the current fuel supply and demand from different sectors.

Example observation:

```
{
  "fuel_available": 1000,
  "requests": {
    "hospital": 300,
    "transport": 300,
    "public": 200
  },
  "urgency": "low"
}
```

Fields:

* **fuel_available** — total fuel available for allocation
* **requests** — demand from each sector
* **urgency** — crisis severity level

---

### Action

The agent must decide how much fuel to allocate to each sector.

Example action:

```
{
  "allocations": {
    "hospital": 300,
    "transport": 200,
    "public": 100
  }
}
```

Constraints:

* Total allocation cannot exceed available fuel.
* Prioritization of critical sectors is encouraged.

---

### Reward

The reward is a score between **0.0 and 1.0** based on how well the allocation meets demand.

Evaluation considers:

* Meeting hospital demand
* Supporting transportation infrastructure
* Remaining fuel distribution fairness

Higher scores represent more effective resource allocation.

---

## Tasks


The environment contains **three tasks with increasing difficulty**:

| Task   | Description                                 |
| ------ | ------------------------------------------- |
| Easy   | Sufficient fuel supply with moderate demand |
| Medium | Balanced demand and limited fuel            |
| Hard   | Severe shortage requiring prioritization    |

---

## Project Structure

```
fuel_crisis_env/
│
├── env/
│   ├── core.py
│   ├── models.py
│   └── tasks.py
│
├── app.py
├── inference.py
├── openenv.yaml
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Running Locally

### Install dependencies

```
pip install -r requirements.txt
```

---

### Start the API server

```
uvicorn app:app --reload
```

---

### Test the environment

Reset environment:

```
curl -X POST http://localhost:7860/reset
```

Take a step:

```
curl -X POST http://localhost:7860/step \
-H "Content-Type: application/json" \
-d '{"allocations":{"hospital":300,"transport":200,"public":100}}'
```

---

## Running Inference

Run the evaluation script:

```
python inference.py
```

Example output:

```
easy 0.8
medium 0.6
hard 0.6
```

This script runs a simple rule-based allocation policy that prioritizes hospitals and essential services.

---

## Docker Usage

Build container:

```
docker build -t fuel-env .
```

Run container:

```
docker run -p 7860:7860 fuel-env
```

---

## OpenEnv Compatibility

The environment implements the required endpoints:

* `/reset`
* `/step`
* `/state`

It follows the **OpenEnv specification** and can be validated using:

```
openenv validate
```

---

## Use Cases

This environment can be used for:

* Reinforcement learning experiments
* Resource allocation policy evaluation
* Crisis response simulations
* AI planning research

---

## Conclusion

This project demonstrates how AI agents can assist in **decision-making during fuel shortages caused by geopolitical crises**. By simulating constrained supply and competing demand, the environment encourages development of strategies that prioritize critical infrastructure and maximize societal benefit.
