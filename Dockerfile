FROM python:3.13-slim

RUN apt-get update && \
    apt-get install -y \
    wget \
    curl \
    unzip \
    libnss3 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libglib2.0-0 \
    libgdk-pixbuf2.0-0 \
    libappindicator3-1 \
    libsecret-1-0 \
    && apt-get clean

RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome.deb && \
    dpkg -i google-chrome.deb && \
    apt-get install -f -y

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./tests /app/tests

CMD ["pytest"]
