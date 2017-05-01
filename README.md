# Learning Bowtie - v0.3.2
I'm learning Python [bowtie](https://github.com/jwkvam/bowtie)!

[Bowtie](https://github.com/jwkvam/bowtie) is used to quickly and easily create interactive dashboards in Python. It's basically the Python version of Shiny for R.

I will be working with macOS for these instructions.

## Step 1: Installation

Installation will require the use a terminal. On macOS, I just use the Terminal app. To open it, try typing ```CMD+Spacebar``` on your keyboard, then type the first few letters of "Terminal". Some of these steps will also require administrator privileges, so use of the ```su``` command may be required if you are not an administrator.

### 1.1 Install Homebrew (macOS)

We will need use a package manager called Homebrew to install another package we'll need. From the command line in the Terminal app:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### 1.2 Install Node

```
brew install node
```

### 1.3 Install Yarn

```
npm install -g webpack yarn
```

### 1.4 Install virtualvenv

Using virtual environments makes controlling the work environment and dependencies much easier. I recommend installing virtualvenv, but it's also possible to just skip to the __Install Bowtie__ step.

```
pip install virtualenv
```

### 1.5 Create a Virtual Environment

Make sure you are in the directory that you plan to create your first Bowtie app in. Or, you can create one and change directories to it in one command.

```
mkdir my_bowtie_project && cd my_bowtie_project
```

_Note: 'my_bowtie_prject' can be named anything you want._

To create the virtual environment, just enter:

```
virtualenv venv
```

Finally, to activate the virtual environment, type:

```
venv/bin/activate
```

Now newly installed packages will become a part of this project's virtual environment. simply type ```deactivate``` when you are finished working on this project, or ```venv/bin/activate``` to work on it again. _You must be in your project's directory for these commands to work!_

### 1.6 Install Bowtie

```
pip install bowtie
```

## Step 2: Running an Interactive Example

Some additional packages are required to run the interactive examples in this repository. To install all of them at once, enter the following command in your terminal:

```
pip install -r requirements.txt
```

The first Bowtie example can be built with the following command:

```
python step_1.py build
```

After the build is finished, enter the following command:

```
python step_1.py serve
```

Then, open a web browser and navigate to [http://0.0.0.0:9991](http://0.0.0.0:9991). You are now able to interact with the app.

_**Bug notice:_ After the build step, you must make the following edit to ```build/src/server.py``` for the timer to work:

change ```socketio.run(app, host=host, port=port)``` to ```socketio.run(app, host=host, port=port, use_reloader=False)```.

## Resources

[Bowtie Docs](http://bowtie-py.readthedocs.io/en/latest/index.html)  
[Bowtie on GitHub](https://github.com/jwkvam/bowtie)  
[Bowtie live demo](https://bowtie-demo.herokuapp.com/)  
[The Hitchhiker's Guide to Python](http://python-guide-pt-br.readthedocs.io/en/latest/)  