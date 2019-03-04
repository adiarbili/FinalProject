pyrcc5 "./Views/resources/qt files/guiResource.qrc" -o ./View/guiResource.py
pyuic5 "./Views/resources/qt files/mainWindow.ui" --resource-suffix Resource -o ./View/mainWindow$(date +"%s").py
pyuic5 "./Views/resources/qt files/about.ui" --resource-suffix Resource -o ./View/about$(date +"%s").py