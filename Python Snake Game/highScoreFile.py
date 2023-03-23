from msilib.schema import ServiceControl
import shelve  #use to save dictionary on file
import time

class highScoreFile():
    
    def __init__(self):
        self.sHighScoreFileName = "SnakeParameters.txt"
        self.sStatus = "Saved"
        self.iHighScore = 0

    def getHighScore(self):
        self.bOpenFile()
        return self.iHighScore

    def bOpenFile(self):
        try:
            with shelve.open(self.sHighScoreFileName) as sFile:
                self.HighScoreDate = sFile["Date"] 
                self.iHighScore = sFile["High Score"]
                sFile.close()
        except FileNotFoundError as ex:
            self.iHighScore = 0
            pass

    def bSaveFile(self, bNewHighScore, NewHighScore):
        #Is there a new high score??
        if bNewHighScore == True:
            with shelve.open(self.sHighScoreFileName) as sFile:
                #save File
                sFile["Date"] = time.strftime("%d/%b/%Y %H:%m:%S", time.localtime())
                sFile["High Score"] =NewHighScore
                sFile.close()
                                                                                                                      