[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/laughlin/automated-testing/teresa)

Teresa's Version

# Automated Testing Tools
Holds Jupyter Notebooks containing python script used to automate the implementation and testing of SEO updates.

## How to run
Each tool is in its own folder consisting of the notebook with code to run, along with two folders, "Inputs" and "Results".

To use the tools, a person places an xslx with the correct format in the "Inputs" folder of the tool they wish to use. For examples of format, see the Example.xlsx file contained in each "Inputs" folder.

Then, after opening the notebook, the user alters the User Input cell near the top of the notebook to reflect their input file's name and sheet name, along with a couple true/false questions. Once everything is input and correct in the cell, the user can run all of the code by going to the top of the notebook and selecting Cell -> Run All.

Once results have been calculated, outputted results will then be visible near the bottom of the notebook if all goes well. These same results will also be saved to an xlsx file, timestamped with the current date and time, in the "Results" folder of the tool. If using these tools with the binder, make sure to download the outputted files to your local machine before closing the program. Otherwise, they will be lost.

## How to open in browser
Click on the above "Launch Binder" button. This will open the notebook in browser. If you wish to use any libraries not already installed, you'll need to clone the repo locally, add updates to requirements.txt to reflect the new libraries, push, and then select the "Launch Binder" button above to re-launch the notebook into the cloud.

## Alternative way to open the notebook
Python 3.x, pip, virtualenv, and Jupyter Notebook must be installed. Then, after changing the directory to the main directory folder of the repo in the Command Prompt (Windows) or Terminal (Mac), call:

```
$ virtualenv automated-testing-tools-env
$ source automated-testing-tools-env/bin/activate
(automated-testing-tools-env) $ pip install -r requirements.txt
(automated-testing-tools-env) $ jupyter notebook
```

or, if you prefer to work in Conda,


```
MAC

$ conda env create automated-testing-tools-env -f requirements.txt
$ source activate automated-testing-tools-env
(automated-testing-tools-env) $ jupyter notebook

WINDOWS Anaconda Command Prompt

conda env create automated-testing-tools-env -f requirements.txt
activate automated-testing-tools-env
(automated-testing-tools-env) jupyter notebook
```

For more info on conda environemnts, see this link: https://conda.io/docs/user-guide/tasks/manage-environments.html#activating-an-environment

This will open the notebook in browser.

## Closing the notebook
An individual notebook can be closed by going to the menu and selecting File -> Close and Halt. This saves and closes the notebook. Any remaining wondows containing file directories can also be closed then. This is all you need to do if running through the "Launch Binder" button above. However! If running in the binder, make sure you save any output xlsx files to your local machine before closing! Otherwise they will be lost.

If running locally, there are a few more steps.

Jupyter Notebooks can be closed by going to the Command Prompt (Terminal) and pushing CTRL-C. A message will pop up asking if you're sure you wish to exist. Type 'y' for yes. This then closes the program. The browser windows containing the notebooks will now throw errors and not allow for code manipulation. Make sure to save all progress before closing Jupyter Notebook!

Finally, you can decativate the environment by running

```
MAC

(automated-testing-tools-env) $ source deactivate

WINDOWS Anaconda Prompt

(automated-testing-tools-env) deactivate
```