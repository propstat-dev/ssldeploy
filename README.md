# ssldeploy
A flask based web interface to deploy let's encrypt certificates to various services without compromising domain management credentials.

## Introduction
**Let's encrypt** and **certbot** have dramatically improved the availability of certificates. Unfortunately, DNS authentication is today one of he leading means of distributing the certificates, frequently at the expense of a good security strategy. **ssldeploy** allows you to centralize the DNS authentication, certificate creation and deployment of your SSL certificates in a safe part of your network, distant from the edge. 

# How do I run this

## Installation
1. Copy the repo
2. Launch the Installation script
3. Launch the production server via 'gunicorn -w 4 \'ssldeploy:ssldeploy\''

## Development & Debug Mode
1. Navigate to the folder.
2. Activate venv with 'source venv/bin/activate'.
3. Define the python.py as 'FLASK_APP by export FLASK_APP=ssldeploy.py'  
4. 'flask run' will run on your localhost at the default python port (usually http://127.0.0.1:5000/).
5. If you have made modifications to css and templates run './tools/tailwind/tailwindcss-macos-arm64-v430 -i ./tools/tailwind/input.css -o ./static/css/ssldeploy.css --watch'

## Why is this better than the alternatives?

## What security precautions have been taken to secure your credentials and certificates?

DNS authentication credentials, target system credentials and certificates are not available on the front-end. While you can create, update and delete credentials, viewing them remains impossible in lack of endpoints. 

## Supported DNS creation


