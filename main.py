def main():
    import train_pipeline
    import predict_pipeline

    print("Starting ML pipeline...")

    train_pipeline.train_pipeline()

    print("Training complete.")

    results = predict_pipeline.predict_pipeline()

    print(results)

if __name__ == "__main__":
    main()