# 🌾 Crop Advisor – Smart Farm Management System

Python 3.8+ | MIT License | Limkokwing University PROG103 Project

Crop Advisor is an offline, lightweight desktop application designed to empower smallholder farmers in Sierra Leone by modernizing daily farm operations, optimizing soil health through structured crop rotation logic, and tracking structural seasonal finance.

Built as a final project for PROG103 – Principles of Structured Programming at Limkokwing University of Creative Technology, Faculty of Information & Communications Technology.

---

## 📖 Table of Contents
- About The Project
- Core Features
- Built With
- Project Structure
- Data Privacy & .gitignore Compliance
- Installation
- How to Run
- Login Credentials
- How It Works
- Structured Programming Principles
- Contributors
- License

---

## 📌 About The Project

Agriculture serves as the economic backbone of Sierra Leone, yet smallholders often struggle with declining soil quality, unexpected crop failures, and fragmented financial records. 

Crop Advisor directly targets these challenges by providing a 100% offline, user-friendly digital layout that removes the barrier of rural internet access. The platform replaces guesswork with programmatic, data-driven agricultural logic to help maximize crop yields and align local farming with United Nations Sustainable Development Goals (SDGs 1, 2, 8, 12, and 15).

---

## ✨ Core Features

Secure Auth
Secure access with unique user profile credentials and account registration frames.

Interactive Dashboard
Real-time tracking of operational KPIs, visual crop distributions, and high-priority alerts.

Crop Rotation Logic
Smart engine that evaluates past crop history and active soil quality to suggest ideal sequential plantings.

Fertilizer Planner
Computes precise, environmentally responsible fertilizer weight limits based on plot acreage.

Harvest Live Tracker
Monitors fields with second-by-second countdown variables, dynamic progress bars, and targeted crop tips.

Sales Ledger
Registers market transactions, builds revenue/profit summaries, and exports data directly to CSV files.

JSON Persistence
Automated state-saving architecture into structured JSON configurations to guarantee data recovery on system reboot.

Harvest Alarm System
Active visual system alerts triggered immediately when a specific crop's optimal harvest window opens.

---

## 🛠️ Built With

* Python 3.8+ – Core architecture and programming logic.
* Tkinter – Native graphical user interface framework.
* JSON Modules – Local file-based database engine for offline persistence.
* CSV & Datetime Packages – Interoperable data exports and precise mathematical timeline tracking.

No External Dependencies: The application utilizes entirely native standard Python libraries, making installation straightforward on any device.

---

## 📁 Project Structure

crop_advisor/
  main.py          Description: Application entry point — boots login module
  config.py        Description: System constants (crop definitions, maturity indexes, colors)
  model.py         Description: Global file state operations & automated JSON serialization
  logic.py         Description: Algorithmic business workflows (rotation matching, duration formulas)
  gui.py           Description: GUI rendering engine containing all structural view layouts
  crop_data.json   Description: Local operational application ledger (Auto-generated)
  crop_users.json  Description: Authenticated local security parameters (Auto-generated)
  .gitignore       Description: Excludes runtime caches and user databases from public version history
  README.md        Description: Document orientation manual

---

## 🛡️ Data Privacy & .gitignore Compliance

To comply with proper software engineering standards and ensure data privacy, a `.gitignore` file is implemented in the repository root. This configuration intentionally blocks local transaction history and security databases from being pushed to public GitHub servers. for example * .DS_Store
Excluded paths:
* `crop_data.json` (Protects local farmer financial ledgers)
* `crop_users.json` (Protects local credentials and account states)
* `__pycache__/` (Excludes compiled Python bytecode)

---

## 📥 Installation

Prerequisites
* Ensure Python 3.8 or higher is installed on your local computer system.

Deployment Steps
1. Clone the project repository to your local path:
   git clone https://github.com/masseinsolo/PROG103_FINALPROJECT_BSEM1202F_GROUP2.git

2. Navigate directly into the source module root:
   cd PROG103_FINALPROJECT_BSEM1202F_GROUP2/crop_advisor

---

## 🚀 How to Run

Execute the bootstrap initialization command from your terminal:
python3 main.py

---

## 🔑 Login Credentials

The system initializes with a baseline smallholder testing profile. Custom farmer accounts can be generated independently using the registration menu inside the application interface:

* Smallholder Testing Profile
  Username: farmer1
  Password: crop123

---

## ⚙️ How It Works

1. Data Pipeline Architecture
User Input via GUI triggers Event Signals, which process through Core Logical Math before utilizing Data Serialization to write silently to the local JSON Database File.

2. Crop Rotation Conditional Array
The software applies a highly ordered structural logic layer (recommend_crop()) to manage soil health and maximize yield efficiency:

* Cereals (Rice, Maize)
  - Poor Soil State: Recommends Cassava (Restores texture depth)
  - Fair Soil State: Recommends Groundnut (Nitrogen fixing)
  - Rich Soil State: Recommends Sweet Potato

* Legumes (Groundnut, Beans)
  - Poor Soil State: Recommends Maize
  - Fair Soil State: Recommends Rice
  - Rich Soil State: Recommends Cassava

3. Chronological Harvest Predictor
The system determines exact timeline constraints via the internal estimate_harvest_seconds_left() module. It pulls standard germination variables from the configuration file, evaluates current regional tracking timestamps against user-defined planting entries, and applies scaling adjustments for weather variables before passing remaining intervals directly to the active system ticker.

4. Continuous System Heartbeat
The system framework relies on a persistent synchronization loop utilizing the structural _tick() architecture:

root.after(1000, self._tick)

This loop runs continuously every 1,000 milliseconds to adjust countdown meters, recalculate chart ranges, and fire popup notification warnings the exact moment a target plot crosses its maturity threshold.

---

## 📚 Structured Programming Principles

The platform serves as an intentional showcase of standard structured software engineering paradigms:

* Sequence: Code operates along fixed linear steps. The boot sequence progresses uniformly: data recovery via load_data() then container frame compilation via _build_layout() followed by primary screen population via show_dashboard() and background loop binding via _tick().
* Selection: Evaluates real-time contextual variables using clean conditional branching algorithms (if-elif-else) to guide state routing, permission clearance, and user navigation paths.
* Iteration: Processes multiple array collections smoothly using robust loop constructs (for/while) to build analytics tracking systems, map dynamic harvest cards, and render data structures into system reporting tables.
* Modularisation: Splits unrelated system requirements into decoupled, isolated units. Functions focus strictly on single task executions, minimizing code entanglement across files.

---

## 👥 Contributors

* Solomon Massein Kanu (905005767) – Lead System Logic Developer & Concept Designer
  Responsibility: Formulated core application concept and built underlying algorithmic files (logic.py, config.py, and state tracking matrices).

* Joseph Vandy (905005916) – Lead UI Architect & Graphical Designer
  Responsibility: Structured layout frameworks, canvas bindings, operational panels, and visual chart assets across the primary application display.

* Alpha Sesay (905006158) – Interface Verification & Feature Integration
  Responsibility: Implemented the registration frames, user credential pipelines, field detail windows, and assisted in system QA testing.

Academic Class: PROG103 – Principles of Structured Programming  
University Institution: Limkokwing University of Creative Technology, Sierra Leone  
Academic Semester: Term 02 (March 2026 – July 2026)

---

## 📄 License

This system is released and distributed under the clear provisions of the open-source MIT License. Check the primary project LICENSE configuration file for complete operational definitions.

---

## 🙏 Acknowledgements

* Mr. Amadu Kamara – Academic Lecturer & Course Examiner, Faculty of Information & Communications Technology, for layout guidelines, continuous guidance, and foundational structured programming methodologies.
* Limkokwing University Quality Assurance Committee – For providing structural boundaries that help focus academic work on real local problems in Sierra Leone.

---
