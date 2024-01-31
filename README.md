# Quick Notes

Organize your thoughts

## Description

<!-- An extended description of your project. Here, explain what your project does, its features, and its purpose. This section is particularly important to give users and contributors an overview of what your project is all about. -->

This is a note taking application that helps you save texts (notes) and soon to be images. It's main purpose is to help store your thought process so that you can organize them and become more productive.

## Getting Started

### Dependencies

Ensure you have [python](https://www.python.org/) installed and access to a database provider like [postgres](https://www.postgresql.org/)

- flask
- Flask-SQLAlchemy
- flask-login
- Authlib
- requests
- Gunicorn

See `src/requirements.txt` for full list of dependenciess

### Installing

In order to get started, follow these steps

#### Step 1: Clone the repo

On your terminal run the following command to clone the repository

```sh
git clone https://github.com/kimfom01/quicknotes.git
```

#### Step 2: Go to src directory

Navigate to the `src` directory

```sh
cd src/
```

#### Step 3: Install required packages

```sh
pip install -r requirements.txt
```

#### Step 4: Create .env

The project depends on some config that it expects to be provided from a .env file at the `src` directory.  
Here is the structure of the file

```env
OAUTH2_CLIENT_ID=
OAUTH2_CLIENT_SECRET=
OAUTH2_META_URL=
FLASK_SECRET=
DB_URI=
DEMO_USERNAME=
```

#### Step 5: Run Migrations

```sh
flask db init
flask db migrate
flask db upgrade
```

### Executing program

Within the `src` directory

```sh
python main.py
```

## Hosting

- [Render](https://render.com/)

## Database Provider

- Postgres through [neon.tech](https://neon.tech/)

<!-- ## Help

Any advice for common problems or issues.
command to run if program contains helper info -->

## Authors

Contributors names and contact info

- Kim Fom - [kimfom01@gmail.com](mailto:kimfom01@gmail.com)

<!-- ## Version History

- 0.2
  - Various bug fixes and optimizations
  - See [commit change]() or [release history]()
- 0.1
  - Initial Release -->

<!-- ## License

This project is licensed under the [LICENSE NAME] License - see the LICENSE.md file for details -->

<!-- ## Acknowledgments

Give credit to any resources or individuals that helped in the development of this project.

- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [Markdown Syntax Guide](https://www.markdownguide.org/basic-syntax/)
- [Choose an Open Source License](https://choosealicense.com/) -->
