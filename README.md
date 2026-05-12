## ✨ Key Features
* 🪐 **3D Orrery:** Interactive Solar System rendered with Three.js.
* 🛰️ **ISS Live Tracker:** Real-time location mapping.
* 📰 **Space News:** Stay updated with cosmic events. News are stored in CSV..
* 🧮 **Astronomical Engine:** Python-based calculations.
* 💾 **Space Facts DB:** Curated database of space facts stored in CSV..

## 🛠️ Tech Stack
* **Backend:** Python 3.10+, Flask
* **Frontend:** Jinja2 Templates, HTML, CSS, JavaScript (Three.js)
* **Database:** CSV file
* **APIs:** NASA Open API, OpenNotify (ISS Tracker)

## 📂 Project Structure
├── Demo/                        # Main web application directory
│   ├── static/                  # Static assets
│   │   ├── image/               # UI icons and celestial textures
│   │   ├── solar.css            # 3D visualization styles
│   │   ├── solar.js             # Three.js engine and orbital logic
│   │   └── style.css            # General application styles
│   ├── templates/               # Jinja2 HTML templates
│   │   ├── index.html           # Landing page
│   │   ├── login.html           # Authentication page
│   │   ├── solar.html           # 3D Solar System view
│   │   ├── iss.html             # ISS tracking dashboard
│   │   ├── news.html            # Space news interface
│   │   ├── facts.html           # Cosmic trivia page
│   │   └── calcus.html          # Astronomical calculator UI
│   ├── calcus.py                # Calculation routes
│   ├── facts.py                 # Facts processing logic
│   ├── iss.py                   # ISS API integration
│   ├── main.py                  # Core application entry point
│   └── news.py                  # News fetching logic
├── library/                     # Backend logic and data processing
│   └── lib/                     
│       ├── facts.csv            # Database for cosmic trivia
│       ├── news.csv             # Cached space events data
│       ├── logic.py             # Core astronomical engine
│       ├── spaceObject.py       # Physics classes for celestial bodies
│       ├── InterestingFacts.py 
│       ├── memoization.py       # Custom caching decorators to optimize heavy calculations
│       ├── news.py              # Backend processing and filtering for space news data
│       └── my_decorator.py      # Custom Python decorators
├── .gitignore                   # Files to ignore (e.g., .venv, __pycache__)
├── app_log.json                 # Application activity logs
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
└── visitors.txt                 # Simple visitor tracking log

##  Observation
* **🔐 Authentication**
![Page of Login](./Demo/static/image/loginPage.png)
* **🏠 Dashboard & Exploration**
![Main Page](./Demo/static/image/main.png)
![Main Page 2](./Demo/static/image/main2.png)
* **🪐 3D Solar System View**
![Solar System 3D](./Demo/static/image/solar1.png)
![Solar System 3D 2](./Demo/static/image/solar2.png)
![Solar System 3D 3](./Demo/static/image/solar3.png)
![Solar System 3D 4](./Demo/static/image/solar4.png)
* **🧮 Calculating Tools**
![Calcus Page](./Demo/static/image/calcusPage.png)
* **Space Facts**
![Facts Page 1](./Demo/static/image/factsPage1.png)
![Facts Page 2](./Demo/static/image/factsPage2.png)
![Facts Page 3](./Demo/static/image/factsPage3.png)
![Facts Page 4](./Demo/static/image/factsPage4.png)
* **🛰️ Tracking & News**
![ISS Tracker](./Demo/static/image/ISSTracker.png)
![News Page](./Demo/static/image/SpaceNewsEvents.png)

## 🚀 Installation & Setup
* **Clone the repository:**
* git clone [https://github.com/sofiakiosova37-boop/Deno-](https://github.com/sofiakiosova37-boop/Deno-)
cd stellarview
* **Set up virtual environment:**
* python -m venv venv
* Activate (Windows):
venv\Scripts\activate
* Activate (Mac/Linux):
source venv/bin/activate
* **Install dependencies:**
pip install -r requirements.txt
* **Run the app:**
python main.py

## 📜 License
This project is licensed under the MIT License.

