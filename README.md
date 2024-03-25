This is the final project for the DataTalks Club Data Engineering Zoomcamp 2024.

In this project we will display used car sales in the United States.

Dataset
*******
We will use the Vehicles Sales dataset from Kaggle. The dataset can be found in the URL below:

https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data

After downloading the dataset it was divided into 4 parts because of the gitHub limitation of uploading files up to 25MB each.

The four files can be found in the data folder.

Moving data to a bucket
***********************
First we need to create a GCP bucket. For this we will use terraform which must be installed on our computer. Then we have to modify the main.tf file located in the terraform folder. We are going to make the following changes:

    1. For the provider
        a. Replace the project ID with your GCP project ID
        b. Replace the region with your GCP region
    2. For the bucket
        a. Replace name with your bucket name
        b. Replace the bucket location with your bucket location

We also have to copy our service account json file to the keys directory. Then from the terraform directory we execute:

    terraform init
    terraform plan
    terraform apply

    Type yes and hit Enter.

The bucket is created in our GCP storage.

