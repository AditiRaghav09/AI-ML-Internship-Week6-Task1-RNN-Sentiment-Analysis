from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Configuration
VOCAB_SIZE = 10000
MAX_LENGTH = 200


def load_and_preprocess_data():
    """
    Loads and preprocesses the IMDB dataset.

    Returns:
        X_train_padded
        X_test_padded
        y_train
        y_test
    """

    # Load dataset
    (X_train, y_train), (X_test, y_test) = imdb.load_data(
        num_words=VOCAB_SIZE
    )

    # Pad sequences
    X_train_padded = pad_sequences(
        X_train,
        maxlen=MAX_LENGTH,
        padding="post",
        truncating="post"
    )

    X_test_padded = pad_sequences(
        X_test,
        maxlen=MAX_LENGTH,
        padding="post",
        truncating="post"
    )

    return (
        X_train_padded,
        X_test_padded,
        y_train,
        y_test
    )


if __name__ == "__main__":

    X_train, X_test, y_train, y_test = load_and_preprocess_data()

    print("Training Shape:", X_train.shape)
    print("Testing Shape:", X_test.shape)
