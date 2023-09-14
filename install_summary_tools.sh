#!/bin/bash

echo "Installing python"
sudo apt install python3 --upgrade

echo "Installing summary tools"
python3 -m pip install --ignore-installed -e ./summary_tools
