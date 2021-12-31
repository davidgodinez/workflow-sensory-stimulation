FROM datajoint/djlab:py3.9-debian

RUN mkdir main/

WORKDIR /main

RUN git clone https://github.com/datajoint/workflow-sensory-stimulation.git .

RUN pip install .

COPY ./dj_local_conf.json /main/   