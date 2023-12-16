# --key-pass
Password with which the private key is protected.
The following formats are supported:

    pass:<password> password provided inline
    env:<name>      password provided in the named
                    environment variable
    file:<file>     password provided in the named
                    file, as a single line
    stdin           password provided on standard input,
                    as a single line

If --key-pass is not specified for a KeyStore key, this
tool will attempt to load the key using the KeyStore
password and, if that fails, will prompt for key password
and attempt to load the key using that password.

If --key-pass is not specified for a private key file key,
this tool will prompt for key password only if a password
is required.

When the same file (including standard input) is used for
providing multiple passwords, the passwords are read from
the file one line at a time. Passwords are read in the
order in which signers are specified and, within each
signer, KeyStore password is read before the key password
is read.