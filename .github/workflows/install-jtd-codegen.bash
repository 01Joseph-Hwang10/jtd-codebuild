#!/bin/bash

# Download and unpack jtd-codegen
jtd_codegen_archive_url=$(curl https://api.github.com/repos/jsontypedef/json-typedef-codegen/releases | jq '.[0].assets' | jq '.[] | select(.name | test("linux-gnu"))' | jq -r '.browser_download_url')
wget $jtd_codegen_archive_url -O jtd-codegen.zip
unzip jtd-codegen.zip

# Install jtd-codegen
chmod +x jtd-codegen
mkdir -p .jtd-codegen
mv jtd-codegen .jtd-codegen/jtd-codegen
echo "$(pwd)/.jtd-codegen" >> $GITHUB_PATH

# Clean up
rm -f jtd-codegen.zip
