from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

# Predefined knowledge base
knowledge_base = {
    "what does the eligibility verification agent (eva) do?":
        "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.",
    "what does the claims processing agent (cam) do?":
        "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.",
    "how does the payment posting agent (phil) work?":
        "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.",
    "tell me about thoughtful ai's agents.":
        "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.",
    "what are the benefits of using thoughtful ai's agents?":
        "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
}

# Basic style for CLI
style = Style.from_dict({
    '': '#00ff00'
})

def find_answer(user_input):
    normalized_input = user_input.lower().strip()
    if normalized_input in knowledge_base:
        return knowledge_base[normalized_input]
    else:
        return "I'm sorry, I don't have that information yet. But I'm learning more every day!"

def main():
    print("🤖 Welcome to Thoughtful AI Support! Ask me anything about our AI Agents.\nType 'exit' to quit.\n")

    while True:
        try:
            user_input = prompt("You: ", style=style)
            if user_input.lower() in ['exit', 'quit']:
                print("Agent: Goodbye! 👋")
                break
            response = find_answer(user_input)
            print(f"Agent: {response}\n")
        except (KeyboardInterrupt, EOFError):
            print("\nAgent: Goodbye! 👋")
            break

if __name__ == "__main__":
    main()