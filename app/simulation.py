import time
import threading
import random
from database import insert_data, read_data

class SimulationManager:
    def __init__(self):
        self.running = True
        self.read_load = 10  # Base read operations per second
        self.write_load = 2  # Base write operations per second
        self.read_spike = False
        self.write_spike = False
        self.db_crashed = False

    def run_simulations(self):
        while self.running:
            if not self.db_crashed:
                # Simulate Read and Write Operations
                threading.Thread(target=self.simulate_reads).start()
                threading.Thread(target=self.simulate_writes).start()
            time.sleep(1)

    def simulate_reads(self):
        operations = self.read_load * (5 if self.read_spike else 1)
        for _ in range(operations):
            if self.db_crashed:
                break
            read_data()
            time.sleep(1 / operations)

    def simulate_writes(self):
        operations = self.write_load * (5 if self.write_spike else 1)
        for _ in range(operations):
            if self.db_crashed:
                break
            insert_data()
            time.sleep(1 / operations)

    def trigger_read_spike(self, duration):
        self.read_spike = True
        threading.Timer(duration, self.reset_read_spike).start()

    def trigger_write_spike(self, duration):
        self.write_spike = True
        threading.Timer(duration, self.reset_write_spike).start()

    def reset_read_spike(self):
        self.read_spike = False

    def reset_write_spike(self):
        self.write_spike = False

    def crash_db(self):
        self.db_crashed = True

    def restore_db(self):
        self.db_crashed = False

    def stop(self):
        self.running = False
