# Student utility app

## Purpose

This small app brings together some useful information to help students.
Feel free to use and expand on this as you want

## Features
- [X] Link to the current semester [Schedule](https://ifrinf.ub.ro/wp-content/uploads/2024/11/ORAR_Info_IFR_sem_I_2024-2025_definitiv.pdf)
- [X] Link to the list of [set exams page](https://www.ub.ro/stiinte/studenti/programare-examene)
- [X] Link to the [University secretary contact page](https://www.ub.ro/stiinte/contact)
- [X] Link to the [payment platform](https://smartums.ub.ro/as/dashboard)
- [X] University image for branding with error handling
- [X] Week time tracker for how many weeks there are left in the current semester
- [X] Bat file to mimic an exe, yet you need to adjust the paths inside the file for it to work

## Not a bug, but a feature
- The image is intented to be local, and trimmed down, instead of fetching it from the [University site](https://ifrinf.ub.ro/wp-content/uploads/2024/09/LOGO_INFORMATICA_IFR.png) to avoid generating needless traffic to the university server
- The image was downsized to 100x100 instead of using a library to process the downsizing for efficiency, also PIL library has been deprecated
- The bat file is there to make it easy to run without the IDE or a terminal, should you have python already installed
- The hardcoded link to the pdf file could be automated with Appium/Selenium to find the button however, that increases the scope and complexity of the app, forcing to have waits and handling 

