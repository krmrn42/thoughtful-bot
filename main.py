from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Knowledge base
knowledge_base = {
    "What does the eligibility verification agent (EVA) do?":
        "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.",
    "What does the claims processing agent (CAM) do?":
        "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.",
    "How does the payment posting agent (PHIL) work?":
        "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.",
    "Tell me about Thoughtful AI's Agents.":
        "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.",
    "What are the benefits of using Thoughtful AI's agents?":
        "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
}

# CLI style
style = Style.from_dict({'': '#00ff00'})

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Prepare dataset for vector search
entries = []
entry_to_answer = []

for q, a in knowledge_base.items():
    entries.append(q)
    entry_to_answer.append(a)
    entries.append(a)
    entry_to_answer.append(a)

# Create vector index
embeddings = model.encode(entries, convert_to_numpy=True)
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def search_response(user_query, top_k=1):
    query_embedding = model.encode([user_query])[0].reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    best_match_idx = indices[0][0]
    return entry_to_answer[best_match_idx]

def main():
    print("🤖 Welcome to Thoughtful AI Support! Ask me anything about our AI Agents.\nType 'exit' to quit.\n")

    while True:
        try:
            user_input = prompt("You: ", style=style)
            if user_input.lower() in ['exit', 'quit']:
                print("Agent: Goodbye! 👋")
                break
            response = search_response(user_input)
            print(f"Agent: {response}\n")
        except (KeyboardInterrupt, EOFError):
            print("\nAgent: Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
