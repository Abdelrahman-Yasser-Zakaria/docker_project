# OS
FROM ubuntu:latest

# install python3
RUN apt-get update && apt-get install -y python3 python3-venv

# create virtual env
RUN python3 -m venv /opt/venv

# activate the env
RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install pandas numpy seaborn matplotlib scikit-learn scipy

# set the venv as the default Python environment
ENV PATH="/opt/venv/bin:$PATH"

# create directory
RUN mkdir -p /home/doc-bd-a1/

# copy dataset to container
COPY train.csv /home/doc-bd-a1/

# set working directory
WORKDIR /home/doc-bd-a1/

# start bash shell
CMD ["/bin/bash"]