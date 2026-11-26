import psutil

class PCMonitor:

    def __init__(self):
        self.name = "PC Monitor"

    def start(self):
        print(f"{self.name} has started!")


    def get_cpu_usage(self):
        usage = psutil.cpu_percent(interval=1)
        return usage
    
    def get_memory_usage(self):
        usage = psutil.virtual_memory()
        return usage

    def get_disk_usage(self):
        usage = psutil.disk_usage("/")
        return usage

    def show_warning(self, message):
        print(f"WARNING: {message}")

    def check_system_health(self, cpu, ram, disk):
        if cpu > 90:
            self.show_warning("CPU usage is high!")

        if ram.percent > 90:
            self.show_warning("RAM usage is high!")

        if disk.percent > 90:
            self.show_warning("Disk space is running low!")

    def generate_report(self, cpu, ram, disk):
        divider = "=" * 32

        report = f"""
        {divider}
        DAEMON SYSTEM REPORT
        {divider}

        CPU
        Usage: {cpu}%

        RAM
        Usage: {ram.percent}%

        Disk
        Usage: {disk.percent}%

        {divider}
        """

        return report

    def run_check(self):
        cpu = self.get_cpu_usage()
        ram = self.get_memory_usage()
        disk = self.get_disk_usage()

        self.check_system_health(cpu, ram, disk)

        report = self.generate_report(cpu, ram, disk)
        print(report)