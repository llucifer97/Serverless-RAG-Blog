# Serverless-RAG-Blog

![Serverless RAG Blog Factory](./Serverless_RAG_Blog_Factory_with_AWS_Service_Icons.png)

## ✨ Project Highlights

- 🚀 **End-to-end Serverless RAG Blog Factory**  
  Transform raw PDFs into grounded, long-form blog posts using an AWS-native Retrieval-Augmented Generation (RAG) pipeline. [memory:196]

- 🧠 **Powered by Amazon Bedrock Knowledge Bases**  
  Uses Bedrock KBs to automatically chunk, embed (Titan embeddings), and index documents into a managed OpenSearch vector store, so every blog is generated from your own content—not generic web data. [web:35][memory:196]

- ☁️ **Fully Serverless Backend**  
  - **Amazon API Gateway** exposes clean REST endpoints (`/upload`, `/blog`) for both UI and external clients.  
  - **AWS Lambda (Python 3.12)** handles PDF uploads, auto-ingestion, RAG calls, and S3 writes with pay-per-use scalability. [memory:197]  

- 📂 **Smart Document Ingestion & Auto-Sync**  
  - Upload PDFs via the UI or API; they’re stored in S3 with a date-based folder structure for easy organization.  
  - After each upload, a Lambda automatically triggers `StartIngestionJob` on the Bedrock Knowledge Base so new docs are indexed without any manual sync. [memory:196]

- 📝 **Grounded Blog Generation API**  
  - A dedicated Lambda calls Bedrock’s `RetrieveAndGenerate` API over the Knowledge Base to create 400–600 word blog posts tied to your documents.  
  - Generated blogs are saved back to S3 with timestamped keys, making them easy to list, audit, and reuse. [memory:196][web:37]

- 💻 **Streamlit UI on EC2**  
  - A lightweight Streamlit app running on an EC2 instance provides a simple UI:  
    - Step 1: Upload a PDF.  
    - Step 2: Enter a topic.  
    - Step 3: Get a full, grounded blog rendered directly in the browser.  
  - Perfect for demos, non-technical users, and interview walk-throughs. [memory:190]

- 🧩 **Clean, Modern AWS Stack**  
  - **Compute:** Lambda, EC2 (Streamlit)  
  - **API Layer:** API Gateway  
  - **AI/RAG:** Amazon Bedrock Knowledge Bases + foundation model (e.g., Claude / Titan-based flow)  
  - **Storage:** S3 (source PDFs + generated blogs)  
  - Designed to be low-ops, cost-efficient, and easy to extend with auth, agents, or CI/CD later. [memory:201][web:37]

- 📌 **Resume-Ready Story**  
  - *“Designed and implemented a serverless GenAI application on AWS (S3, Lambda, API Gateway, Bedrock Knowledge Bases, EC2/Streamlit) that auto-ingests PDFs and generates RAG-grounded blogs from user prompts, showcasing production-style GenAI orchestration.”* [memory:201]
