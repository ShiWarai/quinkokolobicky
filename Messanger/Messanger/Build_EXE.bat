rd /q /s dist
pyinstaller main.pyw --add-data="data/sound.wav;." --icon=app.ico --workpath=for_building --noconsole --onefile --version-file=version.rc