Q1. Explain the difference between a traditional keyword-based search system and a Retrieval-
Augmented Generation (RAG) system. Where would you prefer using RAG over a normal
search pipeline?

A1. Keyword based search just matches exact words in your query to documents, so if the wording doesn't match, you miss relevant results, whereas RAG understands the meaning behind your query, retrieves semantically relevant chunks, and lets the LLM generate a grounded, conversational answer. I'd prefer RAG when dealing with large internal knowledge bases, customer support bots, or any scenario where users ask natural language questions and expect precise, context-aware answers rather than a list of links.



Q2. Suppose you are integrating an LLM into an existing workflow automation system. What
factors would you consider before deploying it into production?

A2. Before pushing an LLM into production, I'd evaluate things like response accuracy, latency, and how often it hallucinates, along with cost per API call and how well it handles edge cases or unexpected inputs. I'd also make sure there's proper logging, fallback mechanisms, and human in the loop checks wherever the stakes are high, because an LLM failing silently in an automated workflow can cause real damage.



Q3. Describe a technical project (academic, internship, freelance, or personal) where you built or
contributed to a software application. What challenges did you face and how did you solve them?

A3. I built a Full Stack Web app where the biggest challenge was managing state across multiple components while keeping the UI in sync with real time backend responses. It got messy fast. I solved it by restructuring the data flow, lifting state up to a common parent, and using proper API response handling, which made the whole system significantly cleaner and more predictable.