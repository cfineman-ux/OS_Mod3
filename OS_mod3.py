import sim_logger.py

# classes
# process state

class ProcessState:
    def __init__(self, READY, BLOCKED, SUSPENDED_READY,
                 SUSPENDED_BLOCKED, FINISHED):
        self.BLOCKED = BLOCKED
        self.SUSPENDED_READY = SUSPENDED_READY
        self.SUSPENDED_BLOCKED = SUSPENDED_BLOCKED
        self.FINISHED = FINISHED

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
                
        