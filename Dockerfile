FROM python
COPY . /app
WORKDIR /app
RUN pip install flask
EXPOSE 8080
CMD ["python", "untitled2.py"]
