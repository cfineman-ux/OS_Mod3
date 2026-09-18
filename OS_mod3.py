import sim_logger.py
from enum import ENUM
# classes

# represents the state of the processor
class ProcessState(ENUM):
        READY = 0
        BLOCKED = 1
        SUSPENDED_READY = 2
        SUSPENDED_BLOCKED = 3
        FINISHED = 4

# represents the process
class SimProcess:
    # integer to rep process id
    # string to rep name
    # int of total instructions
    def __init__(self, pid, procName, totalInstructions):
        self.pid = pid
        self.procName = procName
        self.totalInstructions = totalInstructions

    #help idk whats going on here
    # execute mthod
    # will perform one of the instructions
    # will take number of the instruction that its up to as the parameter
    # returns a process state - one of those enum values
    # so execute method display message with the pid, name, and instruction
    # number being executed and determines what state to return
    def execute(i, totalInstructions):
        # if i is greater than totalinstructions, return finished
        if i >= totalInstructions:
            return
        # otherwise roll the dice and with 15% prob act as if 
        # the device is blocked
        # the other 75% time retun ready
# reps the processor of the computer
# references the current process - use getter and setter that
# can manipulated in the main of the program
# 4 int vals to rep 4 registers, and use getters and setters for these too
# will have int to rep curr instruction thats running
# execute next isnstruction method
# look at curr process, and curr instruction register value,
# and tell sim process the sim process the instruction its up to
class SimProcessor:
    def __init__(self, curr_process, currInstruction, registers
    ):
        self.curr_process = SimProcess
        self.currInstruction = currInstruction
        self.registers = [9,8,7,6]
    def executeNextInstruction(SimProcess, currInstruction):
        SimProcess.execute(currInstruction)
        currInstruction +1
        ##### huh
class ProcessControlBlock:
    def __init__(self, currInstruction):
        self.currInstruction = currInstruction

        