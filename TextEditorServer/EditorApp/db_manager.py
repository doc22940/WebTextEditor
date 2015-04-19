import datetime
import logging
from models import Document

logger = logging.getLogger('db_manager')

def insert_text(document, text, position):
	logger.info("Inserting '" + text + "' at position " + str(position) + " in " + document.name)
	document["text"] = document["text"][:position] + text + document["text"][position:]
	document["last_change"] = datetime.datetime.now()
	logger.info("After editing text: " + document["text"])
	document.save()
	logger.info("Document saved")

def remove_text(document, text, position):
	logger.info("Removing '" + text + "' at position " + str(position) + " in " + document.name)
	document["text"] = document["text"][:position] + document["text"][position + len(text):]
	document["last_change"] = datetime.datetime.now()
	logger.info("After removing text: " + document["text"])
	document.save()
	logger.info("Document saved")

def create_document(name, text):
	logger.info("Creating document " + name + ' with text ' + text)
	document = Document(name = name)
	document.last_change = datetime.datetime.now()
	document.text = text
	document.save()
	logger.info("Document created")