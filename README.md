# is-it-tuesday

[![Docker](https://github.com/hasithsen/is-it-tuesday/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/hasithsen/is-it-tuesday/actions/workflows/docker-publish.yml)

### About

This flask app was created partly for fun, partly to be used in a test CI/CD pipeline.

Inspired by https://shanetully.com/2024/07/hey-google-what-happened-to-all-the-fun/

### Local setup

#### Without Docker
```sh
# Create a Python virtual environment
python3 -m venv .pyenv

# Activte the virtaul environment
. .pyenv/bin/activate

# Install required Python packages
pip install -r requirements.txt

# Run Flask app
flask --app tuesday run
```

#### With Docker
```sh
docker build -t flask-tuesday-app .
docker run -d -p 5000:5000 flask-tuesday-app
```

Access application on ```http://localhost:5000```.

Have a good day!
