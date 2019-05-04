FROM ubuntu
LABEL maintainer="blackd0t@protonmail.com"

RUN apt-get update -y --fix-missing
RUN apt-get install -y python3.6 python3-pip python-pip python-dev build-essential
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 -c "import nltk;nltk.download('stopwords');nltk.download('punkt');nltk.download('averaged_perceptron_tagger')"

# CMD ["python", "api.py"]


# ENTRYPOINT ["python3"]
# CMD ["api.py"]