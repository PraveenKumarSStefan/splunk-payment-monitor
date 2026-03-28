from datetime import datetime
from pathlib import Path
class ReportGenerator:
    def __init__(self, cfg): self.out = cfg.get("output_dir","reports")
    def generate_html_report(self, client):
        Path(self.out).mkdir(exist_ok=True)
        p = f"{self.out}/report_{datetime.now().strftime('%Ym%d_%H%M')}.html"
        with open(p,"w") as f: f.write("<h1>Payment Health Report</h1>")
        return p
