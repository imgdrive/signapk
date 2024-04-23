@echo off
mkdir out
del out\*.apk
del out\*.idsig

set SIGNAPK=signapk sign -v
set APKSIGN=java -Xmx1024M -Xss1m -jar apksigner.jar sign
set APKVERIFY=@java -Xmx1024M -Xss1m -jar apksigner.jar verify --verbose

set SIGNARG=--ks-pass pass:android --key-pass pass:android --v1-signing-enabled true --v2-signing-enabled true --v3-signing-enabled true
@for %%A in (rsa_1024 rsa_2048 rsa_4096 rsa_8192 rsa_16384 ec_256 ec_384 ec_521 dsa_1024 dsa_2048 dsa_3072) do (
    echo ----------------------------------
    echo SignApk %%A.jks in.apk out\%%A_signapk.apk
    %SIGNAPK% %SIGNARG% --ks %%A.jks in.apk out\%%A_signapk.apk
    %APKVERIFY% out\%%A_signapk.apk
    
    %APKSIGN% %SIGNARG% --ks %%A.jks --out out\%%A_apksigner.apk in.apk
)