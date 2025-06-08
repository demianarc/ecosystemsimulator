# Ecosystem Simulator

This repository contains a minimal prototype of a generative simulation swarm using the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/).

The demo spins up multiple lightweight agents (founders, VCs and mentors) that interact over a few simulation ticks. Each agent produces a short action which is printed to the console.

## Requirements

* Python 3.12+
* `openai`, `openai-agents`, `fastapi`, and `uvicorn` packages
* An OpenAI API key set in the environment variable `OPENAI_API_KEY`

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Running the demo

Run `python src/simulation.py` to start the simulation. By default it spawns 10 agents and runs three ticks. You can configure the number of agents or steps via command line arguments:

```bash
python src/simulation.py 20 5
```

### Running as a web service

You can also launch a small FastAPI server that exposes the simulation via HTTP:

```bash
uvicorn main:app --reload
```

Then POST to `/simulate` with JSON like `{"num_agents": 5, "steps": 2}` to run a simulation and receive the events.

## Notes

This is a simple starting point for experimentation during a hackathon. You can extend the simulation with vector-store based memory, additional agent roles and more sophisticated world state updates.
