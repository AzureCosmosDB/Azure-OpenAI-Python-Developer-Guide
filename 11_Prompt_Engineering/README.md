# Prompt engineering

- Add LangChain to project
- Manage system and user prompts
- Manage contextual data
- Create a flow that communicates with the deployed Azure OpenAI and Azure Cosmos DB services
- Implement a web search plugin

## What is a prompt

A prompt is an input or instruction provided to an Artificial Intelligence (AI) model to direct its behavior and produce the desired results. The quality and specificity of the prompt are crucial in obtaining precise and relevant outputs. A well-designed prompt can ensure that the AI model generates the desired information or completes the intended task effectively. Some typical prompts include summarization, question answering, text classification, and code generation.

## What is prompt engineering

Prompt engineering is the iterative process of designing, evaluating, and optimizing prompts to produce consistently accurate responses from language models for a particular problem domain. It involves designing and refining the prompts given to an AI model to achieve the desired outputs. Prompt engineers experiment with various prompts, test their effectiveness, and refine them to improve performance. Performance is measured using predefined metrics such as accuracy, relevance, and user satisfaction to assess the impact of prompt engineering.

## General anatomy of a prompt

Instruction, context, input, output indicator

## Zero-shot prompting

Zero-shot prompting is what we would consider the “default”. This is when we provide no examples of inputs/expected outputs to the model to work with. We’re leaving it up to the model to decipher what is needed and how to output it from the instructions.

## Few-shot prompting

Few-shot prompting provides examples to guide the model to the desired output.

## RAG

GPT language models can be fine-tuned to achieve several common tasks such as sentiment analysis and named entity recognition. These tasks generally don't require additional background knowledge.

The RAG pattern facilitates bringing private proprietary knowledge to the model so that it can perform Question Answering over this content. Remember that Large Language Models are indexed only on public information.
Because the RAG technique accesses external knowledge sources to complete tasks, it enables more factual consistency, improves the reliability of the generated responses, and helps to mitigate the problem of "hallucination".

In some cases, the RAG process involves a technique called vectorization on the proprietary data. The user prompt is compared to the vector store and only the most relevant/matching pieces of information are returned and stuffed into prompt for the LLM to reason over and provide an answer.

## Chain of thought
## ReAct

## Lab
### Diagram RAG using Azure Cosmos DB for MongoDB vCore as a retriever
### Using Azure Cosmos DB for MongoDB vCore as a retriever
### Sample prompts

