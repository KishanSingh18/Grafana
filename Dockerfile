# # Base image
# FROM ubuntu:latest

# # Install necessary packages
# RUN apt-get update && apt-get install -y \
#     python3 \
#     python3-pip \
#     wget

# # Install Prometheus client library
# RUN pip3 install prometheus-client

# # Install Grafana and Prometheus (adjust versions as needed)
# # Instructions for installing Grafana and Prometheus may vary depending on your environment and requirements
# # This example uses Grafana 8.0.0 and Prometheus 2.28.1

# # Download and install Grafana
# RUN wget --no-check-certificate https://dl.grafana.com/oss/release/grafana_10.0.1_amd64.deb
# RUN dpkg -i grafana_10.0.1_amd64.deb





# # Expose necessary ports (adjust as per your needs)
# EXPOSE 8080 9090 3000

# # Start Grafana and Prometheus services
# CMD service grafana-server start && /opt/prometheus/prometheus --config.file=/opt/prometheus/prometheus.yml



# Base image with Grafana and Prometheus
# FROM ubuntu:latest
FROM python:3.9
# FROM grafana/grafana:latest


# FROM prom/prometheus:latest

# ADD prometheus.yml /etc/prometheus/prometheus.yml
#Install Python and dependencies
# RUN apt-get update && apt-get install -y python3 python3-pip wget


# Download and install Prometheus
# RUN wget -O /tmp/prometheus.tar.gz https://github.com/prometheus/prometheus/releases/download/v2.37.8/prometheus-2.37.8.linux-amd64.tar.gz
# RUN tar -xzf /tmp/prometheus.tar.gz -C /tmp/
# RUN mv /tmp/prometheus-2.37.8.linux-amd64 /opt/prometheus

# Copy Prometheus configuration file
# COPY prometheus.yml /opt/prometheus/prometheus.yml

ENV SRC_DIR /usr/bin/src/webapp/src

COPY . ${SRC_DIR}/

WORKDIR ${SRC_DIR}

ENV PYTHONUNBUFFERED=1  

RUN pip3 install prometheus-client


# CMD service /opt/prometheus/prometheus --config.file=/opt/prometheus/prometheus.yml

# CMD ["docker", "run","-d","-p","3000:3000","--name","grafana","grafana/grafana:latest"]
