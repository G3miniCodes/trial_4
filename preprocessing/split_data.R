
library(caret)

split_data <- function(df){

  set.seed(42)

  train_index <- createDataPartition(df$Churn, p = 0.8, list = FALSE)

  train <- df[train_index, ]
  test <- df[-train_index, ]

  return(list(train=train, test=test))
}
