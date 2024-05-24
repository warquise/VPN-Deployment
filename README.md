
# VPN Deployment Project on AWS

This project automates the deployment of a VPN server on AWS using OpenVpn Technology

First i chose to deploy my server on Us-East-1 Since my North Carolina A & T is located on the East Coast in North Carolina 
![image](https://github.com/warquise/VPN-Deployment/assets/160808546/31cda74f-d868-43ad-8373-516989879f4a)

navigated the Virtual private Cloud and Went in the ECS (The virtual machine)
![image](https://github.com/warquise/VPN-Deployment/assets/160808546/5334cb73-a8c8-4ed5-a0de-dfe824caa319)



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




