[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/laughlin/automated-testing/carlos)

Carlos' Version

# Automated Testing Tools
Holds Jupyter Notebooks containing python script used to automate the implementation and testing of SEO updates

# How to run in browser
Click on the above "Launch Binder" button. This will open the notebook in browser. If you wish to use any libraries not already installed, you'll need to fork the repo, and updates to requirements.txt to reflect the new libraries, push, and then go to mybinder.org to re-push the notbook into the cloud.

## Alternative way to run the notebook
Python 3.x, pip, and virtualenv must be installed. Then, from the main directory folder of the repo, call
```
$ virtualenv master-lock-seo-scripts-env
$ source master-lock-seo-scripts-env/bin/activate
(master-lock-seo-scripts-env) $ pip install -r requirements.txt
(master-lock-seo-scripts-env) $ jupyter notebook
```

## Alternative way 3 to run the notebook
Jupyter Notebook and Python 3.x must be installed on your machine. The easiest way to do this is to install Anaconda (https://www.anaconda.com/download) which will install all dependencies along with JN. 

Then, navigate to this repo in your folder structure
`$ cd path/to/repo`

Install virtual env and then create an environment based on the requirements.txt file located at the base directory of the repo.
```
$ pip install virtualenv
$ virtualenv master-lock-seo-scripts-env
$ source master-lock-seo-scripts-env/bin/activate
(master-lock-seo-scripts-env) $ pip install -r requirements.txt
```

Once this is installed, open Jupyter Notebooks by going to your command prompt terminal and typing:

`(master-lock-seo-scripts-env) $ jupyter notebook`

This will open Jupyter Notebook in your browser. You can then navigate to this repo and select the repo.
