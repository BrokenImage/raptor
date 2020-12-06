# To run on machine locally
## Set up Flask server 
Must have `virtualenv` python package installed. From root directory, type
```
cd api
virtualenv env 
source env/bin/activate
pip install -r requirements.txt
python app.py
```
Go to http://localhost:5000 to try out the API. Use images from the test-images folder.

## Set up React 
Must have `Node.js` installed. From root directory, type
```
cd web
npm install 
npm start
```
Go to http://localhost:3000 to view frontend. Currently, requests can not be made to the API from the frontend. We're working on fixing this issue.  

<br>

# To run on Docker 
Instructions will be available soon