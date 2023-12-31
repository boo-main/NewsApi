FROM python:3.11

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt clean && \
    rm -rf /var/cache/apt/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

COPY requirements.txt/ /tmp/requirements.txt

RUN pip install -U pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /src
ENV PATH "$PATH:/src/scripts"

RUN useradd -m -d /src -s /bin/bash app \
   && chown -R app:app /src/* && chmod +x /src/scripts/*

WORKDIR /src
USER app

#CMD ["./scripts/start-dev.sh"]
#CMD ["uvicorn main:app --reload"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

 # useradd: warning: the home directory /src already exists.
 # useradd: Not copying any file from skel directory into it.