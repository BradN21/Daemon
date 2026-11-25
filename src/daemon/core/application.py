from daemon.modules.file_organiser.organiser import FileOrganiser
from daemon.modules.pc_monitor.monitor import PCMonitor

class Application:

    def __init__(self):
        self.name = "Daemon"
        self.version = "0.1.0"
        self.file_organiser = FileOrganiser()
        self.pc_monitor = PCMonitor()

    def start(self):
        print(f"{self.name} v{self.version} is starting...")

        self.file_organiser.start()
        self.pc_monitor.start()