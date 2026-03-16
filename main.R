
source("scripts/train_pipeline.R")
source("scripts/predict_pipeline.R")

cat("Starting ML pipeline...\n")

train_pipeline()

cat("Training complete.\n")

results <- predict_pipeline()

print(results)
