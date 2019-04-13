#!/bin/bash

# Deploys the project on GCP Run
PROJECT_ID=`gcloud config get-value project`
gcloud beta run deploy --image gcr.io/$PROJECT_ID/tornado-server:v0
