from apscheduler.schedulers.background import BackgroundScheduler

class Scheduler:

    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def add_interval_job(self, function, seconds):
        self.scheduler.add_job(
            function,
            "interval",
            seconds=seconds
        )

    def start(self):
        self.scheduler.start()

    def shutdown(self):
        self.scheduler.shutdown()