import boto3
import os
import uuid

def lambda_handler(event, context):
    # Retrieve the S3 bucket and object information from the event
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']
    print(f"{s3_key} and {s3_bucket}")
    # Generate a unique job name and output file name
    job_name = str(uuid.uuid4())
    output_file_name = f"{str(uuid.uuid4())}.txt"
    
    # Create an Amazon Transcribe client
    transcribe_client = boto3.client('transcribe')
    
    # Set the S3 URI for the input audio file
    s3_uri = f"s3://{s3_bucket}/{s3_key}"
    
    # Start the transcription job
    response = transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        LanguageCode='en-US',  # Set the language code if different
        Media={
            'MediaFileUri': s3_uri
        },
        OutputBucketName='OUTPUT_BUCKET_NAME',
        OutputKey=output_file_name
    )
    
    print(f"Transcription job started with name: {job_name}")
    
    return {
        'statusCode': 200,
        'body': response
    }
