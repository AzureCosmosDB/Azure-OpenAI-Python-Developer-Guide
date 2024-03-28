# Overview of AI Concepts

## Large Language Models (LLM)

A Large Language Models (LLM) is a type of AI that can process and produce natural language text. LLMs are "general purpose" AI models trained using massive amounts of data gathered from various sources; like books, articles, webpages, and images to discover patterns and rules of language.

LLMs are complex and built using a neural network architecture. They are trained using large amounts of information, and calculate millions of parameters. From a developer perspective, the APIs expose by Azure OpenAI Service enable the LLMs to be easily integrated into enterprise solutions without requiring knowledge of how to build to train the models.

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
| Describes in natural language the desired model responses. | Highly optimized for specific use cases. |

## Prompting and Prompt Engineering

### What is a prompt?

A prompt is an input or instruction provided to an Artificial Intelligence (AI) model to direct its behavior and produce the desired results. The quality and specificity of the prompt are crucial in obtaining precise and relevant outputs. A well-designed prompt can ensure that the AI model generates the desired information or completes the intended task effectively. Some typical prompts include summarization, question answering, text classification, and code generation.

While there's techniques and patterns used when building an Azure OpenAI solution and writing prompts, the following is a couple simple prompt examples:

- `List the most popular products in the last quarter.`
- `How many customers are located in the state of California?`

#### Guidelines for creating robust prompts

While it can be quick to write basic prompts, it can also be difficult to write more complex prompts to ge the AI to generate the responses necessary. When writing prompts, there are three basic guidelines to follow for creating useful prompts:

- **Show and tell** - Make it clear what response is desired either through instructions, examples, or a combination of the two. When ranking a list of items in alphabetical order or to classifying a paragraph by sentiment, include these details in the prompt to provided to the model.
- **Provide quality data** - When building a classifier or get the model to follow a pattern, make sure there are enough examples. Be sure to proofread the examples. The model is smart enough to resolve basic spelling mistakes and still provide a meaningful response. Conversely, the model might assume the mistakes are intentional, which can affect the response.
- **Check the settings** - Probability settings, such as `Temperature` and `Top P`, control how deterministic the model is in generating a response. When asking for a response where there's only one right answer, a lower value should be specified for these settings. When looking for a response that are not obvious and needs additional creativity, use higher values. The most common mistake users make with these settings is assuming they control "cleverness" or "creativity" in the model response.

### What is prompt engineering

[Prompt engineering](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering) is the iterative process of designing, evaluating, and optimizing prompts to produce consistently accurate responses from language models for a particular problem domain. It involves designing and refining the prompts given to an AI model to achieve the desired outputs. Prompt engineers experiment with various prompts, test their effectiveness, and refine them to improve performance. Performance is measured using predefined metrics such as accuracy, relevance, and user satisfaction to assess the impact of prompt engineering.

### General anatomy of a prompt

context, input, output indicator
There are a several components that are used in the anatomy of constructing AI prompts:

- Input
  - Instructions
  - Primary content
  - Supporting content
  - System message
- Output

#### Input

The Input in prompt engineering is the text or query that is provided to the LLM model. The model will use this prompt as the basis for the completion, or response, that is generated.

##### Instructions

Instructions are likely the most commonly used prompt component. Instructions are simply that: instructions to the model on what to do. While simple in concept, they can be complex in practice.

The following are examples of both simple and more complex instructions:

| Instruction Type | Prompt | Completion |
| :--- | :--- | :--- |
| Simple | Write an introduction for a weekly newsletter. | Welcome to our weekly newsletter. This week we have a special focus on productivity. We'll be sharing tips and tricks on how to be productive in all areas of your life. We hope you enjoy and please share with your friends! |
| Complex | Write an introduction for a weekly newsletter to my company named Contoso. It should mention the great all hands meeting we had last week and thank the team for all their hard work over the tough past few months. | Welcome to Contoso's weekly newsletter! We had a great all hands meeting last week and I want to thank the team for all their hard work over the tough past few months. We're looking forward to a bright future and I'm confident that with our team's dedication and commitment, we will achieve great things. Thank you for being a part of our team and I look forward to working with you all in the coming weeks and months. Sincerely, [Your name]. |
| Complex | Write an introduction for a weekly newsletter, including the following: <br/> - My company is named contoso <br/> - An exuberant greeting <br/> - Thanking the team for their hard work over a couple tough months <br/> - Positive outlook for the coming quarter <br/> - Signed by the SLT | Hello Contoso team! I wanted to take a moment to thank you for all your hard work over the past few months. It's been a tough couple of months, but you've all pulled together and done an amazing job. I'm really proud of you all. Looking ahead to the next quarter, I'm feeling really positive. I think we're going to achieve some great things. Thanks again, The Senior Leadership Team. |

##### Primary Content

Primary content refers to some sort of text that is being processed or transformed by the model. Primary content is typically used in conjunction with instructions. A simple example would be language translation.

| Prompt | Completion |
| :--- | :--- |
| Can you please tell me how to get to the museum? <br/> Translate to French: | `Pouvez-vous s'il vous plaît me dire comment aller au musée?` |

Primary content can also be much longer. For example, the primary content could pass the introduction section of text content that could be hundreds of words long. Additionally, the primary content could be int he form of structured data as well, such as in JSON or TSV format.

##### Supporting Content

Supporting content is information that the model can utilize to influence the output in some way. It differs from primary content in that it is not the main target of task, but it is typically used along with primary content. Common examples include contextual information such as the current date, the name of the user, user preferences, and so on.

The following are example prompts and possible completions to show what a prompt with and without supporting content might look like:

| Supporting Content | Prompt | Completion |
| :--- | :--- | :--- |
| Without | Workshop list:
Title Description <br/> Planning Workshop Kickoff Please join us to kick off our workshop! Hear from our leaders about cross group priorities and learnings for the year ahead. The invitation to this event has already been sent to everyone in […] <br/> Summarize the workshops above, grouped by topic: | Workshop list: <br/> Planning Workshop Kickoff <br/> - Planning Workshop Wrap-up <br/> - Core MeetUp <br/> - Customer <br/> Driven Perspectives <br/> - Impact and Key Focus Areas <br/> - Best practices <br/> - Accelerating app adoption […] |
| With | Workshop list: <br/> Title Description <br/> Planning Workshop Kickoff Please join us to kick off our workshop! Hear from our leaders about cross group priorities and learnings for the year ahead. The invitation to this event has already been sent to everyone in […] <br/> My Important Topics: prompt engineering, search, GPT models <br/> Summarize the workshops above, grouped by my important topics: | 1. Prompt Engineering: <br/> - New prompt engineering tips <br/> - The art of prompt engineering <br/> 2. Search: <br/> - Intro to vector search with embedding <br/> 3. GPT Models: <br/> - Intro to GPT-4 <br/> - GPT-35-Turbo in-depth. |

The above prompt examples are truncated with `[…]` for brevity. Writing similar prompts would contain more text.

##### System message

System message, also called a system prompt, is used by developers of a system to restrict the LLM to a specific set of constraints. This is useful when building enterprise solutions that integrate Azure OpenAI so the AI completion will be restricted to the focus of the enterprise data it's integrated with.

The following is an example system message that could be used to constrain the LLM in an enterprise solution:

```text
You are a helpful, fun and friendly sales assistant for Cosmic Works, a bicycle and bicycle accessories store.

Your name is Cosmo.

You are designed to answer questions about the products that Cosmic Works sells, the customers that buy them, and the sales orders that are placed by customers.

If you don't know the answer to a question, respond with "I don't know."

Only answer questions related to Cosmic Works products, customers, and sales orders.

If a question is not related to Cosmic Works products, customers, or sales orders, respond with "I only answer questions about Cosmic Works
```

#### Output

The Output is the completion, or response, from the LLM returned as a result to the input prompt given. When an input prompt is given, the language model will process the information and generate an output in the form of text. The text response is the output.

## Standard Patterns

### Retrieval Augmentation Generation (RAG)

[Retrieval Augmentation Generation (RAG)](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview) is an architecture that augments the capabilities of a Large Language Model (LLM) like ChatGPT by adding an information retrieval system that provides grounding data. Adding an information retrieval system provides control over grounding data used by an LLM when it formulates a response.

GPT language models can be fine-tuned to achieve several common tasks such as sentiment analysis and named entity recognition. These tasks generally don't require additional background knowledge.

The RAG pattern facilitates bringing private proprietary knowledge to the model so that it can perform Question Answering over this content. Remember that Large Language Models are indexed only on public information. For an enterprise solution, RAG architecture means that the generative AI is constrained to enterprise content sourced from vectorized documents, images, audio, and video.

Because the RAG technique accesses external knowledge sources to complete tasks, it enables more factual consistency, improves the reliability of the generated responses, and helps to mitigate the problem of "_hallucination_".

In some cases, the RAG process involves a technique called vectorization on the proprietary data. The user prompt is compared to the vector store and only the most relevant/matching pieces of information are returned and stuffed into prompt for the LLM to reason over and provide an answer. The next set of demos will go into this further.

### Chain of Thought (CoT)

Instead of splitting a task into smaller steps, with [Chain of Thought (CoT)](https://learn.microsoft.com/azure/ai-services/openai/concepts/advanced-prompt-engineering?pivots=programming-language-chat-completions#chain-of-thought-prompting) the model response is instructed to proceed step-by-step and present all the steps involved. Doing so reduces the possibility of inaccuracy of outcomes and makes assessing the model response easier.

| System message | Prompt | Response |
| :--- | :--- | :--- |
| You are an AI assistant that helps people find information. | Who was the most decorated (maximum medals) individual athlete in the Olympic games that were held at Sydney? Take a step-by-step approach in your response, cite sources and give reasoning before sharing final answer in the below format: ANSWER is: `<name>` | Step 1: Determine the year of the Sydney Olympic games. The Sydney Olympic games were held in the year 2000. <br/>  <br/> Step 2: Find a list of individual athletes who won multiple medals in the 2000 Sydney Olympics. <br/>  <br/> According to the official website of the Olympic Games, there were several individual athletes who won multiple medals in the 2000 Sydney Olympics. Some of the notable names include: <br/> - Ian Thorpe (Australia) - 3 gold, 2 silver, 0 bronze <br/> - Pieter van den Hoogenband (Netherlands) - 2 gold, 0 silver, 2 bronze <br/> - Lenny Krayzelburg (USA) - 3 gold, 0 silver, 0 bronze <br/> - Inge de Bruijn (Netherlands) - 3 gold, 1 silver, 0 bronze <br/>  <br/> Step 3: Determine the athlete with the most medals. After reviewing the list of individual athletes who won multiple medals in the 2000 Sydney Olympics, we can see that the athlete with the most medals is Ian Thorpe from Australia, who won a total of 5 medals (3 gold and 2 silver). <br/>  <br/> Therefore, the ANSWER is: Ian Thorpe. |

### ReAct

Reasoning and Acting (ReAct) leverages LLMs to generate both reasoning traces and task-specific actions. ReAct combines these to allow for greater synergy between the two. Reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external data sources to gather additional information. When using LLMs to answer questions and verify facts, ReAct is used to overcome issues of hallucination and error propagation by interacting with the additional usage of external data sources.

### Others

#### Zero-shot prompting

Zero-shot prompting is what we would consider the “default”. This is when we provide no examples of inputs/expected outputs to the model to work with. We’re leaving it up to the model to decipher what is needed and how to output it from the instructions.

Example:

| Prompt | Completion |
| :--- | :--- |
| Headline: Coach confident injury won't derail Warriors <br/> Topic: | The coach is confident that the injury won't derail the Warriors' season. The team is still focused on their goals and that they will continue to work hard to achieve them. |

#### Few-shot prompting

Few-shot prompting is a technique that enables in-context learning for the LLM by providing examples or further information within the prompt to steer the model to generate a better response. Providing additional information in the prompt helps particularly in areas where the data used to train the model isn't enough to generate the desired output from the model.

Example:

| Prompt | Completion |
| :--- | :--- |
| Headline: Twins' Correa to use opt-out, test free agency <br/> Topic: Baseball <br/> Headline: Qatar World Cup to have zones for sobering up <br/> Topic: Soccer <br/> Headline: Yates: Fantasy football intel for Week 6 <br/> Topic: Football <br/> Headline: Coach confident injury won't derail Warriors <br/> Topic: | Basketball |
