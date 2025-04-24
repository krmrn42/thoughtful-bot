# 🤖 Thoughtful AI CLI Support Agent

A simple conversational AI agent built with Python and `prompt_toolkit` that provides support for common questions about Thoughtful AI. The agent uses **vector embeddings** to match user queries with the most relevant predefined answer - even when the question is phrased differently.

## How It Works

This agent uses **semantic search** powered by [Sentence Transformers](https://www.sbert.net/) and [FAISS](https://github.com/facebookresearch/faiss):

1. It **embeds** a list of known questions **and** their corresponding answers into dense vector representations using a transformer model.
2. When a user types a question, the app embeds that query too.
3. It compares the query vector against all stored vectors (questions and answers) using **cosine similarity** (approximated from L2 distance in FAISS).
4. It returns the best-matching **answer**, regardless of whether the query was closer to a question or an answer in the knowledge base.

## Why Vector Embeddings?

Traditional keyword search fails when:
- Users paraphrase questions
- Use synonyms or abbreviations

Embeddings capture the **semantic meaning** of the text, allowing the system to match conceptually similar queries - even if no keywords match.

## Why We Index Both Questions *and* Answers

By indexing both:
- Users who ask questions close to how they were originally written will match the **question embeddings**
- Users who describe details (e.g., "fast reconciliation of patient payments") might match better with **answer content**

This ensures the **most relevant answer is always returned**, regardless of how the user phrases the input.

## Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/thoughtful-ai-cli-agent.git
cd thoughtful-ai-cli-agent
```

### 2. Set up virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # or 'venv\Scripts\activate' on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python main.py
```

## Example Prompts

Try typing these and see the results with similarity scores:

| Prompt                                     | Expected Match                                  | Similarity |
|--------------------------------------------|-------------------------------------------------|------------|
| What is EVA?                               | Eligibility Verification Agent (EVA)            | ~0.5       |
| Can you explain how PHIL helps?            | Payment Posting Agent (PHIL)                    | ~0.4       |
| Reconciliation of patient payments         | PHIL's answer (indexed as an answer)            | ~0.6       |
| Administrative costs and automation        | Benefits of using Thoughtful AI agents          | ~0.5       |
| What do your healthcare bots do?           | Overview of all agents                          | ~0.6       |


## Tech Stack

- **Python 3**
- **prompt_toolkit** for rich CLI input
- **sentence-transformers** for generating embeddings
- **FAISS** for fast similarity search (L2 / cosine)
```
