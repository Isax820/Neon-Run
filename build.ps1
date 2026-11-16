Write-Host "Building project..." -ForegroundColor Cyan

cd src
cd windows
pyinstaller --noconsole --add-data "rpc.py;." main_windows.py

Write-Host "Building OK !" -ForegroundColor Green