
import os
import time

def respond_to_idea(filename):
    print(f"Processing idea file: {filename}")
    # Aqui entra a lógica do GPT_CRITIC

def watch_and_debate():
    print("Orchestrator started.")
    while True:
        for filename in os.listdir("shared/thoughts"):
            if filename.endswith(".json"):
                respond_to_idea(f"shared/thoughts/{filename}")
        time.sleep(10)
