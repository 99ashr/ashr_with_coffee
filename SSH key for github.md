# SSK Key

<!-- Generate ssh key: -->

## How to generate ssh key

[ssh-keygen -t rsa -b 4096 -C "your@example.com"].[EOF`]
[eval "$(ssh-agent -s)"]
[ssh-add ~/path/to/the/.ssh/file/id_rsa].[EOF]

## Configure key on GitHub

Copy the id_rsa.pub key from the .ssh folder and goto GitHub, where in the settings you'll find out SSH key setting there you can add a key and paste this key there.[EOF]