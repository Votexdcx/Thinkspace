import logging
import os
import boto3
import watchtower


def setup_cloudwatch():

    aws_access_key_id = "AKIAXZE4WNHMPE3MEFOH"
    aws_secret_access_key = "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"
    region_name = "eu-west-2"
    log_group = os.getenv("CLOUDWATCH_LOG_GROUP", "django-log-group")
    stream_name = os.getenv("CLOUDWATCH_STREAM_NAME", "django-stream")

    try:
        # Create boto3 client with credentials
        boto3_client = boto3.client(
            "logs",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )

        # Pass boto3 client to watchtower handler
        handler = watchtower.CloudWatchLogHandler(
            boto3_client=boto3_client,
            log_group=log_group,
            stream_name=stream_name,

        )
        logging.getLogger().addHandler(handler)
        logging.getLogger().info("✅ CloudWatch logging initialized.")
    except Exception as e:
        logging.getLogger().error(f"❌ Failed to init CloudWatch logging: {e}")