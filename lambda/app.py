import json
import os
import boto3

bedrock = boto3.client("bedrock-agent-runtime", region_name=os.getenv("REGION"))

def handler(event, context):
    path = event.get("path", "")

    if path.endswith("/health"):
        return {"statusCode": 200, "body": json.dumps({"status": "ok"})}

    if path.endswith("/ask"):
        body = json.loads(event.get("body", "{}"))
        question = body.get("question", "No question provided")

        try:
            response = bedrock.retrieve_and_generate(
                input={"text": question},
                retrieveAndGenerateConfiguration={
                    "knowledgeBaseConfiguration": {
                        "knowledgeBaseId": os.getenv("BEDROCK_KB_ID"),
                    },
                    "modelArn": f"arn:aws:bedrock:{os.getenv('REGION')}:foundation-model/{os.getenv('MODEL')}",
                },
            )
            answer = response.get("output", {}).get("text", "No answer generated")
        except Exception as e:
            answer = f"Error: {str(e)}"

        return {"statusCode": 200, "body": json.dumps({"answer": answer})}

    return {"statusCode": 404, "body": json.dumps({"error": "Not Found"})}
