
library(randomForest)

train_model <- function(train_data){

  model <- randomForest(
    Churn ~ .,
    data=train_data,
    ntree=200,
    importance=TRUE
  )

  saveRDS(model, "models/churn_model.rds")

  return(model)
}
