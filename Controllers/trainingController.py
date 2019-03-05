import os
from Controllers.controller import Controller
from threading import Thread
import _thread

class TrainingController(Controller):

    def __init__(self):
        super()

    def startTrainingGuide(self):
        if not os.path.isdir(self.view.trainingDir.text()):
            self._Controller__invalidPath(self.view.trainingDir)
            self.setStatusBarMessage("Invalid training directory")
        else:
            # start training process
            self.setStatusBarMessage("Starting training process")
            try:
                training_thread = Thread(target=self.__printX, daemon=True) # daemon=None - means inherited
                training_thread.start()
                # _thread.start_new_thread(printX,())
            except:
               print("Error: unable to start thread")
               self.setStatusBarMessage("Unknown error: unable to start training process")


    def __printX(self):
        for i in range(99999999):
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaa {}".format(i))
