"""
MODELS – Data storage and persistence (JSON)
"""

import json
import os
from datetime import datetime
from config import DATA_FILE, USERS_FILE

# ── Global state ────────────────────────────────────────────────
crops_planted   = []
harvest_records = []
sales_records   = []
current_user    = None
start_work_time = None
USERS           = {}

# ── User persistence ────────────────────────────────────────────
def load_users():
    global USERS
    default = {
        "farmer1": {"password":"crop123","phone":"0781234567","fullname":"Elijah Farmer","role":"admin"}
    }
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE) as f:
                USERS = json.load(f)
        except:
            USERS = default
    else:
        USERS = default
        save_users()

def save_users():
    with open(USERS_FILE,"w") as f:
        json.dump(USERS, f, indent=2)

# ── Data persistence ────────────────────────────────────────────
def save_data():
    data = {
        "crops_planted": [{
            "name": c["name"], "plants": c["plants"],
            "planted_date": c["planted_date"].isoformat(),
            "maturity_days": c["maturity_days"],
            "plot_acres": c.get("plot_acres",1)
        } for c in crops_planted],
        "harvest_records": harvest_records,
        "sales_records":   sales_records,
        "current_user":    current_user,
        "start_work_time": start_work_time.isoformat() if start_work_time else None
    }
    with open(DATA_FILE,"w") as f:
        json.dump(data, f, indent=2)

def load_data():
    global crops_planted, harvest_records, sales_records, current_user, start_work_time
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE) as f:
                data = json.load(f)
            crops_planted = []
            for c in data.get("crops_planted",[]):
                crops_planted.append({
                    "name":          c["name"],
                    "plants":        c["plants"],
                    "planted_date":  datetime.fromisoformat(c["planted_date"]),
                    "maturity_days": c["maturity_days"],
                    "plot_acres":    c.get("plot_acres",1)
                })
            harvest_records = data.get("harvest_records",[])
            sales_records   = data.get("sales_records",[])
            current_user    = data.get("current_user", None)
            st = data.get("start_work_time")
            start_work_time = datetime.fromisoformat(st) if st else None
        except:
            crops_planted = []; harvest_records = []; sales_records = []
    else:
        crops_planted = []; harvest_records = []; sales_records = []