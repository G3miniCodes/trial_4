
source("utils/helpers.R")
source("utils/logger.R")

source("preprocessing/clean_data.R")
source("preprocessing/feature_engineering.R")
source("preprocessing/split_data.R")

source("models/train_model.R")

train_pipeline <- function(){

  log_message("Loading data")

  df <- load_dataset("data/raw/telecom_churn.csv")

  log_message("Cleaning data")

  df <- clean_data(df)

  df <- feature_engineering(df)

  split <- split_data(df)

  train <- split$train

  log_message("Training model")

  model <- train_model(train)

  return(model)

}
