
library(caret)

evaluate_model <- function(predictions, actual){

  cm <- confusionMatrix(predictions, actual)

  accuracy <- cm$overall["Accuracy"]

  print(cm)

  return(accuracy)
}
