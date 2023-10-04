#Ubuntu
FROM python:latest

ADD recommend.py .
#RUN system update
#Install python3 and pip3

RUN apt-get update && apt-get install -y python3-pip

#Install libraries
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install scikit-learn
RUN pip3 install seaborn
RUN pip3 install matplotlib

CMD ["python", "./recommend.py"]