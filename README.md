# This is the Pycharm Broker Game by PythonicInquisition
Available under **[Pybroker.de](https://pybroker.de)**


Authors: Daniel Ebert, Luca Müller, Luca Weissbeck, Ben Schaper, Jannik Sinz
- daniel.ebert@ibm.com, luca.mueller1@ibm.com, luca.weissbeck@ibm.com, ben.schaper@ibm.com, jannik.sinz@ibm.com  
  
Project Start: 24.10.2020  
Project End: 22.11.2020  

## Preview
### Buying Stocks 
![screencapture-localhost-8501-2021-12-29-13_42_59](https://user-images.githubusercontent.com/62757957/147664009-a6490873-d65c-4911-84d1-3b5d83cf80fc.png)
### Selling Stocks
![screencapture-localhost-8501-2021-12-29-13_44_14](https://user-images.githubusercontent.com/62757957/147664079-914c3782-3c55-4d2e-b9c8-7c68cebb0e0e.png)
### Stock Screener
![screencapture-localhost-8501-2021-12-29-13_41_58](https://user-images.githubusercontent.com/62757957/147664103-9eaf8f82-0556-4d4d-b57b-c694d61eebef.png)
### Settings
![screencapture-localhost-8501-2021-12-29-13_43_21](https://user-images.githubusercontent.com/62757957/147664290-5f46e4ff-da9b-4896-9572-8589f0e7ec60.png)

### Dark Mode Ready
<img width="1788" alt="Screenshot 2021-12-29 at 13 46 12" src="https://user-images.githubusercontent.com/62757957/147664203-9744ad3e-5e24-4fdd-b00d-b979019699ce.png">

## Architecture / Infrastructure
![Uberblick_der_AnwendungsarchitekturPRESET](https://user-images.githubusercontent.com/62757957/147664785-f0758d24-0dc3-43ee-9b5f-f0791451d412.png)

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
