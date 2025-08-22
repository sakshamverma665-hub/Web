from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>📱 Mobile Tracker</title>
    <style>
        body { background-color: black; color: #00FF00; font-family: monospace; }
        .container { width: 80%; margin: auto; padding: 20px; text-align: center; }
        input[type=text] { width: 60%; padding: 10px; border-radius: 5px; border: none; }
        button { padding: 10px 20px; background: #00FF00; border: none; cursor: pointer; font-weight: bold; }
        .card { border: 1px solid #00FF00; margin: 15px 0; padding: 15px; border-radius: 10px; text-align: left; }
        h1 { font-size: 28px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📱 Mobile Number Tracker</h1>
        <form method="get">
            <input type="text" name="num" placeholder="Enter Mobile Number" required>
            <button type="submit">Search</button>
        </form>
        {% if results %}
            {% for r in results %}
            <div class="card">
                <p>🔥 <b>Name:</b> {{ r.get("Name","N/A") }}</p>
                <p>👨 <b>Father Name:</b> {{ r.get("Father Name","N/A") }}</p>
                <p>📞 <b>Mobile:</b> {{ r.get("Mobile","N/A") }}</p>
                <p>📱 <b>Alt Mobile:</b> {{ r.get("Alt Mobile","N/A") }}</p>
                <p>🌍 <b>Circle:</b> {{ r.get("Circle","N/A") }}</p>
                <p>🏠 <b>Address:</b> {{ r.get("Address","N/A") }}</p>
                <p>🆔 <b>ID Number:</b> {{ r.get("ID Number","N/A") }}</p>
            </div>
            {% endfor %}
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    number = request.args.get("num")
    results = None

    if number:
        url = f"https://sakshamxosintapi.onrender.com/get?num={number}"
        try:
            response = requests.get(url).json()
            if isinstance(response, dict):  
                results = [response]
            elif isinstance(response, list):  
                results = response
        except Exception as e:
            results = [{"Name": "Error", "Father Name": str(e)}]

    return render_template_string(HTML_TEMPLATE, results=results)


if __name__ == "__main__":
    # Render ke liye host="0.0.0.0" aur port=5000 rakho
    app.run(host="0.0.0.0", port=5000)