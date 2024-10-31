import tensorflow as tf
from keras.models import load_model
import mlflow
import mlflow.tensorflow
from mlflow.models import ModelSignature
from mlflow.types import Schema
from mlflow.types.schema import TensorSpec
import numpy as np  # Import numpy

# Load the model
model_path = r"C:\data science material\project_6\model\model.h5"
model = load_model(model_path)

# Create the input schema using TensorSpec
input_schema = Schema([
    TensorSpec(shape=(None, 10, 1), type=mlflow.types.DataType.FLOAT)  # Use DataType.FLOAT for the type
])

# Create a ModelSignature
signature = ModelSignature(inputs=input_schema)

# Start MLflow run
with mlflow.start_run():
    # Log the model with signature
    mlflow.tensorflow.log_model(model=model, artifact_path="model", registered_model_name="RossmannSalesLSTM", signature=signature)
    print("Model logged to MLflow.")
