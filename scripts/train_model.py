import mlflow
import mlflow.tensorflow
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('C:\data science material\project_6\Notebook\model.h5')  

# Log the model in MLflow
with mlflow.start_run():
    mlflow.tensorflow.log_model(tf_model=model, artifact_path="model", registered_model_name="RossmannSalesLSTM")
    print("Model logged to MLflow.")
