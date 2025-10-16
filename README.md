# Rooftop Rainwater Harvesting (RTRWH) Assessment & Recommendation Engine

A comprehensive web application designed to assess the feasibility of rainwater harvesting for any given location, providing detailed analysis, personalized recommendations, and information on government subsidies.

![RTRWH Application Showcase](https://via.placeholder.com/800x400/1e293b/22d3ee?text=Project+Showcase+Image)

## 🌟 Key Features

- **Interactive Location Selection:** Users can pinpoint their property using an interactive map (powered by MapTiler) with both street and satellite views, or use their device's GPS.
- **Multi-Step Data Collection:** A guided, multi-page form collects essential user, property, and water usage details for a precise assessment.
- **Comprehensive Backend Analysis:** A powerful Flask backend performs detailed calculations for:
  - **Feasibility:** Compares rainwater harvesting potential against household demand.
  - **User Categorization:** Classifies the property into one of six distinct categories based on size, rainfall, and geological data.
  - **Safety Checks:** Validates the safety of artificial groundwater recharge based on soil type, groundwater depth, and contamination risks.
  - **Cost & Payback Analysis:** Provides estimated installation costs and calculates the financial payback period.
  - **Purification Recommendations:** Suggests a water treatment sequence based on the user's intended use.
- **Dynamic & Visual Reports:** The results are displayed on a beautifully designed, animated page featuring charts (via Chart.js) for easy comparison of supply vs. demand.
- **PDF Report Generation:** Users can download a clean, text-based summary of their assessment report, generated on the backend with FPDF2.
- **Government Subsidy Checker:** An integrated module that checks user eligibility for national and state-level rainwater harvesting schemes and regulations.

## 📸 Screenshots

*(Add screenshots of your application here to showcase the UI)*

**1. Onboarding & Consent**
![Onboarding Page](https://via.placeholder.com/400x250/1e293b/ffffff?text=Onboarding+Screen)

**2. Location & Data Input**
![Data Input Page](https://via.placeholder.com/400x250/1e293b/ffffff?text=Data+Input+Screen)

**3. Feasibility Report**
![Results Page](https://via.placeholder.com/400x250/1e293b/ffffff?text=Results+Screen)

**4. Subsidy Checker**
![Subsidy Checker Page](https://via.placeholder.com/400x250/1e293b/ffffff?text=Subsidy+Checker)

## 🛠️ Technology Stack

- **Backend:**
  - **Python 3**
  - **Flask:** Micro web framework.
  - **SQLAlchemy:** Database ORM for SQLite.
  - **Pandas:** For processing location data from CSV.
  - **FPDF2:** For server-side PDF generation.
- **Frontend:**
  - **HTML5**
  - **CSS3** (with **Tailwind CSS**)
  - **JavaScript (ES6+)**
- **Mapping & Geocoding:**
  - **MapLibre GL JS:** For the interactive map.
  - **MapTiler:** For map tiles, geocoding, and reverse geocoding services.
- **Data Visualization:**
  - **Chart.js:** For creating dynamic charts on the results page.

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/rtrwh-assessment-tool.git
cd rtrwh-assessment-tool
```

### 3. Set Up a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```



### 5. Run the Application

Once the dependencies are installed and the API key is configured, you can start the Flask server.

```bash
python app.py
```

The backend server will start running on `http://127.0.0.1:5000`. Open this URL in your web browser to access the application.

## 📂 Project Structure

```
Rain Water Harvesting/
├── static/
│   └── js/
│       ├── index.js
│       ├── location-input.js
│       └── subsidy-checker.js
├── templates/
│   ├── index.html
│   ├── location-input.html
│   ├── results.html
│   └── subsidy-checker.html
├── data/
│   └── mock_location_data.csv
├── app.py
├── recommendations.py
├── requirements.txt
└── rtrwh_data.db (generated)
```

This project is licensed under the MIT License. See the `LICENSE` file for details.

