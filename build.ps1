$exclude = @("venv", "bot-youtube.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-youtube.zip" -Force