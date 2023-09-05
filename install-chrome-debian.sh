#!/usr/bin/bash

# Zie ook ~/ansible/install-chrome-debian.yml

# FOUT (key in /etc/apt/trusted.gpg)
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
wget --no-verbose --output-document=- https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo apt-get update
sudo apt-get install --yes google-chrome-stable

# BETER (key in /etc/apt/trusted.gpg.d/)
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
wget --no-verbose --output-document=- https://dl.google.com/linux/linux_signing_key.pub | sudo sudo tee /etc/apt/trusted.gpg.d/google-chrome.asc
sudo apt-get update
sudo apt-get install --yes google-chrome-stable

# GOED (signed-by toegevoegd aan source.list en key in /usr/share/keyrings/)
echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
wget --no-verbose --output-document=- https://dl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor --yes --output=/usr/share/keyrings/google-chrome.gpg
sudo apt-get update
sudo apt-get install --yes google-chrome-stable
sudo apt-key del 7FAC5991 D38B4796
sudo rm --force /etc/apt/trusted.gpg.d/google-chrome*
