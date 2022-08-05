# Description: This script deletes the existing Cygwin 64 bit configuration on your machine at C:\cygwin64 directory
#              and installs a fresh cygwin64 bit on the same directory from cygwin site. 
#              It also installs the cygwin packages bash,flex,unzip,cpio,diffutils,patch,dos2unix,ctags,gawk,sed,grep,wget,curl 
#              addtional packages can be appended with -P <package name>
#usage: .\install_cygwin.ps1

Write-Host "Installing Cygwin x64..." -ForegroundColor Cyan

if(Test-Path C:\cygwin64) {
    Write-Host "Deleting existing installation..."
    Remove-Item C:\cygwin64 -Recurse -Force
}

# download installer
New-Item -Path C:\cygwin64 -ItemType Directory -Force
$exePath = "C:\cygwin64\setup-x86_64.exe"
(New-Object Net.WebClient).DownloadFile('https://cygwin.com/setup-x86_64.exe', $exePath)

# install cygwin
cmd /c start /wait $exePath -qnNdO -R C:/cygwin64 -s http://cygwin.mirror.constant.com -l C:/cygwin64/var/cache/setup -P bash -P flex -P unzip -P cpio -P diffutils -P patch -P dos2unix -P ctags -P gawk -P sed -P grep -P wget -P curl
C:\cygwin64\bin\bash -lc true

Write-Host "Installed Cygwin x64" -ForegroundColor Green
