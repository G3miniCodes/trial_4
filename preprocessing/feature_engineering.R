
library(dplyr)

feature_engineering <- function(df){

  df <- df %>%
    mutate(
      tenure_group = case_when(
        tenure < 12 ~ "new",
        tenure < 24 ~ "mid",
        TRUE ~ "loyal"
      )
    )

  df$tenure_group <- as.factor(df$tenure_group)

  return(df)
}
