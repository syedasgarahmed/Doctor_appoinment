from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (for demonstration purposes)
doctors = [
    {
        "id": 1,
        "name": "Dr. John Smith",
        "specialization": "Internal Medicine",
        "available_days": ["Monday", "Tuesday", "Wednesday"],
        "max_patients": 5,
    },
    {
        "id": 2,
        "name": "Dr. Jane Doe",
        "specialization": "Pediatrics",
        "available_days": ["Tuesday", "Thursday", "Friday"],
        "max_patients": 6,
    },
]

# Defining a route to list all doctors
@app.route("/doctors", methods=["GET"])
def list_doctors():
    return jsonify(doctors)

# Defining a route to retrieve details of a specific doctor
@app.route("/doctors/<int:doctor_id>", methods=["GET"])
def get_doctor(doctor_id):
    doctor = next((doc for doc in doctors if doc["id"] == doctor_id), None)
    if doctor:
        return jsonify(doctor)
    return jsonify({"error": "Doctor not found"}), 404

# Defining a route to book an appointment with a doctor
@app.route("/appointments", methods=["POST"])
def book_appointment():
    data = request.get_json()
    doctor_id = data.get("doctor_id")
    appointment_date = data.get("appointment_date")
    return jsonify({"message": "Appointment booked successfully"})

if __name__ == "__main__":
    app.run(debug=True)
