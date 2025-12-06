import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(ROOT_DIR, 'data')
MODELS_DIR = os.path.join(ROOT_DIR, 'models')
SRC_DIR = os.path.join(ROOT_DIR, 'src')


TRAIN_DATA_PATH = os.path.join(DATA_DIR, 'train.csv')
STORES_DATA_PATH = os.path.join(DATA_DIR, 'stores.csv')
FEATURES_DATA_PATH = os.path.join(DATA_DIR, 'features.csv')
TEST_DATA_PATH = os.path.join(DATA_DIR, 'test.csv')
SAMPLE_SUBMISSION_PATH = os.path.join(DATA_DIR, 'sampleSubmission.csv')

MODEL_PATH = os.path.join(MODELS_DIR, 'walmart_rf_model_optimized.pkl')