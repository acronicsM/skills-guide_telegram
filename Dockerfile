FROM python:3.11
WORKDIR /skills-guide_telegram

COPY ./core /skills-guide_telegram/core
COPY ./requirements.txt /skills-guide_telegram
COPY ./settings.py /skills-guide_telegram
COPY ./README.md /skills-guide_telegram
COPY ./main.py /skills-guide_telegram


RUN python -m pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev

RUN python -m pip install -r requirements.txt

EXPOSE 6000

CMD ["python", "main.py"]
