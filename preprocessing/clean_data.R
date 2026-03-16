
library(dplyr)

clean_data <- function(df){

  df <- df %>%
    mutate_if(is.character, as.factor)

  df <- df %>%
    mutate_if(is.numeric, ~replace(., is.na(.), mean(., na.rm = TRUE)))

  df <- df %>%
    filter(!is.na(Churn))

  return(df)
}
