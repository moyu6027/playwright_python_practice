FROM ubuntu:bionic

# Install Python
RUN apt-get update && apt-get install -y python3.7 && apt-get install -y curl
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-distutils
RUN python3.7 get-pip.py
RUN python3.7 -m pip install -U setuptools

# Install Allure.
# See https://github.com/allure-framework/allure-debian/issues/9
RUN apt-get update && apt-get install -y wget default-jdk && cd /opt && \
    (wget -c https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/allure-2.7.0.tgz -O - | tar -xz && chmod +x allure-2.7.0/bin/allure)
ENV PATH="${PATH}:/opt/allure-2.7.0/bin"
RUN allure --version

# 2. Install WebKit dependencies
RUN apt-get install -y libwoff1 \
                       libopus0 \
                       libwebp6 \
                       libwebpdemux2 \
                       libenchant1c2a \
                       libgudev-1.0-0 \
                       libsecret-1-0 \
                       libhyphen0 \
                       libgdk-pixbuf2.0-0 \
                       libegl1 \
                       libnotify4 \
                       libxslt1.1 \
                       libevent-2.1-6 \
                       libgles2 \
                       libvpx5

# 3. Install Chromium dependencies
RUN apt-get install -y libnss3 \
                       libxss1 \
                       libasound2

ADD requirements.txt /

RUN pip install --upgrade pip && \
    pip install virtualenv && \
    virtualenv --python=/usr/bin/python3 /opt/venv && \
    . /opt/venv/bin/activate && \
    python3.7 -m pip install -r requirements.txt --quiet && \
    python3.7 -m playwright install

WORKDIR /app