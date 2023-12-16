# signapk command line

## Usage
    signapk <command> [options]

| Command  | Description                                                     |
|:---------|:----------------------------------------------------------------|
| sign     | Sign the provided APK                                           |
| verify   | Check whether the provided APK is expected to verify on Android |

<table>
<tr><th>Options</th><th>Description</th></tr>
<tr><td><a href="--ks.md">--ks</a></td><td>KeyStore file</td></tr>
<tr><td><a href="--ks-key-alias.md">--ks-key-alias</a></td><td>KeyStore key alias</td></tr>
<tr><td><a href="--ks-pass.md">--ks-pass</a></td><td>KeyStore password</td></tr>
<tr><td><a href="--key-pass.md">--key-pass</a></td><td>Key password</td></tr>
<tr><td><a href="--in.md">--in</a></td><td>Input file</td></tr>
<tr><td><a href="--out.md">--out</a></td><td>Output file</td></tr>
<tr><td><a href="--help.md">--help</a><br><a href="-h.md">-h</a></td><td>Help</td></tr>
<tr><td><a href="--verbose.md">--verbose</a><br><a href="-v.md">-v</a></td><td>Verbose output</td></tr>
<tr><td><a href="--v1-signing-enabled.md">--v1-signing-enabled</a></td><td>Whether to enable signing using APK Signature Scheme v1</td></tr>
<tr><td><a href="--v2-signing-enabled.md">--v2-signing-enabled</a></td><td>Whether to enable signing using APK Signature Scheme v2</td></tr>
<tr><td><a href="--v3-signing-enabled.md">--v3-signing-enabled</a></td><td>Whether to enable signing using APK Signature Scheme v3</td></tr>
<tr><td><a href="--min-sdk-version.md">--min-sdk-version</a></td><td>Lowest API Level</td></tr>
<tr><td><a href="--max-sdk-version.md">--max-sdk-version</a></td><td>Highest API Level</td></tr>
</table>

## Example
	signapk sign --ks release.jks app.apk
	signapk verify --verbose app.apk