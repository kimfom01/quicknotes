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
python app.py
```

### Building and running with docker

When you're ready, start your application by running:
`docker compose up --build`.

Your application will be available at [http://localhost:5000](http://localhost:5000)

### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References

- [Docker's Python guide](https://docs.docker.com/language/python/)

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
