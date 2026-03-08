import psutil, os
from psutil import Process
import pandas as pd
from pathlib import Path

class ProgramManager:
    def __init__(self):
        self.df_all_programs = None
        self.df_not_include = None
        self.df_client_apps = None

    def find_processes(self, name:str) -> list[Process]:
        """Find all process IDs (PIDs) of a given program by its name."""
        pids = []
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            if proc.info['name'] and name.lower() in proc.info['name'].lower():
                pids.append(proc.info['pid'])
        return pids
    
    def close_programs(self, pids, program_name) -> bool:
        """Close all programs using their PIDs."""
        for pid in pids:
            os.kill(pid, 9)  # Sends SIGKILL to terminate the process
        return True

    def kill(self, program_name) -> bool:
        pids = self.find_processes(program_name)
        if pids:
            if self.close_programs(pids, program_name):
                return True
            else: 
                return False
        else:
            return False
        
    def get_open_programs(self) -> pd.DataFrame:
        programs = []
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            programs.append(
                {
                    'pid': proc.pid,
                    'name': proc.name()
                }
            )
        self.df_all_programs = pd.DataFrame(programs)

        not_include_fp = Path(__file__).resolve().parent / 'not_client_app.csv'
        self.df_not_include = pd.read_csv(not_include_fp)
        
        result = self.df_all_programs[
            ~ self.df_all_programs['name'].isin(self.df_not_include['name'])
        ]
        return result
