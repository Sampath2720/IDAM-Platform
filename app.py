from flask import Flask, render_template

app = Flask(__name__)

requests = [
    {
        "request_id": "REQ0001",
        "employee": "Sampath DhanunjayM",
        "department": "IT",
        "status": "Pending"
    },
    {
        "request_id": "REQ0002",
        "employee": "Rakesh",
        "department": "Finance",
        "status": "Approved"
    },
    {
        "request_id": "REQ0003",
        "employee": "Ram",
        "department": "Finance",
        "status": "Approved"
    },
    {
        "request_id": "REQ0004",
        "employee": "Rami",
        "department": "Finance",
        "status": "Approved"

    }
]

@app.route("/")
def dashboard():
    return render_template(
        "index.html",
        requests=requests,
        total=len(requests),
        approved=sum(1 for r in requests if r["status"] == "Approved"),
        pending=sum(1 for r in requests if r["status"] == "Pending"),
    )

if __name__ == "__main__":
    app
