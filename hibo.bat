rmdir  /s /q ..\.qgis2\python\plugins\hibo
echo d | xcopy /f /y hibo ..\.qgis2\python\plugins\hibo
::echo d | xcopy /f /y qgis-project ..\.qgis2\python\plugins\qgis-project
::start ..\.qgis2\python\plugins\qgis-project\project.qgs
start qgis-project\project.qgs