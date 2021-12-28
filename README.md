# This is the Pycharm Broker Game by PythonicInquisition
Available under **[Pybroker.vision](https://pybroker.vision)**


Authors: Daniel Ebert, Luca Müller, Luca Weissbeck, Ben Schaper, Jannik Sinz
- daniel.ebert@ibm.com, luca.mueller1@ibm.com, luca.weissbeck@ibm.com, ben.schaper@ibm.com, jannik.sinz@ibm.com  
  
Project Start: 24.10.2020  
Project End: 22.11.2020  

## Requirements
Python: 3.8
### with pip:
```
pip3 install -r requirements.txt
```  
### with poetry:
```
poetry init  
for item in $(cat requirements.txt); do   poetry add "${item}"; done
```


## BackEnd - Usage
To run the server, please execute the following from the BackEnd-root directory:

```
python3 -m swagger_server
```

## BackEnd - Docs
https://pybroker.readme.io/

## Start FrontEnd:

To start the frontend, change directory to the root folder of the repository. Then run ```streamlit run FrontEnd/orchestrator.py```. This will run the streamlit server.
