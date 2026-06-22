"""
LOGIC – Business logic (rotation, fertiliser, time calculations)
"""

from datetime import datetime
from config import MATURITY_DAYS, TEST_CROPS

# ── Crop rotation logic ──────────────────────────────────────────
def recommend_crop(last_crop, soil):
    cereals   = ["Rice","Maize"]
    legumes   = ["Groundnut","Beans"]
    roots     = ["Cassava","Sweet Potato","Yams","Pumpkin"]
    leafy     = ["Cassava Leaves","Okra","Eggplant","Pepper","Tomato","Onions","Carrot","Garden Egg","Cucumber","Watermelon"]
    if last_crop in cereals:
        return {"Poor":"Cassava","Fair":"Groundnut"}.get(soil,"Sweet Potato")
    if last_crop in legumes:
        return {"Poor":"Maize","Fair":"Rice"}.get(soil,"Cassava")
    if last_crop in roots:
        return {"Poor":"Groundnut","Fair":"Maize"}.get(soil,"Cassava Leaves")
    if last_crop in leafy:
        return {"Poor":"Groundnut","Fair":"Sweet Potato"}.get(soil,"Maize")
    return "Sweet Potato"

def get_fertilizer(soil, next_crop, plot_acres=1):
    base = {"Poor":80, "Fair":50, "Rich":20}
    kg   = base[soil] * plot_acres
    if soil == "Poor":
        return f"Compost + NPK 20-20-20 – {kg:.0f} kg for {plot_acres} acre(s)"
    elif soil == "Fair":
        return f"NPK 15-15-15 – {kg:.0f} kg for {plot_acres} acre(s)"
    else:
        if next_crop in ["Maize","Rice"]:
            return f"No fertiliser needed — soil is rich & crop is a light feeder ({plot_acres} acre(s))"
        return f"Compost only – {kg:.0f} kg for {plot_acres} acre(s)"

# ── Season and time helpers ─────────────────────────────────────
def get_current_season():
    m = datetime.now().month
    return "Rainy" if 5 <= m <= 10 else "Dry"

def days_since_planting(planted_date):
    return (datetime.now() - planted_date).total_seconds() / 86400

def estimate_harvest_seconds_left(crop):
    base_days    = crop["maturity_days"]
    elapsed_days = days_since_planting(crop["planted_date"])
    season       = get_current_season()
    factor = 1.0
    if season == "Rainy" and crop["name"] in ["Maize","Cassava","Groundnut"]:
        factor = 0.92
    elif season == "Dry" and crop["name"] in ["Tomato","Pepper","Okra"]:
        factor = 0.88
    adj_days = base_days * factor
    sec_left = max(0, (adj_days - elapsed_days) * 86400)
    return sec_left, adj_days

def fmt_time(seconds):
    if seconds <= 0:      return "Ready!"
    if seconds < 60:      return f"{int(seconds)} sec"
    if seconds < 3600:    return f"{int(seconds//60)} min {int(seconds%60)} sec"
    if seconds < 86400:   return f"{int(seconds//3600)}h {int((seconds%3600)//60)}m"
    return f"{int(seconds//86400)}d {int((seconds%86400)//3600)}h"

def pct_complete(crop):
    sec_left, adj_days = estimate_harvest_seconds_left(crop)
    total_sec = adj_days * 86400
    if total_sec <= 0: return 100
    elapsed   = total_sec - sec_left
    return min(100, max(0, elapsed / total_sec * 100))

def _lighten(hex_col, factor=0.25):
    """Lighten a hex colour by blending toward white."""
    hex_col = hex_col.lstrip("#")
    r,g,b = int(hex_col[0:2],16), int(hex_col[2:4],16), int(hex_col[4:6],16)
    r = int(r + (255-r)*factor)
    g = int(g + (255-g)*factor)
    b = int(b + (255-b)*factor)
    return f"#{r:02x}{g:02x}{b:02x}"