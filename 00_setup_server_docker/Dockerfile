FROM photon:2.0

# Adding startup.sh to the image
#RUN if [ ! -d "/opt" ]; then mkdir /opt; fi \
# && if [ ! -d "/opt/startup" ]; then mkdir /opt/startup; fi \
# && if [ ! -d "/opt/startup/bin" ]; then mkdir /opt/startup/bin; fi
COPY startup.sh /opt/startup/bin/startup.sh
RUN chmod 770 /opt/startup/bin/startup.sh

# Installing necessary packages
RUN tdnf update -y \
 && tdnf install -y \
 linux-api-headers \
 gcc \
 glibc-devel \
 binutils \
 python3-devel \
 python3 \
 python3-pip \
 gzip \
 tar \
 glibc-i18n \
 && locale-gen.sh \
 && ln -s /usr/bin/pip3.6 /usr/bin/pip \
 && pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir setuptools \
 && pip install --no-cache-dir mlflow==1.2.0

ENV LC_ALL "en_US.utf8"
ENV LANG "en_US.utf8"

EXPOSE 5000

CMD ["/bin/bash", "-c", "/opt/startup/bin/startup.sh"]
