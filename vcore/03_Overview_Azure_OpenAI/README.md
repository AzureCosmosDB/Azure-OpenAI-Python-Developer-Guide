# Overview of Azure OpenAI

Azure OpenAI is a collaboration between Microsoft Azure and OpenAI, a leading research organization in artificial intelligence. It is a cloud-based platform that enables developers and data scientists to build and deploy AI models quickly and easily. With Azure OpenAI, users can access a wide range of AI tools and technologies to create intelligent applications, including natural language processing, computer vision, and deep learning.

Azure OpenAI is designed to accelerate the development of AI applications, allowing users to focus on creating innovative solutions that deliver value to their organizations and customers.

Here are ways that Azure OpenAI can help developers:

- **Simplified integration** - Simple and easy-to-use APIs for tasks such as text generation, summarization, sentiment analysis, language translation, and more.
- **Pre-trained models** - AI models that are already fine-tuned on vast amounts of data making it easier for developers to leverage the power of AI without having to train their own models from scratch.
- **Customization** - Developers can also fine-tune the included pre-trained models with their own data with minimal coding, providing an opportunity to create more personalized and specialized AI applications.
- **Documentation and resources** - Azure OpenAI provides comprehensive documentation and resources to help developers get started quickly.
- **Scalability and reliability** - Hosted on Microsoft Azure, the OpenAI service provides robust scalability and reliability that developers can leverage to deploy their applications.
- **Responsible AI** - Azure OpenAI promotes responsible AI by adhering to ethical principles, providing explainability tools, governance features, diversity and inclusion support, and collaboration opportunities. These measures help ensure that AI models are unbiased, explainable, trustworthy, and used in a responsible and compliance manner.
- **Community support** - With an active developer community developers can seek help via forums and other community support channels.

## Comparison of Azure OpenAI and OpenAI

Azure OpenAI Service gives customers advanced language AI with OpenAI GPT-4, GPT-3, Codex, DALL-E, and Whisper models with the security and enterprise promise of Azure. Azure OpenAI co-develops the APIs with OpenAI, ensuring compatibility and a smooth transition from one to the other.

With Azure OpenAI, customers get the security capabilities of Microsoft Azure while running the same models as OpenAI. Azure OpenAI offers private networking, regional availability, and responsible AI content filtering.

## Azure OpenAI Data Privacy and Security

Azure OpenAI stores and processes data to provide the service and to monitor for uses that violate the applicable product terms. Azure OpenAI is fully controlled by Microsoft. Microsoft hosts the OpenAI models in Microsoft Azure for the usage of Azure OpenAI, and does not interact with any services operated by OpenAI.

Here are a few important things to know in regards to the security and privacy of prompts (inputs) and completions (outputs), embeddings, and training data when using Azure OpenAI:

- are NOT available to other customers.
- are NOT available to OpenAI.
- are NOT used to improve OpenAI models.
- are NOT used to improve any Microsoft or 3rd party products or services.
- are NOT used for automatically improving Azure OpenAI models for use in the deployed resource (The models are stateless, unless explicitly fine-tuning models with explicitly provided training data).
- Fine-tuned Azure OpenAI models are available exclusively for the account in which it was created.

## Azure AI Platform

Developers can use the power of AI, cloud-scale data, and cloud-native app development to create highly differentiated digital experiences and establish leadership among competitors. Build or modernize intelligent applications that take advantage of industry-leading AI technology and leverage real-time data and analytics to deliver adaptive, responsive, and personalized experiences.

The Azure platform of managed AI, containers, and database services, along with offerings developed by or in partnership with key software vendors, enables developers to build, deploy, and scale applications with speed, flexibility, and enterprise-grade security. This platform has been used by market leaders like The NBA, H&R Block, Real Madrid Football Club, Bosch, and Nuance to develop their own intelligent apps.

Developers can use Azure AI Services, along with other Azure services, to build and modernize intelligent apps on Azure. Examples of this could be:

- Build new with Azure Kubernetes Service or Azure Container Apps, Azure Cosmos DB, and Azure AI Services
- Modernize with Azure Kubernetes Service, Azure SQL or Azure Database for PostgresSQL, and Azure AI Services

### Azure AI Services

While this guide focuses on building intelligent apps using Azure OpenAI combined with vCore-based Azure Cosmos DB for MongoDB, the Azure AI Platform consists of many additional AI services. Each AI service is built to fit a specific AI and/or Machine Learning (ML) need.

Here's a list of the AI services within the [Azure AI platform](https://learn.microsoft.com/azure/ai-services/what-are-ai-services):

| Service | Description |
| --- | --- |
| Azure AI Search | Bring AI-powered cloud search to mobile and web apps |
| Azure OpenAI | Perform a wide variety of natural language tasks |
| Bot Service | Create bots and connect them across channels |
| Content Safety | An AI service that detects unwanted contents |
| Custom Vision | Customize image recognition to fit the business |
| Document Intelligence | Turn documents into usable data at a fraction of the time and cost |
| Face | Detect and identify people and emotions in images |
| Immersive Reader | Help users read and comprehend text |
| Language | Build apps with industry-leading natural language understanding capabilities |
| Machine Learning | ML professionals, data scientists, and engineers can use Azure Machine Learning in their day-to-day workflows to train and deploy models, such as those built from an open-source platform, such as PyTorch, TensorFlow, or scikit-learn |
| Speech | Speech to text, text to speech, translation and speaker recognition |
| Translator | Translate more than 100 languages and dialects |
| Video Indexer | Extract actionable insights from videos |
| Vision | Analyze content in images and videos |

> **Note:** Follow this link for additional tips to help in determining the which Azure AI service is most appropriate for a specific project requirement: <https://azure.microsoft.com/products/category/ai>

The tools that used to customize and configure models are different from those used to call the Azure AI services. Out of the box, most Azure AI services allow for sending data and receive insights without any customization.

For example:

- Sending an image to the Azure AI Vision service to detect words and phrases or count the number of people in the frame
- Sending an audio file to the Speech service and get transcriptions and translate the speech to text at the same time

Azure offers a wide range of tools that are designed for different types of users, many of which can be used with Azure AI services. Designer-driven tools are the easiest to use, and are quick to set up and automate, but might have limitations when it comes to customization. The REST APIs and client libraries provide users with more control and flexibility, but require more effort, time, and expertise to build a solution. When using REST APIs and client libraries, there is an expectation that the developer is comfortable working with modern programming languages like C#, Java, Python, JavaScript, or another popular programming language.

### Azure Machine Learning

[Azure Machine Learning](https://learn.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning?view=azureml-api-2) is a cloud service for accelerating and managing the machine learning (ML) project lifecycle. ML professionals, data scientists, and engineers can use it in their day-to-day workflows to train and deploy models and manage machine learning operations (MLOps).

Azure Machine Learning can be used to create a model or use a model built from an open-source platform, such as PyTorch, TensorFlow, or scikit-learn. Additionally, MLOps tools help monitor, retrain, and redeploy models.

ML projects often require a team with a varied skill set to build and maintain. Azure Machine Learning has tools that help enable:

- Collaboration within a team via shared notebooks, compute resources, serverless compute, data, and environments

- Developing models for fairness and explainability, tracking and auditability to fulfill lineage and audit compliance requirements

- Deploying ML models quickly and easily at scale, and manage and govern them efficiently with MLOps

- Running machine learning workloads anywhere with built-in governance, security, and compliance

Enterprises working in the Microsoft Azure cloud can use familiar security and role-based access control for infrastructure. A project can be set up to deny access to protected data and select operations.

#### Azure Machine Learning vs Azure Open AI

Many of the Azure AI services are suited to a very specific AI / ML need. The Azure Machine Learning and Azure OpenAI services offer more flexible usage based on the solution requirements.

Here are a couple differentiators to help determine which of these to services to use when comparing the two:

- Azure Machine Learning service is appropriate for solutions where a custom model needs to be trained specifically on private data.

- Azure OpenAI service is appropriate for solutions that require pre-trained models that provide natural language processing or vision services, such as the GPT-4 or DALL-E models from OpenAI.

If the solution requires other more task specific AI features, then one of the other Azure AI services should be considered.

### Azure AI Studio

Azure AI Studio is a web portal that brings together multiple Azure AI-related services into a single, unified development environment.

Specifically, Azure AI Studio combines:

- The model catalog and prompt flow development capabilities of Azure Machine Learning service.

- The generative AI model deployment, testing, and custom data integration capabilities of Azure OpenAI service.

- Integration with Azure AI Services for speech, vision, language, document intelligence, and content safety.

Azure AI Studio enables teams to collaborate efficiently and effectively on AI projects, such as developing custom copilot applications that use large language models (LLMs).

![Azure AI Studio screenshot](images/2024-01-23-17-52-46.png)

Tasks accomplished using Azure AI Studio include:

- Deploying models from the model catalog to real-time inferencing endpoints for client applications to consume.
- Deploying and testing generative AI models in an Azure OpenAI service.
- Integrating data from custom data sources to support a retrieval augmented generation (RAG) approach to prompt engineering for generative AI models.
- Using prompt flow to define workflows that integrate models, prompts, and custom processing.
- Integrating content safety filters into a generative AI solution to mitigate potential harms.
- Extending a generative AI solution with multiple AI capabilities using Azure AI services.
