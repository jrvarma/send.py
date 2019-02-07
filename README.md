send.py
=======

Send email using XOAUTH2 over SMTP

This fork adds capability to read the refresh token from the gnome key ring instead of storing it in a plain text config file

Usage:
Run `store_refresh_token.py` to store the refresh tokens in the key ring giving a suitable repo name for each account.
Copy `sendpyrc-example` to `.sendpyrc` and edit it to fill up the values for `client_id` and `client_secret` as also the value of `repo` (whatever name was chosen while running `store_refresh_token.py`) for each account. 
