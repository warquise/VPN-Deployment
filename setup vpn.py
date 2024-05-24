#!/bin/bash

# Deploy VPC
./scripts/setup-vpc.sh

# Deploy EC2 instances
./scripts/setup-ec2.sh

# Configure VPN
./scripts/configure-vpn.sh

echo "VPN deployment completed."
