FROM python:latest

RUN mkdir /opt/streamlit/
WORKDIR /opt/streamlit/
ADD requirements.txt ./
ADD src ./src
ADD data ./data
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --use-feature=2020-resolver
RUN python src/download_model.py
RUN curl -s -o data/data.json https://raw.githubusercontent.com/tokyo-metropolitan-gov/covid19/master/data/data.json 

CMD streamlit run src/app.py
