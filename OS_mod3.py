import sim_logger.py
from enum import ENUM
# classes
# process state

class ProcessState(Enum):
        READY = 0
        BLOCKED = 1
        SUSPENDED_READY = 2
        SUSPENDED_BLOCKED = 3
        FINISHED = 4

class SimProcess:
    def __init__(self, pid, procName, totalInstructions):
        self.pid = pid
        self.procName = procName
        self.totalInstructions = totalInstructions

    #help idk whats going on here
    def execute(i, pid, procName, totalInstructions):
        if i >= totalInstructions:
            return "FINISHED"
        else:
            pass
            #CONFUSION
class SimProcessor:
    def __init__(self, SimProcess, currInstruction # ?
    ):
        self.SimProcess = SimProcess
        self.currInstruction = currInstruction
    def executeNextInstruction(SimProcess, currInstruction):
        SimProcess.execute(currInstruction)
        currInstruction +1
        ##### huh
class ProcessControlBlock:
    def __init__(self, currInstruction):
        self.currInstruction = currInstruction

        