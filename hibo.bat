TASKKILL /F /IM qgis-bin.exe
rmdir  /s /q ..\.qgis2\python\plugins\hibo
echo d | xcopy /f /y /e . ..\.qgis2\python\plugins
start ..\.qgis2\python\plugins\qgis-project\project.qgs