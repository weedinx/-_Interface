
class GPTAgent:
    def __init__(self, role):
        self.role = role

    def respond(self, prompt):
        return f"{self.role} responding to: {prompt}"

class GPTOperator:
    def __init__(self, agents):
        self.agents = agents

    def debate(self, topic):
        return [agent.respond(topic) for agent in self.agents]
