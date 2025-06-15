FROM python:3.11.2-slim

# Set the working directory in the container
WORKDIR /app

# Instal pip requirements
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the container of the local src directory to the working directory
COPY . .

# Specify the port nunmber the container should expose
EXPOSE 80

# Run the application
# el que vimos en clase
CMD ["uvicorn", "fastapiapp.main:app", "--host", "0.0.0.0", "--port", "80"]   
# Para local
#CMD ["fastapi", "run", "main.py", "--port", "80"]
