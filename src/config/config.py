import torch


class Config:
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    
    STOPWORDS_FILE_PATH = "data/raw_data/stopwords.txt"
    OUTPUT_DIR = "data/preprocessed_data/"
    NYT_PATH = "data/raw_data/nyt.txt"