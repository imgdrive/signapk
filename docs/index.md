# signapk
signapk is a free cross-platform standalone tool to sign the Android APK file, it's written in C/C++ and has compatible command line arguments with Google [ApkSigner](https://developer.android.com/tools/apksigner).

signapk is implemented from scratch in C/C++ according to ApkSigner docs and source code, because there are many factors involved in APK signing. If you have problems with the signature, please submit an issue at https://github.com/dvdforge/signapk/issues.

## Download
signapk version 1.5 (2023-12-15)
- signapk for Windows
  - [signapk x86](https://download.yubsoft.com/x86/signapk.exe)
  - [signapk x64](https://download.yubsoft.com/x64/signapk.exe)
  - [signapk ARM64](https://download.yubsoft.com/arm64/signapk.exe)
- [signapk for macOS](https://download.yubsoft.com/macos/signapk)
- [signapk for Linux (Unbuntu)](https://download.yubsoft.com/ubuntu/signapk)

## Features
- Written in C/C++, with no third-party dependencies
- Native binaries for Windows(x86/x64/ARM64), macOS(x86_64/ARM64) and Linux(Unbuntu)
- Compatible command line arguments with [ApkSigner](https://developer.android.com/tools/apksigner)
- Support [APK Signature Scheme v1](https://source.android.google.cn/docs/security/features/apksigning)
- Support [APK Signature Scheme v2](https://source.android.google.cn/docs/security/features/apksigning/v2)
- Support [APK Signature Scheme v3](https://source.android.google.cn/docs/security/features/apksigning/v3)

## Todo
- Loading PKCS#12 keystore
- Support APK Signature Scheme v4
- Verify APK Signature Scheme v1