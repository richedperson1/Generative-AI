


from pyngrok import ngrok

# Replace 'your-authtoken' with your actual authtoken
ngrok.set_auth_token('2jKSDvO6pSuQe19yr9emrmxa33c_7zCSzinpLKE12jEpD2sFF')

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is your Flask app running with ngrok!"

# Set up the ngrok tunnel
public_url = ngrok.connect(port=5000)
print(" * Ngrok tunnel URL:", public_url)

# Run the Flask app
app.run(port=5000)

# !pip install flask pyngrok
