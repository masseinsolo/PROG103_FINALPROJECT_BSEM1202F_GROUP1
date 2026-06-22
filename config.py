"""
CONFIGURATION – Constants and settings
"""

DATA_FILE   = "crop_data.json"
USERS_FILE  = "crop_users.json"

# ── Crop catalogue ──────────────────────────────────────────────
LOCAL_CROPS = [
    "Rice", "Maize", "Cassava", "Groundnut", "Sweet Potato",
    "Okra", "Eggplant", "Pepper", "Tomato", "Cassava Leaves",
    "Onions", "Carrot", "Yams", "Beans", "Watermelon",
    "Cucumber", "Pumpkin", "Garden Egg"
]
TEST_CROPS = ["TestCrop1", "TestCrop2", "TestCrop3", "TestCrop4", "TestCrop5"]
ALL_CROPS  = LOCAL_CROPS + TEST_CROPS

MATURITY_DAYS = {
    "Rice": 120, "Maize": 85, "Cassava": 210, "Groundnut": 100,
    "Sweet Potato": 120, "Okra": 60, "Eggplant": 70, "Pepper": 70,
    "Tomato": 65, "Cassava Leaves": 45, "Onions": 90, "Carrot": 75,
    "Yams": 150, "Beans": 75, "Watermelon": 90, "Cucumber": 55,
    "Pumpkin": 100, "Garden Egg": 80,
    "TestCrop1": 0.0002, "TestCrop2": 0.0002, "TestCrop3": 0.0002,
    "TestCrop4": 0.0002, "TestCrop5": 0.0002
}

CROP_TIPS = {
    "Rice":          "Water regularly; drain before harvest. Use flooded paddies for best yield.",
    "Maize":         "Plant in rows 75 cm apart. Side-dress nitrogen at knee height.",
    "Cassava":       "Easy in poor soils. Harvest before 24 months to avoid woodiness.",
    "Groundnut":     "Excellent nitrogen fixer. Helps replenish soil after cereals.",
    "Sweet Potato":  "Needs well-drained ridges. Vines can be replanted as cuttings.",
    "Okra":          "Heat-loving. Harvest pods young (5–7 cm) for tenderness.",
    "Eggplant":      "Mulch to retain moisture. Watch for flea beetles on young plants.",
    "Pepper":        "Stagger planting for continuous supply. Thrives in sunny plots.",
    "Tomato":        "Stake plants at 30 cm. Remove suckers for larger fruits.",
    "Cassava Leaves":"Harvest outer leaves only to keep plant productive.",
    "Onions":        "Stop watering 2 weeks before harvest. Cure in shade for 2 weeks.",
    "Carrot":        "Deep, loose soil prevents forking. Thin seedlings to 5 cm apart.",
    "Yams":          "Requires staking. Mound soil at planting for large tubers.",
    "Beans":         "Fix nitrogen. Sow directly; beans dislike transplanting.",
    "Watermelon":    "Needs full sun and warm nights. Pinch to 2–3 fruits per vine.",
    "Cucumber":      "Train on trellis to save space. Harvest before yellowing.",
    "Pumpkin":       "Give vines plenty of room. Cure harvested fruits for 10 days.",
    "Garden Egg":    "Close relative of eggplant. Tolerates heat and light drought.",
}
for t in TEST_CROPS:
    CROP_TIPS[t] = "Quick-maturing test crop — ready in ~20 seconds for demo purposes."

CROP_ICONS = {
    "Rice": "🌾", "Maize": "🌽", "Cassava": "🌿", "Groundnut": "🥜",
    "Sweet Potato": "🍠", "Okra": "🫑", "Eggplant": "🍆", "Pepper": "🌶️",
    "Tomato": "🍅", "Cassava Leaves": "🌱", "Onions": "🧅", "Carrot": "🥕",
    "Yams": "🍠", "Beans": "🫘", "Watermelon": "🍉", "Cucumber": "🥒",
    "Pumpkin": "🎃", "Garden Egg": "🥚",
}
for t in TEST_CROPS:
    CROP_ICONS[t] = "🧪"

# ── Colour palette ───────────────────────────────────────────────
C = {
    "bg":        "#111b12",
    "sidebar":   "#0d1a0e",
    "panel":     "#1a2e1c",
    "card":      "#243327",
    "accent":    "#4caf50",
    "accent2":   "#81c784",
    "warn":      "#ff9800",
    "danger":    "#f44336",
    "text":      "#e8f5e9",
    "muted":     "#a5d6a7",
    "border":    "#2e4d31",
    "gold":      "#ffd54f",
    "chartbars": ["#4caf50","#81c784","#aed581","#dce775","#ffee58",
                  "#ffa726","#ef5350","#ab47bc","#42a5f5","#26c6da"],
}