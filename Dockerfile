#Python Base Image
FROM python:3.10-slim

#Initialize the Working directory
WORKDIR /app

#Copy Requirements file
COPY ./requirements.txt /app/requirements.txt

#Run the Installation
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#Download VGG16 Weights
RUN python -c "from tensorflow.keras.applications import VGG16; VGG16(weights='imagenet')"

# Copy Remaining files
COPY . /app/

EXPOSE 8000
#Start Command
CMD ["uvicorn", "endpoints:app","--host", "0.0.0.0", "--port", "8000"]