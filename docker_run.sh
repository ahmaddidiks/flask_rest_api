
DOCKER_IMAGE="rest-api-flask"
DIR_PATH="udemy/flask_rest_api_udemy"

cd $HOME/$DIR_PATH
source .venv/bin/activate
# docker run -dp 5000:5000 -w /app -v "$(pwd):/app" $DOCKER_IMAGE
flask run
