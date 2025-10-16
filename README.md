Rainwise — Rooftop Rainwater Harvesting (RTRWH) Assessment & Recommendation Engine

A comprehensive web application designed to assess the feasibility of rooftop rainwater harvesting for any given location. It provides detailed analysis, personalized recommendations, and information on government subsidies, helping users make sustainable water management decisions with ease.

Key Features

Interactive Location Selection
Users can pinpoint their property using an interactive MapTiler map with both street and satellite views or use their device’s GPS.

Multi-Step Data Collection
A guided, multi-page form collects essential details such as user info, property dimensions, and water usage for accurate analysis.

Comprehensive Backend Analysis
The Flask backend performs robust calculations for:

Feasibility Assessment – comparing rainwater harvesting potential vs. household demand.

User Categorization – classifying properties by area, rainfall data, and geological parameters.

Safety Validation – verifying safety for artificial groundwater recharge.

Cost & Payback Analysis – estimating system cost and expected return period.

Purification Recommendations – suggesting optimal water treatment processes based on intended usage.

Dynamic Reports & Visualizations
Animated, interactive results using Chart.js for clear and intuitive interpretation.

PDF Report Generation
Downloadable, professional-quality reports generated with FPDF2.

Government Subsidy Checker
Automatically checks eligibility for relevant national/state rainwater harvesting schemes.

 Technology Stack

Backend: Python 3, Flask, SQLAlchemy, Pandas, FPDF2
Frontend: HTML5, CSS3 (Tailwind CSS), JavaScript (ES6+)
Mapping & Geocoding: MapLibre GL JS, MapTiler
Data Visualization: Chart.js

Setup and Installation
1. Prerequisites

Python 3.8 or higher

pip (Python package installer)

2. Clone the Repository
git clone https://github.com/amulya817/Rainwise.git
cd Rainwise

3. Create a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate


macOS/Linux

python3 -m venv venv
source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Run the Application
python app.py


Then open http://127.0.0.1:5000
 in your browser.

Project Structure
Rainwise/
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

📄 License

This project is licensed under the MIT License — see the LICENSE
 file for details.
