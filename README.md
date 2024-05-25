
# VPN Deployment Project on AWS


This guide provides step-by-step instructions on how i deployed A VPN using OpenVPN on Amazon Web Services (AWS) 

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Launching an EC2 Instance](#launching-an-ec2-instance)
3. [Creating Username and Password for VPN SERVER](#creating-username-and-password-for-vpn-server)  
4. [ Configure VPN Settings in Admin Panel](#configure-vpn-settings-in-admin-panel)
5. [Use The VPN on your devices](#use-the-vpn-on-your-devices)
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

1. Type `yes` for the agreement. Then continue to press `enter` key for all the default settings til you get to the username and password code.
  ![image](https://github.com/warquise/VPN-Deployment/assets/160808546/54bb1074-d9ca-41ec-879a-77cc00939647)

2. Once I saw my the default username "openvpn", I created my password and then skipped the activation key and pressed `enter`
![image](https://github.com/warquise/VPN-Deployment/assets/160808546/b0f9c4da-4d6a-40a0-b799-0318225fab47)


## Configure VPN Settings in Admin Panel

1. Copy the admin url to log in to the OpenVpn admin panel
![image](https://github.com/warquise/VPN-Deployment/assets/160808546/3e033204-8015-45dc-a9d4-58f76657e4cc)

2. Once I pasted the url in google browser i typed my username and password in.
![image](https://github.com/warquise/VPN-Deployment/assets/160808546/14ca6e1f-c275-4fe3-bb99-3e9e0ab1e001)

3. Go to VPN settings and enable the toggle to yes of the highighted sentence 
   ![image](https://github.com/warquise/VPN-Deployment/assets/160808546/c219ff64-8ed0-42b0-bf54-075540ee6109)


## Use The VPN on your devices

1.Download the VPN connect app 

![image](https://github.com/warquise/VPN-Deployment/assets/160808546/c97116ab-a2d5-419b-8714-779e414bf37d)

2. Once prompted to the openvpn app use the client url

![image](https://github.com/warquise/VPN-Deployment/assets/160808546/1168e0e6-5ce8-4e8e-8f6d-16e0a777c34c)

3. After I logged in connected to the VPN

![image](https://github.com/warquise/VPN-Deployment/assets/160808546/b562da0a-b6b4-40f0-9808-77feda9deeb7)

4. Congrats your VPN is now connected!!!

![image](https://github.com/warquise/VPN-Deployment/assets/160808546/415cf2fd-c549-4f2a-8d09-017a57babbdd)

