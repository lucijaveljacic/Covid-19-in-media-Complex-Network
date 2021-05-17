# __Covid 19 in media - Linguistic Complex Network__

This project was created as a part of the course called Knowledge Management (Upravljanje znanjem). 

<b>Faculty:</b> Department of Informatics, University of Rijeka

<b>Author:</b> Lucija Veljačić
  
<b>Mentor:</b> izv. prof. dr. sc. Ana Meštrović
  
<b>Programming language:</b> Python 3

<hr>

## Description

The purpose of this project is to further analyse data collected from a Croatian web portal  [Požeška kronika](https://pozeska-kronika.hr).

The aim of the project is to analyse keywords during 4 time periods and to identify and rank keywords with respect to certain measures of centrality. The analysis is performed to find out whether the obtained keywords were related to the topic of the coronavirus pandemic that took off in the observed period.

### Technical information

__OS:__ Windows 10

__Tools and software:__
* PyCharm
* Python 3.8
* Gephi

__Packages:__


<hr>

## Phase 1 - Data preparation

### Script __preparation.py__

In the first phase, data is being prepared and newspaper articles (1602 articles in total) are grouped into 4 groups, as follows:

* 1. Group: all articles created in the period __1.1.2020.-24.2.2020. - 281 articles__
* 2. Group: all articles created in the period __25.2.2020.-13.3.2020. - 118 articles__
* 3. Group: all articles created in the period __14.3.2020.-11.5.2020. - 481 articles__
* 4. Group: all articles created in the period __12.5.2020.-25.8.2020. - 722 articles__

The script __preparation.py__ reads the data from the __podaci.csv__ file and stores the text data from the Title and Text columns in a new 'Text' column.

The time period is then defined by setting the start and end dates. The values of the Text column for the defined period of time are extracted from the loaded data and stored in the file __prva.txt__ (for the __first__ data group).

* 1. Group - __prva.txt__
* 2. Group - __druga.txt__
* 3. Group - __treca.txt__
* 4. Group - __cetvrta.txt__

## Phase 2 - Construction of the linguistic network

## Phase 3 - Analysis of the linguistic network

## Phase 4 - Analysing results
