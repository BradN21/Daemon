from daemon.modules.file_organiser.organiser import FileOrganiser
from daemon.modules.pc_monitor.monitor import PCMonitor
from daemon.core.scheduler import Scheduler
from threading import Event

class Application:

    def __init__(self):
        self.name = "Daemon"
        self.version = "0.1.0"
        self.file_organiser = FileOrganiser()
        self.pc_monitor = PCMonitor()
        self.scheduler = Scheduler()
        self.shutdown_event = Event()

    def start(self):
        print(f"{self.name} v{self.version} is starting...")

        self.file_organiser.start()
        self.pc_monitor.start()

        self.scheduler.add_interval_job(
            self.pc_monitor.run_check,
            30
        )

        self.scheduler.start()
        self.shutdown_event.wait() 

    def stop(self):
        print(f"{self.name} is shutting down...")

        self.scheduler.shutdown()
        self.shutdown_event.set()

        print(f"{self.name} has stopped.")