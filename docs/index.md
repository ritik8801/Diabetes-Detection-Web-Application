# Project Documentation
 
This is the Documentatin for my project. I ended up putting a lot of effort into the CI/CD Part as i easily get obsessed with automation.

## 1. git

<a href="https://github.com/ritik8801/Diabetes-Detection-Web-Application">Github Repository</a>

## 2. UML 

The UML Diagrams were made in Miro.
You can find the definitions here: <a href="https://github.com/ritik8801/Diabetes-Detection-Web-Application/tree/main/UML%20Diagrams">UML></a>

### Use Case Diagram
![file](./UML Diagrams/Use Case Diagram.jpg)

### State Diagram
![file](./UML Diagrams/State Diagram.jpg)

### Sequence Diagram
![file](./UML Diagrams/Sequence Diagram.jpg)


## 3. Event-Storming/DDD
<iframe width="768" height="432" src="https://miro.com/app/board/uXjVPpa-1xA=/?share_link_id=345011287833" frameBorder="0" scrolling="no" allowFullScreen></iframe>

## 4. Metrics

I used <a href="https://sonarcloud.io/project/overview?id=ritik8801_Diabetes-Detection-Web-Application" target="_blank">Sonarcloud</a>, which is sonarqube in the cloud, as i wanted the whole project to be cloud based.
It also gives you the ability to embed lot's of different badges:
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ritik8801_Diabetes-Detection-Web-Application&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=ritik8801_Diabetes-Detection-Web-Application)

## 5. Clean Code

My Clean Code Development Pdf: <a href="https://github.com/ritik8801/Diabetes-Detection-Web-Application/blob/main/Clean%20Code%20Development/Clean%20Code%20Development.pdf">Clean Code Development</a>


## 6. Build Management + 8. Continuous Delivery

The build management and continuous delivery are also completely cloud based.

I used Github Actions for the build management and continuos delivery because all the services i use integrate extremely well with it. 

My Github Actions Pipeline yaml: <a href="https://github.com/ritik8801/Diabetes-Detection-Web-Application/blob/main/.github/workflows/github%20actions.yml">github actions.yml</a>

[![Build Status](https://github.com/ritik8801/Diabetes-Detection-Web-Application/actions/workflows/github%20actions.yml/badge.svg)](https://github.com/ritik8801/Diabetes-Detection-Web-Application/actions/workflows/github%20actions.yml)


### Build Management 

The Github Actions Pipeline runs the unit tests by calling pytest and is also connected to sonarcloud. 

### Continuos Delivery

When the build is successful e.g. sonarqube and pytest are happy the documentation is regenerated and published to <a href="https://github.com/JLiekenbrock/lyrics-visualiser/tree/gh-pages">github pages</a>.
There is  <a href="https://jliekenbrock.github.io/lyrics-visualiser/lyrics-visualiser/index.html">technical documentation</a> generated based on the source code as well as what you are [reading right now](https://jliekenbrock.github.io/lyrics-visualiser/index.html).

[Documentation Code](https://github.com/JLiekenbrock/lyrics-visualiser/blob/main/docs/index.md)

THe app is also deployed to <a href="http://lyricsvis.herokuapp.com/">heroku</a> on every successfull commit.

## 7. Unit-Tests
The [Unit tests ](https://jliekenbrock.github.io/lyrics-visualiser/lyrics-visualiser/tests/index.html) are written with the help of the python library pytest.

## 9. IDE
I use visual studio code as main IDE as it has great support for my main languages, namely R and Python.
It also allows you to use the <a href="https://copilot.github.com/">Github Copilot AI</a>, which is great in my opinion. It is especially useful when trying out new things like libraries, because it often comes up with useful suggestions which helps exploring things faster.
The in-built explorer of vscode is also great as it easily let's you search through all files in your opened directory. You can even replace 
code across multiple files at once. 

Shortcuts i like:
Shift+Enter is very useful. It runs the selected lines of code in a python terminal in the IDE.
Otherwise i'm mostly using the standard shortcuts everyone else uses.

## 10. DSL
I created a class that uses the style of the Cars example in moodle:
<a href="https://jliekenbrock.github.io/lyrics-visualiser/lyrics-visualiser/components/songsearch.html">"DSL" Class</a>.
I also used a DSL like Regex in the module nlp.py.

## 11. Functional Programming
I tried to use functional style where possible.
The function <a href= "https://jliekenbrock.github.io/lyrics-visualiser/lyrics-visualiser/components/nlp.html#components.nlp.clean_lyrics">clean_lyrics</a> is written as sequence of function calls.
It does not store any variables and does not manipulate any objects out of it's scope, 
it just performs transormations on the data and returns the result.

In the main programm i used functions as arguments in the update_graph callback:
<a href="https://jliekenbrock.github.io/lyrics-visualiser/lyrics-visualiser/dashlyrics.html#lyrics-visualiser.dashlyrics.update_graph">function chaining</a>
