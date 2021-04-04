<h3 align="center">Machiron</h3>

  <p align="center">
    Web app to monitor DICOM exams with additional information
    <br />
     <a href="https://github.com/lldenisll/frontmachiron" target="blank">Para português, acesse o repô do front-end</a>
    <br />
    <a href="https://lldenisll.github.io/#/" target="blank">Open Front-end</a>
    ·
    <a href="https://github.com/lldenisll/frontmachiron" target="blank">Front-End Repository</a>
   </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">About the project</h2></summary>
  <ol>
    <li>
      <a href="#about">About</a>
      <ul>
        <li><a href="#tecnologies">Tecnologies</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#tasks">Tasks</a></li>
    <li><a href="#next-steps">Next Steps</a></li>
    <li><a href="#my-contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About
This project includes a script to read DICOM files and colletct the main information, also the back-end provides a API to include other information
on each DICOM exam. In addition, it also collect the images from each exam. The front-end provides a simple dashboard with the main information
regarding each pacient

### Tecnologies

* []() Python + Django + Django Rest Framework
* []() VueJS
* []() GitHub + Postgresql + Heroku



<!-- GETTING STARTED -->
## Getting Started

If you wish for a local copy:

### Instalação back-end

1. Clone repository
   ```sh
   git clone https://github.com/lldenisll/doctor_backend
   ```
2. Create virtual env
   ```sh
   python3 -m venv /path/to/virtual/env
   ```
   3. Activate virtual env
   ```sh
   source/path/virtual/env/bin/activate
   ```
3. Install requirements
   ```sh
   pip install requirements.txt
   ```
3. Make migrations
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Run server!
   ```sh
   python manage.py runserver
   ```
### Front-end install

1. Clone repository
   ```sh
   git clone https://github.com/lldenisll/frontmachiron
   ```
2. Install
   ```sh
   npm install
   ```
3. Run
   ```sh
   npm run serve
   ```
### Database
If you wish to run local with your databse, please insert your local database information on the file settings.py at config folder, and make migrations again

## Tasks

Task 01 - API build with python and DJANGO REST FRAMEWORK, to get info on each DICOM exam. Script created to collect the data on each folder. And set up a JSON file that can
be loaded easily on our database (python manage.py loaddata data.json). The script also uses the matplotlib to create images based on the pixel_array parameter.

Task 02 - Model created in order to accept data from a json file (created on task1), also the model include the informations on diagnosis. The model was build in a way that
a radiologist can input/update data regarding diagnosis on each exam. And the researcher can view all the details (the researcher can also include diagnosis - for a better UX) 

Task 03 - Front end developed using VueJS, and a little material design kit to help. The front end get information from the rest api, and allows the user to 
include and update information on the database (task2). It also shows a table to describe the items of the task 1. And finnaly the researcher can see the details on each exam li images, slice thickness..

## Next steps
Include the option to the user of the web app to upload folders with lots of DICOM files regarding one exam. In this case the back-end will read and salve the
relevant datas from each exam on the database. If relevant, the script can also create a gif of each slice image.


## My contact

Dênis Gonçalves dos Santos 
[![LinkedIn][linkedin-shield]][linkedin-url]



[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/denis142/
