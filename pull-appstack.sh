#!/bin/bash

set -e

# cleanup
rm -rf terraform.zip terraform

# downbload appstack
appcd appstack download-iac --uuid "$APPSTACK_ID" --output terraform.zip

# unzip
unzip terraform.zip

mkdir -p generated/terraform/build
rm -rf generated/terraform/modules
mv -f terraform/* generated/terraform/
rm -rf terraform terraform.zip
