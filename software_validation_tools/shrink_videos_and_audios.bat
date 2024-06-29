@echo off
setlocal enabledelayedexpansion

rem Directory containing the original mp4 files
set "SOURCE_DIR=..\__pool__"

rem Directory to save the shortened mp4 files
set "DEST_DIR=..\__pool_short__"

rem Create the destination directory if it doesn't exist
if not exist "%DEST_DIR%" mkdir "%DEST_DIR%"

rem Find all video files in the source directory and its subdirectories
for /r "%SOURCE_DIR%" %%F in (*.avi) do (
    rem Compute the path of the new file by replacing the source directory with the destination directory
    set "FILE=%%F"
    set "NEW_FILE=!FILE:%SOURCE_DIR%=%DEST_DIR%!"

    rem Create the directory structure for the new file

echo
    rem Use ffmpeg to create a 1-second clip from the original video
    ffmpeg -y -i "!FILE!" -ss 0 -t 1 -c:v copy -c:a copy "!NEW_FILE!"
)

rem Find all image files in the source directory and its subdirectories
for /r "%SOURCE_DIR%" %%F in (*.jpg) do (
    set "FILE=%%F"
    set "NEW_FILE=!FILE:%SOURCE_DIR%=%DEST_DIR%!"
    mkdir "%~dpNEW_FILE%" 2>nul
    copy "!FILE!" "!NEW_FILE!"
)

rem Find all audio files in the source directory and its subdirectories
for /r "%SOURCE_DIR%" %%F in (*.wav) do (
    set "FILE=%%F"
    set "NEW_FILE=!FILE:%SOURCE_DIR%=%DEST_DIR%!"
    mkdir "%~dpNEW_FILE%" 2>nul
    ffmpeg -y -i "!FILE!" -ss 0 -t 1 -c:a copy "!NEW_FILE!"
)