# Overview of AI Concepts


## Large Language Models (LLM)

A Large Language Models (LLM) is a type of AI that can process and produce natural language text. LLMs are "general purpose" AI models trained using massive amounts of data gathered from various sources; like books, articles, webpages, and images to discover patterns and rules of language.

Understanding the capabilities of what an LLM can do is important when deciding to use it for a solution:

- **Understand language** - An LLM is a predictive engine that pulls patterns together based on pre-existing text to produce more text. It doesn't understand language or math.
- **Understand facts** - An LLM doesn't have separate modes for information retrieval and creative writing; it simply predicts the next most probable token.
- **Understand manners, emotion, or ethics** - An LLM can't exhibit anthropomorphism or understand ethics. The output of a foundational model is a combination of training data and prompts.

### Foundational Models

Foundational Models are specific instances or versions of an LLM. Examples of these would be GPT-3, GPT-4, or Codex. Foundational models are trained and fine-tuned on a large corpus of text, or code in the case of a Codex model instance.

A foundational model takes in training data in all different formats and uses a transformer architecture to build a general model. Adaptions and specializations can be created to achieve certain tasks via prompts or fine-tuning.

### Difference between LLM and traditional Natural Language Processing (NLP)

LLMs and Natural Language Processing (NLP) differs in their approach to understanding and processing language.

Here are a few things that separate NLPs from LLMs:

| Traditional NLP | Large Language Models |
| --- | --- |
| One model per capability is needed. | A single model is used for many natural language use cases. |
| Provides a set of labeled data to train the ML model. | Uses many terabytes of unlabeled data in the foundation model. |
| Describes in natural language what you want the model to do. | Highly optimized for specific use cases. |


https://learn.microsoft.com/en-us/training/modules/introduction-large-language-models/2-understand-large-language-models



## Standard Patterns

### Retrieval Augmentation Generation (RAG)

Retrieval Augmentation Generation (RAG) is an architecture that augments the capabilities of a Large Language Model (LLM) like ChatGPT by adding an information retrieval system that provides grounding data. Adding an information retrieval system gives you control over grounding data used by an LLM when it formulates a response. For an enterprise solution, RAG architecture means that you can constrain generative AI to your enterprise content sourced from vectorized documents, images, audio, and video.

GPT language models can be fine-tuned to achieve several common tasks such as sentiment analysis and named entity recognition. These tasks generally don't require additional background knowledge.

The RAG pattern facilitates bringing private proprietary knowledge to the model so that it can perform Question Answering over this content. Remember that Large Language Models are indexed only on public information.
Because the RAG technique accesses external knowledge sources to complete tasks, it enables more factual consistency, improves the reliability of the generated responses, and helps to mitigate the problem of "hallucination".

In some cases, the RAG process involves a technique called vectorization on the proprietary data. The user prompt is compared to the vector store and only the most relevant/matching pieces of information are returned and stuffed into prompt for the LLM to reason over and provide an answer. The next set of demos will go into this further.

https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview

### Chain of Thought (CoT)

Instead of splitting a task into smaller steps, with Chain of Though (CoT) the model response is instructed to proceed step-by-step and present all the steps involved. Doing so reduces the possibility of inaccuracy of outcomes and makes assessing the model response easier.

https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering?pivots=programming-language-chat-completions#chain-of-thought-prompting

### ReAct

### Others?

#### Zero-shot prompting

Zero-shot prompting is what we would consider the “default”. This is when we provide no examples of inputs/expected outputs to the model to work with. We’re leaving it up to the model to decipher what is needed and how to output it from the instructions.

#### Few-shot prompting

Few-shot prompting provides examples to guide the model to the desired output.

https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering?pivots=programming-language-chat-completions#provide-grounding-context


## Vectorization and Vector Search

What are you trying to solve with finding relevant data through vector?

## Prompt Engineering

### What is a prompt

A prompt is an input or instruction provided to an Artificial Intelligence (AI) model to direct its behavior and produce the desired results. The quality and specificity of the prompt are crucial in obtaining precise and relevant outputs. A well-designed prompt can ensure that the AI model generates the desired information or completes the intended task effectively. Some typical prompts include summarization, question answering, text classification, and code generation.

Simple examples of prompts:

- _""_
- _""_

### What is prompt engineering

Prompt engineering is the iterative process of designing, evaluating, and optimizing prompts to produce consistently accurate responses from language models for a particular problem domain. It involves designing and refining the prompts given to an AI model to achieve the desired outputs. Prompt engineers experiment with various prompts, test their effectiveness, and refine them to improve performance. Performance is measured using predefined metrics such as accuracy, relevance, and user satisfaction to assess the impact of prompt engineering.

### General anatomy of a prompt

Instruction, context, input, output indicator

https://learn.microsoft.com/en-us/semantic-kernel/prompts/

https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering

https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/

https://learn.microsoft.com/en-us/training/modules/introduction-large-language-models/3-large-language-model-core-concepts

