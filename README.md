# IDS706Project1
Continuous Delivery of Flask/FastAPI Data Engineering API on GCP/AWS/Azure

# Online Recipe Scraper
This FastAPI helps you to find interesting recipes related to an ingredient. 
You can enter ingredients like chocolate, milk, and egg, etc. 
The API will return the TOP 10 recipes that's related to the ingredient!
Enjoy the recipe and make delicious food!

# Instruction:
* Create a new Cloud9 Enviornment
* Git clone this repository in the terminal
* In the terminal, type in python3 -m venv ~/.venv
* Then type in source ~/.venv/bin/activate
* cd to the project directory IDS706Project1
* In the terminal, type in make install
* Then type in python main.py
* Go to ec2 instance, click on the instance associated with your Cloud9 Env.
* Copy the public IP address, and paste it in a new browser page with port number 8080. eg. 3.236.173.81:8080
* Read the instruction page, then add /docs to 3.236.173.81:8080 eg. 3.236.173.81:8080/docs
* Click on the section /get_recipe/{name}, then click on the Try it out button
* Type in an ingredient of your choice, then try out the recipe recommended! 
