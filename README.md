# Running a Django Rest Framework API on Google Cloud Run 

Using as main database a Cloud SQL Postgres instance and also saving/querying data on BigQuery

️ ⚠️️️️**THIS IS A WORK IN PROGRESS** ⚠️

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/alvarowolfx/cloud-run-django-rest-iot)


### Demo 

Rest API 
![Api](./.github/images/api.png)

Admin Interface
![Admin](./.github/images/admin.png)

### Schematic

* ESP8266 WiFi Microcontroller
* HC-SR04 Ultrasonic Sensor
* Jumpers

![Schematic](./.github/images/Schematic_bb.png)

### References

* https://medium.com/google-cloud/connecting-micropython-devices-to-google-cloud-iot-core-3680e632681e
* https://www.django-rest-framework.org/tutorial/quickstart/
* https://cloud.google.com/sql/docs/postgres/quickstart-proxy-test
* https://github.com/GoogleCloudPlatform/python-docs-samples
* https://cloud.google.com/python/django/kubernetes-engine
* https://medium.com/swlh/say-hello-to-serverless-containers-with-cloud-run-4c32d90330fc
* https://cloud.google.com/run/