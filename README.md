# signapk
signapk is a free cross-platform standalone tool to sign the Android APK file, it's written in C/C++ and has compatible command line arguments with Google [ApkSigner](https://developer.android.com/tools/apksigner).

signapk is implemented from scratch in C/C++ according to ApkSigner docs and source code, because there are many factors involved in APK signing. If you have problems with the signature, please submit an issue at https://github.com/dvdforge/signapk/issues.

## Download
signapk version 1.5 (2023-12-15)
- signapk for Windows
  - [signapk x86](https://download.yubsoft.com/x86/signapk.exe)
  - [signapk x64](https://download.yubsoft.com/x64/signapk.exe)
  - [signapk ARM64](https://download.yubsoft.com/arm64/signapk.exe)
- [signapk for macOS](https://download.yubsoft.com/macos/signapk.zip)
- [signapk for Linux (Unbuntu)](https://download.yubsoft.com/ubuntu/signapk.exe)

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

## Usage
    signapk <command> [options]
| Command  | Description                                                     |
|:---------|:----------------------------------------------------------------|
| sign     | Sign the provided APK                                           |
| verify   | Check whether the provided APK is expected to verify on Android |

<table>
<tr><th>Options</th><th>Description</th></tr>
<tr><td><a href="docs/--ks.md">--ks</a></td><td>KeyStore file</td></tr>
<tr><td><a href="docs/--ks-key-alias.md">--ks-key-alias</a></td><td>KeyStore key alias</td></tr>
<tr><td><a href="docs/--ks-pass.md">--ks-pass</a></td><td>KeyStore password</td></tr>
<tr><td><a href="docs/--key-pass.md">--key-pass</a></td><td>Key password</td></tr>
<tr><td><a href="docs/--in.md">--in</a></td><td>Input file</td></tr>
<tr><td><a href="docs/--out.md">--out</a></td><td>Output file</td></tr>
<tr><td><a href="docs/--help.md">--help</a><br><a href="-h.md">-h</a></td><td>Help</td></tr>
<tr><td><a href="docs/--verbose.md">--verbose</a><br><a href="-v.md">-v</a></td><td>Verbose output</td></tr>
<tr><td><a href="docs/--v1-signing-enabled.md">--v1-signing-enabled</a></td><td>Whether to enable signing using APK Signature Scheme v1</td></tr>
<tr><td><a href="docs/--v2-signing-enabled.md">--v2-signing-enabled</a></td><td>Whether to enable signing using APK Signature Scheme v2</td></tr>
<tr><td><a href="docs/--v3-signing-enabled.md">--v3-signing-enabled</a></td><td>Whether to enable signing using APK Signature Scheme v3</td></tr>
<tr><td><a href="docs/--min-sdk-version.md">--min-sdk-version</a></td><td>Lowest API Level</td></tr>
<tr><td><a href="docs/--max-sdk-version.md">--max-sdk-version</a></td><td>Highest API Level</td></tr>
</table>

### Example
	signapk sign --ks release.jks app.apk
	signapk verify --verbose app.apk

## Changelog
### Version 2.0 2023-12-15
- Changed: implement complatible command line arguments with ApkSigner
- Added: support signature algorithm DSA-1024, DSA-2048 and DSA-3072
- Added: native binaries for macOS (x86-x64 and ARM64)
- Added: native binaries for Linux (Unbuntu)

### Version 1.0 2023-06-01
- First public release
