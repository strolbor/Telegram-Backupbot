import os

def delete_file(filename):
	"""Datei löschen"""
	if os.path.exists(filename): # Wenn Datei vorhanden
		os.remove(filename) # Lösche diese Datei