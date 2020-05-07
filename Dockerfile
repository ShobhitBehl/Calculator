FROM python:3.5
MAINTAINER Shobhit
WORKDIR /calculator
ADD . /calculator
EXPOSE 5000
CMD ["python","calc.py"]