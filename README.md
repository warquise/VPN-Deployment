
# VPN Deployment Project on AWS
# AWS OpenVPN Deployment Guide

This guide provides step-by-step instructions on how to deploy OpenVPN on Amazon Web Services (AWS) using an EC2 instance.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Launching an EC2 Instance](#launching-an-ec2-instance)
3. [Installing OpenVPN](#installing-openvpn)
4. [Accessing the OpenVPN Admin UI](#accessing-the-openvpn-admin-ui)
5. [Configuring OpenVPN](#configuring-openvpn)
6. [Connecting to Your VPN](#connecting-to-your-vpn)

## Prerequisites

- An AWS account
- Basic knowledge of AWS and Linux
- SSH client for connecting to the EC2 instance

## Launching an EC2 Instance

1. Log in to the AWS Management Console.
2. Navigate to the EC2 Dashboard and click on `Launch Instance`.
 ![image](https://github.com/warquise/VPN-Deployment/assets/160808546/5b3cf88c-59dd-4f4e-9e70-03ce7f7e0c5f)
3. Choose an Amazon Machine IMAGE(AMI) and search for OPENVPN and select the OPENVPN ACCESS Server. 
   ![image](https://github.com/warquise/VPN-Deployment/assets/160808546/a9448878-a133-49c1-9ab4-49458e767034)

4. Select an instance type. `t2.micro` is sufficient for this tutorial and is free-tier eligible.
![image](https://github.com/warquise/VPN-Deployment/assets/160808546/7c725d31-6ddc-44c9-83eb-88274ef5583b)

5. Review and launch the instance. 
![image](https://github.com/warquise/VPN-Deployment/assets/160808546/155d9856-5306-4857-b708-b94a9deabcbf)

## Creating Username and Password for VPN SERVER

1. Type `yes` for the agreement then continue to press `enter` key for all the default settings til you get to the username and password code
  ![image](https://github.com/warquise/VPN-Deployment/assets/160808546/54bb1074-d9ca-41ec-879a-77cc00939647)

   ssh -i /path/to/your-key-pair.pem ec2-user@<your-ec2-instance-public-dns>
This project automates the deployment of a VPN server on AWS using OpenVpn Technology





## Prerequisites

- AWS Account
- AWS CLI configured
- SSH key pair for EC2 instance

## Deployment Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/openvpn/vpn-deployment-project.git
    cd vpn-deployment-project
    ```

2. Configure AWS CLI with your credentials and region.

3. Run the deployment script:
    ```sh
    ./scripts/deploy-vpn.sh
    ```

## Configuration

- Modify `config/aws-config.json` for your AWS settings.
- Adjust `config/vpn-setup.conf` for your VPN server settings.

## Usage

- Access the OpenVPN Admin UI at: `https://<INSTANCE_IP>:943/admin`
- Access the OpenVPN Client UI at: `https://<INSTANCE_IP>:943/`
- Login using the 'openvpn' account with the password set during the setup.




