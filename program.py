import psutil, os
from psutil import Process

class ProgramManager:
    def __init__(self):
        pass

    def find_processes(self, name:str) -> list[Process]:
        """Find all process IDs (PIDs) of a given program by its name."""
        pids = []
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            if proc.info['name'] and name.lower() in proc.info['name'].lower():
                pids.append(proc.info['pid'])
        return pids
    
    def close_programs(self, pids, program_name):
        """Close all programs using their PIDs."""
        for pid in pids:
            try:
                os.kill(pid, 9)  # Sends SIGKILL to terminate the process
                print(f"<< {program_name} >> with PID {pid} has been closed.")
            except Exception as e:
                print(f"Error closing program with PID {pid}: {e}")
    def kill(self, program_name):
        pids = self.find_processes(program_name)
        if pids:
            self.close_programs(pids, program_name)
        else:
            print(f"Program <{program_name}> not found.")