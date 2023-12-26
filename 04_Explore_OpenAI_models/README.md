# Explore the Azure OpenAI models and endpoints (console app)

## Azure OpenAI Models

Azure OpenAI is powered by a diverse set of models with different capabilities.

| Model | Description |
| -- | --- |
| GPT-4 | A set of models that improve on GPT-3.5 and can understand and generate natural language and code. |
| GPT-3.5 | A set of models that improve on GPT-3 and can understand and generate natural language and code. |
| Embeddings | A set of models that can convert text into numerical vector form to facilitate text similarity. |
| DALL-E | A series of models in preview that can generate original images from natural language. |
| Whisper | A series of models in preview that can transcribe and translate speech to text. |

### GPT-4 and GPT-3.5 Models

GPT-4 can solve difficult problems with greater accuracy than any of OpenAI's previous models. Like GPT-3.5 Turbo, GPT-4 is optimized for chat and works well for traditional completions tasks.

The GPT-35-Turbo and GPT-4 models are language models that are optimized for conversational interfaces. The models behave differently than the older GPT-3 models. Previous models were text-in and text-out, meaning they accepted a prompt string and returned a completion to append to the prompt. However, the GPT-35-Turbo and GPT-4 models are conversation-in and message-out. The models expect input formatted in a specific chat-like transcript format, and return a completion that represents a model-written message in the chat. While this format was designed specifically for multi-turn conversations, you'll find it can also work well for non-chat scenarios too.

https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/chatgpt?tabs=python&pivots=programming-language-chat-completions

https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/llm-models

https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models

### DALL-E

The DALL-E model, enables the use of a text prompt provided by a user as the input that the model then uses to generate an image response.

## Selecting an LLM

Before a Large Language Model (LLM) can be implemented into a solution, an LLM model must be chosen.





## Explore and use models from code

- Completions
- Chat completions



## Do I use an out-of-the-box model or a fine-tuned model?

## Use the embeddings model to vectorize data
