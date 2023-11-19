# RestAPIs.py

![GitHub repo size](https://img.shields.io/github/repo-size/HeitorFM2/RestAPIs.py?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/HeitorFM2/RestAPIs.py?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/HeitorFM2/RestAPIs.py?style=for-the-badge)

> This project is just to show a bit of my knowledge with RestAPIs.py, using Python with the Flask library and a bit of my knowledge in Docker, hosting a database (PostgreSQL) locally through it.

## 🌃 Project structure

> The project has its file structure containing all the routes in the path `< src/routes >` where the path `< src/service >` of that respective route is called, in the service all the rules that happen in the project are made and where the path `< src/repository >` containing all the SQL queries of the project is called.

> If you want, in the path `< src/infra/database >` there is a Postman collection with all the routes already ready.

## 💻 Pre-requisites

Before you start, make sure you meet the following requirements:

- You have installed `Python 3.11`
- Install the `Black Formatter` formatter on your VSCode

## 🚀 Installing <RestAPIs.py>

To access the <RestAPIs.py>, follow these steps:

First you need to install the project dependencies
```
pip install -r requirements.txt
```

Now run the docker-compose file to create your database locally using it:
```
docker-compose up
```

Now, with the bank started locally in docker and the dependencies installed you can start the project using:
```
python main.py
```

I used a system of environment variables through .env, but these variables are secret, so try to find them by creating the .env file in the root of the project with the format:
```
VARIABLE_NAME=VALUE
```

## 🤝 Collaborator

<table>
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/heitor-melegate/" title="My LinkedIn">
        <img src="https://avatars.githubusercontent.com/u/101652747?s=400&u=58c0332024641b1eedb9d92bd28bcd8ad12f693c&v=4" width="100px;" alt="My photo on GitHub"/><br>
        <sub>
          <b>Heitor Melegate</b>
        </sub>
      </a>
    </td>
  </tr>
</table>