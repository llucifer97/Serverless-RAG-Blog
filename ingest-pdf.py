import json
import boto3
import base64
import uuid
import os  # NEW
from datetime import datetime

s3 = boto3.client('s3')
bedrock_agent = boto3.client("bedrock-agent")
BUCKET = 'rag-docs-bucket-ayush'

def lambda_handler(event, context):
    body = json.loads(event['body'])
    pdf_base64 = body['pdf_data']
    filename = body.get('filename', f"upload_{uuid.uuid4()}.pdf")
    
    pdf_bytes = base64.b64decode(pdf_base64)
    
    key = f"docs/{datetime.now().strftime('%Y%m%d')}/{filename}"
    s3.put_object(Bucket=BUCKET, Key=key, Body=pdf_bytes, ContentType='application/pdf')
    
    # NEW AUTO-SYNC
    job_resp = bedrock_agent.start_ingestion_job(
        knowledgeBaseId=os.environ['KB_ID'],
        dataSourceId=os.environ['DATA_SOURCE_ID']
    )
    job_id = job_resp['ingestionJob']['ingestionJobId']
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            's3_key': key, 
            'ingestion_job_id': job_id,  # NEW
            'message': 'Uploaded + KB sync started!'
        })
    }
