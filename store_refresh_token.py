#!/usr/bin/python2
# Store refresh token in Gnome key ring
# modified from
# https://jason.the-graham.com/2011/01/16/gnome_keyring_with_msmtp_imapfilter_offlineimap/

import gnomekeyring as gkey

def set_credentials(repo, user, pw):
    KEYRING_NAME = "offlineimap"
    attrs = {"repo": repo, "user": user}
    keyring = gkey.get_default_keyring_sync()
    gkey.item_create_sync(keyring, gkey.ITEM_NETWORK_PASSWORD,
                          KEYRING_NAME, attrs, pw, True)

if __name__ == "__main__":
    import sys
    import os
    import getpass
    if len(sys.argv) != 3:
        print("Usage: {}: <repository> <username>".format(
            os.path.basename(sys.argv[0])))
        sys.exit(0)
    repo, username = sys.argv[1:]
    password = getpass.getpass("Enter password for user '%s': " % username)
    password_confirmation = getpass.getpass("Confirm password: ")
    if password != password_confirmation:
        print("Error: password confirmation does not match")
        sys.exit(1)
    set_credentials(repo, username, password)
