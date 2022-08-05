for /f "skip=1 tokens=3" %%s in ('C:\Windows\System32\query.exe user ingres') do (
  %windir%\System32\tscon.exe %%s /dest:console
)