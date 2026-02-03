from agents.orchestrator import Orchestrator

def main():
    user_input = input("Describe your research idea: ")
    orchestrator = Orchestrator()
    result = orchestrator.run(user_input)

if __name__ == "__main__":
    main()
