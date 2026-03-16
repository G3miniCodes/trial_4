
source("models/predict_model.R")
source("evaluation/evaluate_model.R")
source("preprocessing/clean_data.R")

predict_pipeline <- function(){

  model <- readRDS("models/churn_model.rds")

  df <- read.csv("data/raw/telecom_churn.csv")

  df <- clean_data(df)

  predictions <- predict_model(model, df)

  accuracy <- evaluate_model(predictions, df$Churn)

  return(accuracy)

}
