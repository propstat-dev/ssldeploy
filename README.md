> [!CAUTION]
> This app is under active development and not considered stable as of today.

# ssldeploy
![Screenshot of SSL Deploy Admin Dashboard](/documentation/screenshots/admin-dashboard.png)
A flask based web interface to deploy let's encrypt certificates to various services without compromising domain management credentials.

## Introduction
**Let's encrypt** and **certbot** have dramatically improved the availability of certificates. Unfortunately, DNS authentication is today one of he leading means of distributing the certificates, frequently at the expense of a good security strategy. **ssldeploy** allows you to centralize the DNS authentication, certificate creation and deployment of your SSL certificates in a safe part of your network, distant from the edge. To keep the package simple, easy to backup and portable SQLlite was chosen given that even if used for 1000s of servers, the effective processing and I/O effort is negligible. 

## Features
1. Certificate creation via Certbot and Certbot DNS
2. Deployment of certificates to taget systems
3. Certificate Check on target
4. Self Servicing and Approval Processes for Certificates
5. Single Sign-On Supported for Google and Microsoft with Group Level Privilege Assignment

## Limitations

### Let's Encrypt Rate Limitations
Let's Encrypt limit certificates in multiple ways. The most important one is a limit of [50 certificates per domain](https://letsencrypt.org/docs/rate-limits/).
To request an increase of rate limits [visit this link](https://isrg.formstack.com/forms/rate_limit_adjustment_request).

## How do I run this

### Installation
1. Copy the repo
2. Launch the Installation script
3. Launch the production server via `gunicorn -w 4 'ssldeploy:ssldeploy'`

### Development & Debug Mode
1. Navigate to the folder.
2. Activate venv with `source venv/bin/activate`.
3. Define the python.py as FLASK_APP by `export FLASK_APP=ssldeploy.py`.
4. `flask run` will run on your localhost at the default python port (usually http://127.0.0.1:5000/) with --debug and tailwind-cli by default enabled. Werkzeug will actively avoid duplicate instances of tailwind. 

If you have made modifications to css and templates run `./tools/tailwind/tailwindcss-macos-arm64-v430 -i ./tools/tailwind/input.css -o ./static/css/ssldeploy.css --watch` or your O/S equivalent.

### Known Issues

#### Tailwind Cli on MacOS 
MacOS does have the nasty habbit to reject unsigned packages, as @tailwindlabs does not sign the package, you might have to move it out of quarantine. MacOS will report the file as "damaged" asking you to delete it. 

```bash
cd ./tools/tailwind/tailwind-macos-*-v*** # Replace * with your architecture and version
xattr -l tailwind-macos-*-v*** # Replace * with your architecture and version
xattr -d com.apple.quarantine tailwind-macos-*-v*** # Replace * with your architecture and version
chmod +x tailwind-macos-*-v*** # Replace * with your architecture and version
./tailwindcss-macos-arm64 --help # Test if you can run the file without errors now. 
```

## Why is this better than the alternatives?

## What security precautions have been taken to secure your credentials and certificates?

DNS authentication credentials, target system credentials and certificates are not available on the front-end. While you can create, update and delete credentials, viewing them remains impossible in lack of endpoints. 

## Supported DNS creation


