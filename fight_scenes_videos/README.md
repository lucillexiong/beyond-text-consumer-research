# fight_scenes_videos
## Content
This dataset contains videos separated into two tags - fight scenes and non fight scences.
It can be used in different cloud platforms as shown down below.
To use this dataset, download the repository through the command line.

## How to Use in GCP
1. Upload the videos to GCS Cloud Storage at https://cloud.google.com/storage.
2. A summary.csv file is contained with this dataset along with a test.csv and train.csv. Modify these csv files with the approporiate Cloud Storage file paths.
3. Head to the GCP AutoML Video Classification at https://cloud.google.com/automl and create a new project.
4. Import the videos through the summary.csv file path in Cloud Storage.
5. Run the model with the associated tags.

## How to Use in AWS
1. Upload the videos to an AWS S3 at https://aws.amazon.com/s3/.
2. Create an SNS topic and SQS queue.
3. Configure user access for AWS Rekognition Video to the SNS topic.
4. Use the sample code to access the label detection operation for each video in the S3 bucket.