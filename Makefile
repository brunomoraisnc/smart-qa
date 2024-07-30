include .env

create-env:
	conda create -n "${PROJECT_NAME}" python=${PYTHON_VERSION} -y

activate-env:
	conda activate ${PROJECT_NAME}