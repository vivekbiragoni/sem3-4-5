# Potato Disease Classification

## Setup for Python:

1. Install Python 

2. Install Python packages


3. Install Tensorflow Serving 



## Training the Model

1. Download the data from [kaggle](https://www.kaggle.com/arjuntejaswi/plant-village).
2. Only keep folders related to Potatoes.
3. Run Jupyter Notebook.
4. Open `training/potato-disease-training.ipynb` in Jupyter Notebook.
5. Run all the Cells one by one.
6. Copy the model generated and save it with the version number in the `models` folder.

## Running the API

### Using FastAPI

1. Get inside `api` folder

cd api

2. Run the FastAPI Server using uvicorn

uvicorn main:app --reload --host 0.0.0.0

3. API is now running at `0.0.0.0:8000`

### Using FastAPI & TF Serve

1. Get inside `api` folder

cd api


2. set the configurations as in `models.config` and update the paths in file.
3. Run the TF Serve

```bash
docker run -t --rm -p 8501:8501 -v C:/Code/potato-disease-classification:/potato-disease-classification tensorflow/serving --rest_api_port=8501 --model_config_file=/potato-disease-classification/models.config
```

4. Run the FastAPI Server using uvicorn
   For this you can directly run it from your main.py or main-tf-serving.py using pycharm run option (as shown in the video tutorial)
   OR you can run it from command prompt as shown below,

```bash
uvicorn main-tf-serving:app --reload --host 0.0.0.0
```

