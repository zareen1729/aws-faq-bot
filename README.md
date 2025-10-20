# AWS FAQ Bot 🤖

This project builds an **AI-powered FAQ Assistant** using **Amazon Bedrock**, **AWS Lambda**, and **API Gateway** — all deployed with AWS CDK.

---

## 🚀 What You’ll Build

An API with two endpoints:

- `/health` — Health check
- `/ask` — Accepts a question and returns a Bedrock-powered contextual answer

### Components
- **AWS Lambda (Python 3.12)** — Runs chatbot logic  
- **Amazon Bedrock Knowledge Base** — Provides context retrieval  
- **Amazon API Gateway** — Exposes endpoints  
- **Amazon S3** — Stores FAQ documents  
- **AWS CDK** — Deploys all resources

---

## 🧠 Step-by-Step Implementation

### 1️⃣ Create the Knowledge Base
1. Go to **Amazon Bedrock → Knowledge Bases → Create**
2. Choose **Titan Embeddings**
3. Connect your **S3 data source** (text/Markdown)
4. Copy `KnowledgeBaseId` and `DataSourceId`

### 2️⃣ Clone Repository
```bash
git clone https://github.com/zareen1729/aws-faq-bot.git
cd aws-faq-bot
```

### 3️⃣ Setup Environment
```bash
cp env.template .env
# Fill your real values
```

Example `.env`:
```
BEDROCK_KB_ID=kb-xxxx
REGION=us-west-2
MODEL=amazon.titan-text-lite
```

Install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4️⃣ Deploy the Stack
```bash
cdk bootstrap
cdk deploy
```

After a few minutes, get your endpoint like:
```
https://<api_id>.execute-api.us-west-2.amazonaws.com/prod
```

### 5️⃣ Test the API
Check health:
```bash
curl https://<api_url>/prod/health
```

Ask a question:
```bash
curl -X POST https://<api_url>/prod/ask   -H "Content-Type: application/json"   -d '{"question": "What are the refund policies?"}'
```

Response:
```json
{"answer": "Based on our internal FAQ, refunds are processed within 5-7 business days."}
```

---

## 🧩 Lessons Learned

- **IAM permissions** are critical for Lambda to call Bedrock.
- **Region alignment** between model, KB, and Lambda is essential.
- **Containerized Lambda** is useful if dependencies grow large.

---

## 📂 Repo Structure
```
aws-faq-bot/
├── cdk/
│   ├── app.py
│   ├── faq_stack.py
│   ├── requirements.txt
├── lambda/
│   ├── app.py
│   ├── requirements.txt
│   ├── __init__.py
├── env.template
├── README.md
├── architecture.png
```

---

## 🧱 Architecture
See `architecture.png`

---

## 👏 Author
**Zareen Khan**  
DevOps | SRE | AWS Enthusiast | AI Explorer  
📍 California, USA
