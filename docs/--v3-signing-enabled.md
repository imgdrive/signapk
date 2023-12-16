# --v3-signing-enabled
Whether to enable signing using APK Signature Scheme v3
(aka v3 signing scheme) introduced in Android P,
API Level 28. By default, signing using this scheme is
enabled based on min and max SDK version (see
--min-sdk-version and --max-sdk-version).  Multiple
signers are not supported when using v3 signing, but
multiple signers may be provided in conjunction with the
"lineage" option to make sure that the app is signed by
an appropriate signer on all supported platform versions.