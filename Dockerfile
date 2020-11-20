FROM python:latest

RUN mkdir /opt/streamlit/
WORKDIR /opt/streamlit/

ADD requirements.txt ./
ADD src ./src
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --use-feature=2020-resolver
RUN python src/download_model.py

CMD streamlit run src/app.py
