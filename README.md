# Reptile Enlosure Backend 

## About
This is the AWS bakend portion of a proof-of-concept system for monitoring reptile enclosures. This monitoring system is my senior project submission for Cal Poly, and was completed during the 2020-2021 academic year. The project was advised by Dr. Theresa Migler and is in partial fulfillment of the requirements for the degree of B.S. .

The repository for the mobile application for the proejct can be found [here](https://github.com/CharlesAMiller/Reptile-Monitor). The monitoring system's repository can be found [here](https://github.com/CharlesAMiller/Reptile-Monitoring-Enclosure).

## Details
This repository outlines how the AWS Backend for the project should be configured. 

### Structure

* `DynamoDB/` - Screenshots and information relating to how the DynamoDB tables were configured/named, and what the items are expected to look like.
* `IoT-Core/` - Information about how the IoT Core rules should be configured, and how their actions are set up.
* `Lambda/` - The code for the custom Lambda Functions.
* `API-Gateway/` - The exported configuration for the project's API Gateway. Requires some modifications of URI paths to be performed.
* `docs/` - Misc docs that describe various parts of the backend..


