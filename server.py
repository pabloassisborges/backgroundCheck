#Importing Libary
from flask import Flask, render_template
import connexion

# Create the application instance
options = {'swagger_path': './'}
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/server/')

# Function calls "home" webpage
def home():
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)