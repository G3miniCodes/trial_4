
predict_model <- function(model, test_data){

  predictions <- predict(model, test_data)

  return(predictions)
}
