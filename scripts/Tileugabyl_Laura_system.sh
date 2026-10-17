#!/bin/bash

echo "=============================="
echo "Student Information"
echo "=============================="
echo
echo "Name: Laura"
echo "Surname: Tileugabyl"
echo "Group: IT2-2311"
echo "Student ID: 41586"
echo
echo "=============================="
echo "System Information"
echo "=============================="
echo
echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -sr)"
echo "Disk Usage: $(df -h / | awk 'NR==2 {print $3 " used of " $2}')"
echo "Memory Usage: $(free -h | awk '/^Mem:/ {print $3 " used of " $2}')"
echo

if [ -f ~/devops/tileugabyl_laura/Tileugabyl_Laura_info.txt ]; then
  echo "Student information file exists."
else
  echo "Student information file does not exist."
fi
