#!/bin/bash
$SERVICE_NAME=tornado-server # TODO change how we get this
gcloud beta run services delete $SERVICE_NAME
