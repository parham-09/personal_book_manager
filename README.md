# Personal book Manager
A simple book manager built with Python for learning git and github 

## Feature
- add multiple task
- save books 
- load saved books
- admin mode
- set book priority
  
## Book priority
each book can have one of these priority levels:
- low
- medium
- high
  
## Reaquirements
- Python
- python-dotenv
  
## Installation
install the Reaquired packages:
```bash
python -m  pip install -r reaquirements.txt
```
## Envoirment Setup 
creat a `.env` file in the project folder 
use `.env.example` as a template

Add your admin password

```env
admin_pass=your_password_here
```
replase  `your_password_here` with your own admin password


## Screen shot

!["all project"](<!(image.png).png>)



## Run the program
run the admin
```bash
python main.py
```

## Project Structure
`main.py` : These files contain information regarding books and questions, as well as the password required from the user.

`books.py` : This file is also intended to provide improvements, reduce complexity, and support `main.py`, as well as the password-related code and the book-related components.

`.gitignore` : For security reasons, this file should not be treated as a C file.

`.env.example` : This file is for the protection of user privacy.

`requirements.txt`:This file is also for a new library.

`images` : This folder is for the project photos.

## How It Works
```bash
When you run this program, it first asks for your username and then displays a welcome message. It then asks if you would like to enter administrator mode; if you answer "yes," it prompts for the user password. If you answer "no," it proceeds directly. Next, it asks how many book titles you would like to enter. Once you provide the book titles, the program displays a farewell message and terminates.
```
## Troubleshooting
`FileNotFoundError` You might take offense at it.
`JSONDecodeErro`  If books.json is empty
`python-dotenv` In case this book cannot be found or downloaded

Password not being read from `.env`
