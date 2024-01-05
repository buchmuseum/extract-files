# Problem

Um einen Container für den Import der Wasserzeichen-Scans in das Katalogsystem der DNB zu erstellen, müssen alle JPG- und PNG-Dateien aus den verschiedenen, nach Mappen sortierten Verzeichnissen extrahiert und in ein gemeinsames Import-Verzeichnis kopiert werden.

# Lösung

Das Python-Skript erledigt genau das und loggt Fehler in der Datei `copy_log.txt`. Im Skript muss des Verzeichnis mit den zu kopierenden Dateien und das Ziel-Verzeichnis eingetragen werden. Aufzurufen ist es mit `poetry run python extract-files/extract-files.py`.