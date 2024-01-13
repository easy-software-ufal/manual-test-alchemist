# Creating a venv
We advise the creation of a virtual enviroment. Run this:
`python -m venv venv`
Then, activate the venv.

on linux:
`source ./venv/bin/activate`

on windows:

`.\venv\Scripts\`

Now, you must install the dependencies.

# Installing
To run the program, you must install some packages. Run this: 

`pip install -r requirements.txt`

After downloading everything, you must download spacy's models.

`python -m spacy download en_core_web_trf`
`python -m spacy download en_core_web_lg`

After this, you are done installing.

# Running
To run the program, ensure that you are on the `ManualTestAlchemist` folder. Then, run

`streamlit run interface.py`

This will open a server. Navigate to http://localhost:8501 to access the server.

Select your file, then your test. The tool will show before and after the transformation.

