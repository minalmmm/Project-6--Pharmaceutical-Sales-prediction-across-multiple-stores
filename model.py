from tensorflow.keras.models import load_model

def load_my_model():
    """Load a pre-trained Keras model from the specified path."""
    model_path = r"C:\data science material\project_6\model\model.h5"  # Use raw string to avoid escape issues
    model = load_model(model_path)
    return model

# Example usage
if __name__ == "__main__":
    model = load_my_model()
    print("Model loaded successfully!")
