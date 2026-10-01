import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Flatten, Dense


def main():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    model = Sequential([
        Input(shape=(28, 28)),
        Flatten(),
        Dense(128, activation="relu"),
        Dense(10, activation="softmax"),
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    model.fit(x_train, y_train, epochs=3, batch_size=128, validation_split=0.1)
    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)

    print(f"Test accuracy: {accuracy:.4f}")
    predictions = model.predict(x_test[:10], verbose=0).argmax(axis=1)
    print("Predictions for first 10 test images:", predictions.tolist())


if __name__ == "__main__":
    main()
