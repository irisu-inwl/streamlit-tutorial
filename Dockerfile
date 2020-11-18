FROM python:latest

RUN mkdir /opt/streamlit/
WORKDIR /opt/streamlit/

ADD requirements.txt ./
ADD src ./src
RUN pip install -r requirements.txt

CMD streamlit run src/app.py
