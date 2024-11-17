from flask import Flask, render_template, request
import random

app = Flask(__name__)

"""
#This code is for using API Keys
# Add your Google Maps API key here
GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"

# Fetch route details using Google Maps Distance Matrix API
def get_route_data(start, end):
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": start,
        "destinations": end,
        "key": GOOGLE_MAPS_API_KEY,
        "mode": "driving",  # You can also use "walking", "bicycling", or "transit"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        try:
            route_info = data["rows"][0]["elements"][0]
            return {
                "distance": route_info["distance"]["text"],
                "time": route_info["duration"]["text"],
                "carbon_savings": "15%"  # Simulating eco-savings
            }
        except (KeyError, IndexError):
            return {"error": "Invalid response from API"}
    else:
        return {"error": "Failed to fetch data from API"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plan-route", methods=["POST"])
def plan_route():
    start = request.form.get("start")
    end = request.form.get("end")
    if not start or not end:
        return "Start and End locations are required", 400
    
    route_data = get_route_data(start, end)
    if "error" in route_data:
        return f"Error: {route_data['error']}", 500
    return render_template("results.html", start=start, end=end, route_data=route_data)
"""

# Simulated API for route data (to be replaced with real APIs for traffic, emissions, etc.)
def get_route_data(start, end):
    return {
        "eco_route": {
            "distance": f"{random.randint(10, 100)} km",
            "time": f"{random.randint(15, 150)} min",#replace with api for accurate results
            "carbon_savings": f"{random.randint(10, 30)}%"
        },
        "fastest_route": {
            "distance": f"{random.randint(8, 80)} km",
            "time": f"{random.randint(10, 100)} min",
            "carbon_savings": "0%"
        },
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plan-route", methods=["POST"])
def plan_route():
    start = request.form.get("start")
    end = request.form.get("end")
    route_data = get_route_data(start, end)
    return render_template("results.html", start=start, end=end, route_data=route_data)

if __name__ == "__main__":
    app.run(debug=True)
