#On va chercher le thread correspondant puis on appelle sa methode 'stop'
tmpThread = threadTab[int(i)]
tmpThread.stop()
threadTab.remove(tmpThread)



