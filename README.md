# S3 Client Tool

This repository contains a Python script to connect and interact with Amazon S3 using the Boto library.
Prerequisites

Before running the script, make sure you have the following:
AWS account and credentials (access key and secret key)
An S3 bucket name and endpoint

#Installation

Clone the repository to your local machine.
Install the Boto3 library using pip:

```pip install boto3```

# Usage

Open the script s3_client.py in a code editor.

Update the following variables in the s3Controller() function:
S3_ACCESS_KEY: Your S3 access key.
S3_SECRET_KEY: Your S3 secret key.
endpoint: The endpoint URL of your S3 bucket.
is_secure: Set to False if SSL is not available, otherwise set to True.
port: The port to use, defaults to 80.

# Run the script in your command line:

```python s3_client.py```

#Follow the instructions in the terminal to use the tool. You can:
Upload an object to the bucket.
Get a list of objects in the bucket.
Get a list of all buckets.

#Note

Make sure to keep your S3 access key and secret key confidential.
If you are using SSL, make sure to set is_secure to True.
If you are not using SSL, make sure to set is_secure to False.
Make sure you have the necessary permissions to access your S3 bucket.
