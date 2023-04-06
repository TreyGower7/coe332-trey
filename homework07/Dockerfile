FROM python:3.8.10

RUN pip install Flask==2.2.2
RUN pip install redis==4.5.1
RUN pip install requests==2.22.0
RUN pip install PyYAML==6.0

COPY gene_apihw07.py /gene_apihw07.py

CMD ["python", "gene_apihw07.py"]
