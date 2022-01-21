# apparel_images
## Content
This dataset contains images separated into multiple categories each containing two descriptors - color and type of clothing.
It can be used in different cloud platforms as shown down below.
To use this dataset, download the repository through the command line.

## How to Use in AWS
1. Upload the images to an AWS S3 bucket at https://aws.amazon.com/s3/. 
2. Head to the AWS Rekognition Console at https://aws.amazon.com/rekognition/ to make a Rekognition Custom Label project.
3. Import the images into the project through the S3 bucket location.
4. Run the model with the associated tags. 

## How to Use in GCP
1. Upload the images to GCS Cloud Storage at https://cloud.google.com/storage.
2. A summary.csv file is contained with this dataset. Modify this csv file with the appropriate file location and upload into Cloud Storage.
3. Head to the GCP Auto ML Vision Console at https://cloud.google.com/automl and create a new project.
4. Import the images through the summary.csv file path in Cloud Storage.
5. Run the model with the associated tags.

## How to Use in Azure
1. Head to the Azure Custom Vision portal at https://www.customvision.ai/.
2. Create a new project and select “Classification” under Project Types.
3. Import the images with their associated tags through the web console.
4. Run the model with the associated tags.
