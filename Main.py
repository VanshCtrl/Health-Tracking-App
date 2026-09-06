"""
MED_TRACK_API - Health Monitoring & Schedule Engine
Designed for clean data logging, dosage scheduling, and biometric tracking.
"""

import datetime
import json

class HealthTrackerEngine:
    def __init__(self):
        # Simulated database arrays
        self.medications = []
        self.health_logs = []

    def add_medication(self, med_id, name, dosage, schedule_time):
        """Registers a scheduled medication alert."""
        med_entry = {
            "med_id": med_id,
            "name": name,
            "dosage": dosage,
            "schedule_time": schedule_time,  # Format: "HH:MM"
            "status": "Active",
            "created_at": str(datetime.datetime.now())
        }
        self.medications.append(med_entry)
        return f"[SUCCESS] Medication '{name}' ({dosage}) scheduled for {schedule_time} daily."

    def log_biometrics(self, sys_bp, dia_bp, heart_rate):
        """Records daily health metrics."""
        log_entry = {
            "timestamp": str(datetime.datetime.now()),
            "systolic_bp": sys_bp,
            "diastolic_bp": dia_bp,
            "heart_rate": heart_rate,
            "status_flag": "Normal" if sys_bp < 120 and dia_bp < 80 else "Attention Required"
        }
        self.health_logs.append(log_entry)
        return f"[SUCCESS] Biometric entry recorded. Status: {log_entry['status_flag']}"

    def get_due_reminders(self, current_time_str):
        """Filters active medication reminders against system time."""
        due_list = [med for med in self.medications if med["schedule_time"] == current_time_str]
        return due_list


# Execution Verification Routine
if __name__ == "__main__":
    app = HealthTrackerEngine()
    
    # 1. Schedule Medications
    print(app.add_medication(101, "Amoxicillin", "500mg", "08:00"))
    print(app.add_medication(102, "Vitamin D3", "1000IU", "20:00"))

    # 2. Log Health Metrics
    print(app.log_biometrics(118, 78, 72))

    # 3. Simulate Trigger Check
    reminders = app.get_due_reminders("08:00")
    print("\n--- ACTIVE REMINDERS (08:00) ---")
    print(json.dumps(reminders, indent=2))
  
