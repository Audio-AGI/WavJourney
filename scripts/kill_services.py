import os

# Extract values for each application
service_port = os.environ.get('WAVJOURNEY_SERVICE_PORT')

# Execute the commands 
os.system(f'kill $(lsof -t -i :{service_port})')




