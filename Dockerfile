FROM python
COPY main.py .
COPY trips/ ./trips/
RUN pip install tabulate
CMD ["python", "main.py"]
