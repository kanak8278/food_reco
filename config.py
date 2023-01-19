#Training Params
NUM_EPOCHS = 1
BATCH_SIZE = 6
NUM_CATEGORIES = 29
IMG_SIZE = (256, 256, 3) 
RANDOM_SEED = 8
TRAIN_TEST_RATIO = 0.8


DATASET_FOLDER = "/content/drive/MyDrive/similar-foods"
SAVING_CHECKPOINT = f"/content/drive/MyDrive/food_model_checkpoints/resnet_50_bs{BATCH_SIZE}_epochs{NUM_EPOCHS}.pt"
TRAIN_CSV = "/content/drive/MyDrive/train_food.csv"
VAL_CSV = "/content/drive/MyDrive/val_food.csv"