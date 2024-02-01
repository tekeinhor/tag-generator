ARG IMAGE_VERSION=3.11-slim
FROM public.ecr.aws/docker/library/python:${IMAGE_VERSION} as builder
LABEL maintainer="tatiana.ekeinhor@gmail.com"

ARG BUILD_PATH
ARG POETRY_VERSION=1.6.1
WORKDIR ${BUILD_PATH}
ARG NLTK_DATA_DIR_ARG="${BUILD_PATH}/nltk_data"
ENV NLTK_DATA_DIR=$NLTK_DATA_DIR_ARG
ENV NLTK_DATA=$NLTK_DATA_DIR

COPY . .

RUN pip install --pre --no-cache-dir -r "${BUILD_PATH}/info/requirements.txt"
RUN chown 1000 ${BUILD_PATH}

USER 1000

CMD ["python", "-m", "api.main"]