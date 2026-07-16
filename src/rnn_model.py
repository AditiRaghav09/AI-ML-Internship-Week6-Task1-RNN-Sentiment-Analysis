from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dropout, Dense


def build_lstm_model(vocab_size=10000, max_length=200):
    """
    Builds and returns an LSTM model for sentiment analysis.
    """

    model = Sequential([

        # Embedding Layer
        Embedding(
            input_dim=vocab_size,
            output_dim=128,
            input_length=max_length
        ),

        # LSTM Layer
        LSTM(128),

        # Dropout Layer
        Dropout(0.5),

        # Fully Connected Layer
        Dense(64, activation="relu"),

        # Output Layer
        Dense(1, activation="sigmoid")

    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model


if __name__ == "__main__":

    model = build_lstm_model()

    model.summary()
