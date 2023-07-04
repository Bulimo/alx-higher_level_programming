#!/bin/bash
read -p "Enter a file name: " filename
echo "#!/usr/bin/python3" >> "$filename"
chmod u+x "$filename"
