ARG IMAGE_VERSION=3.11
FROM public.ecr.aws/docker/library/python:${IMAGE_VERSION}-slim
LABEL maintainer="tatiana.ekeinhor@gmail.com"

ARG BUILD_PATH
ENV API_ENDPOINT_URL="htpp://localhost:8081/api/v1/predict"
WORKDIR ${BUILD_PATH}

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*


COPY info "${BUILD_PATH}/info"
COPY ui "${BUILD_PATH}/ui"
RUN pip install --pre --no-cache-dir -r ${BUILD_PATH}/info/requirements.txt
RUN chown 1000 ${BUILD_PATH}


EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["python", "-m", "streamlit", "run", "ui/1_🏷️_Tag_Generator.py", "--server.port=8501", "--server.address=0.0.0.0"]