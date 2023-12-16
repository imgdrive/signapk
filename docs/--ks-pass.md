# --ks-pass
KeyStore password (see --ks). The following formats are supported:

    pass:<password> password provided inline
    env:<name>      password provided in the named
                    environment variable
    file:<file>     password provided in the named
                    file, as a single line
    stdin           password provided on standard input,
                    as a single line

A password is required to open a KeyStore.

By default, the tool will prompt for password via console
or standard input.

When the same file (including standard input) is used for
providing multiple passwords, the passwords are read from
the file one line at a time. Passwords are read in the
order in which signers are specified and, within each
signer, KeyStore password is read before the key password
is read.