# Using python 3.7 full image as the base image
FROM python:3.7.7-slim
# Defining working directory and copy the requirements file. We will run the commands inside this new directory
WORKDIR /usr/src/myapp
# Copy requirements.txt  to the working directory
COPY requirements.txt .
# Install required python packages
RUN pip install --no-cache-dir -r requirements.txt
# Copy all files in training-db local host directory to /usr/src/myapp in Docker container
COPY . .
# Expose the port that our app runs in
EXPOSE 5000
# Enviroment Variables
ENV PROJECT_ID=assignment1-328818
ENV MODEL_REPO=model_repo_assignment_1
ENV HISTORY_REPO=model_repo_assignment_1
ENV PREPROCESSDB_API=http://preprocess-db:5000/preprocessing/train_db
# Run our App
CMD ["python3","app.py"]