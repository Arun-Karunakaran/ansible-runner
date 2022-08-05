@ECHO ON
set ExitCode=0
REM echo %II_SYSTEM%
cd %II_SYSTEM%\ingres\bin
call setingenvs.bat
cd C:\Jenkins\test_or_js 
npm run or2js js4gldb > %WORKSPACE%\4GLtoJS_UnitTest_execution_log.txt 2>&1
if NOT %ERRORLEVEL%==0 (echo "Error executing npm for 4gl2js" & set ExitCode=2)
exit /B %ExitCode%

:: > %WORKSPACE%\4GLtoJS_UnitTest_execution_log.txt 2>&1 