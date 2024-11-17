AI-Powered Personalized Green Route Planner

Project Overview

The AI-Powered Personalized Green Route Planner is a web-based application that suggests eco-friendly routes for drivers. Using the Google Maps Distance Matrix API, the system calculates the most environmentally efficient routes while balancing fuel efficiency and user convenience. It also provides real-time carbon savings to promote sustainable driving practices.

Features

For Customers:

Eco-Optimized Routes: Suggests the most environmentally friendly route based on real-time data (e.g., traffic, road conditions).
Personalized Driving Experience: Learns user driving habits and tailors routes for convenience and efficiency.
Carbon Savings Display: Real-time feedback on carbon emission savings with a gamified rewards system.

For Volkswagen:

Sustainability Leadership: Promotes green driving initiatives to reduce carbon footprints.
Data-Driven Insights: Aggregates data to showcase emissions reductions and optimize vehicle designs.
Enhanced Customer Retention: Offers practical benefits and cost savings for environmentally conscious users.

Tech Stack

Backend: Flask (Python)

Frontend: HTML, CSS

API: Google Maps Distance Matrix API

Database: No database used (for demonstration purposes)

Styling: Custom CSS

Prerequisites

Before running the project, ensure you have the following:


Python 3.x installed on your machine.

A Google Maps API key. (Refer to the Google Maps API Documentation to obtain one.)

Flask installed (pip install flask).

Requests library installed (pip install requests).

Installation

Clone the repository:


git clone https://github.com/Ganir19/EcoFriendly_GreenRoute_Planner.git

Install the required Python libraries:


pip install -r requirements.txt

Add your Google Maps API key to the code:

Open app.py and replace YOUR_GOOGLE_MAPS_API_KEY with your actual API key.

Running the Application

Start the Flask server:


python app.py

Open your browser and navigate to:

http://127.0.0.1:5000/

Enter the start and end locations to get eco-friendly route suggestions.

green-route-planner/

│

├── app.py                # Flask application

├── requirements.txt      # Python dependencies

├── templates/

│   ├── index.html        # Home page for route input

│   └── results.html      # Results page displaying route details

└── static/

|     └── css/

|        └── styles.css    # Styling for the application


Screenshots

Home Page

Enter start and end locations to plan a route.


Results Page

View eco-friendly route details, including distance, time, and carbon savings.


Future Enhancements

Integration with user accounts for personalized route histories.

Advanced analytics for eco-driving behavior.
Mobile app version for Android and iOS.
