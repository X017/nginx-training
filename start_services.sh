#!/bin/bash

# Define apps and ports
declare -A apps
apps["simple-blog"]="8001 8002"
apps["twitter-clone"]="8003 8004"

# Start instances
for app in "${!apps[@]}"; do
    echo "Starting instances for $app..."
    
    # Change directory to the app folder
    cd "$app" || { echo "Failed to access $app directory"; exit 1; }

    # Activate virtual environment
    source venv/bin/activate

    # Run Django app instances on specified ports
    for port in ${apps[$app]}; do
        echo "Starting $app on port $port..."
        nohup python manage.py runserver "0.0.0.0:$port" > "server_$port.log" 2>&1 &
    done

    # Deactivate virtual environment and return to root directory
    deactivate
    cd ..
done

echo "All Django apps are running!"

