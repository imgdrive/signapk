# Example
## Sign the in .apk file with v1/v2 and output to out.apk
```
  signapk sign --ks rsa_1024.jks --ks-pass pass:android --key-pass pass:android --v1-signing-enabled true --v2-signing-enabled true --v3-signing-enabled true --out out.apk in.apk
```

## Verify app.apk
```
  signapk verify --verbose app.apk
```
