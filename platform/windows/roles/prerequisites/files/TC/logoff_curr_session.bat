set MY_SESSION_ID=unknown
for /f "tokens=3-4" %%a in ('qwinsta ingres') do @if "%%b"=="Active" set MY_SESSION_ID=%%a
logoff %MY_SESSION_ID%