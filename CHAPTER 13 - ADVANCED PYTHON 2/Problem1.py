# . Create two virtual environments, install few packages in the first one. How do you 
# create a similar environment in the second one? 

# open terminal
# virtualenv env1
# virtualenv env2
# .\env1\Scripts\activate.ps1
# pip install pandas
# pip install pyjokes
# pip freeze > requirements.txt
# deactivate
# .\env2\Scripts\activate.ps1
# pip install -r requirements.txt

# IN REPL
# python
# import pandas  #working