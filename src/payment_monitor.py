"""
Payment Transaction Monitor - Core Engine
Author: Praveenkumar S
"""
import time, logging
from datetime import datetime
from src.splunk_client import SplunkClient
from src.alert_manager import AlertManager
from src.config_loader import load_config
log = logging.getLogger(__name__)

class PaymentMonitor:
    def __init__(self, config):
        self.client = SplunkClient(config["splunk"])
        self.alerts = AlertManager(config["alerts"])
    def run(self):
        log.info("Payment Monitor started")
        while True:
            time.sleep(120)
if __name__ == "__main__":
    cfg = load_config("config/config.yaml")
    PaymentMonitor(cfg).run()
