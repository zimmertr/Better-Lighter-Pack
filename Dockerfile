FROM python
COPY main.py .
COPY trips/ ./trips/
CMD ["python", "main.py"]
