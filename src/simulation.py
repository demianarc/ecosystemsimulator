import os
import random
from typing import List

from agents import Agent, Runner

DEFAULT_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

class World:
    def __init__(self, agents: List[Agent]):
        self.agents = agents
        self.history = []

    def step(self):
        events = []
        for agent in self.agents:
            context = "\n".join(self.history[-5:])
            result = Runner.run_sync(agent, context)
            action = result.final_output
            msg = f"{agent.name}: {action}"
            events.append(msg)
            self.history.append(msg)
        return events


def create_agents(num_agents: int) -> List[Agent]:
    agents = []
    for i in range(num_agents):
        role = random.choice(["Founder", "VC", "Mentor"])
        instructions = f"You are {role} #{i}. Make short decisions in a startup ecosystem."\
            " Respond with a brief action for this simulation tick."
        agent = Agent(name=f"{role}_{i}", instructions=instructions, model=DEFAULT_MODEL)
        agents.append(agent)
    return agents


def main(num_agents: int = 10, steps: int = 3):
    """Run the simulation with the given number of agents and steps."""
    agents = create_agents(num_agents)
    world = World(agents)
    for step in range(steps):
        print(f"--- Tick {step + 1} ---")
        try:
            events = world.step()
        except Exception as exc:
            print(f"Error running agents: {exc}")
            print("Ensure the OPENAI_API_KEY environment variable is set.")
            return

        for e in events:
            print(e)


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 2:
        num_agents = int(sys.argv[1])
    else:
        num_agents = 10

    if len(sys.argv) >= 3:
        steps = int(sys.argv[2])
    else:
        steps = 3

    main(num_agents, steps)
