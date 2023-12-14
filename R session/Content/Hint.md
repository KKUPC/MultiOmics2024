# Hint
## Variables and Data Types
```R
age <- 25
name <- "John"
is_student <- TRUE
```

## Display values of variables
```R
print(age)
print(name)
print(is_student)
```

## Basic Operations
```R
num1 <- 10
num2 <- 5
```

## Calculate and display results
```R
sum_result <- num1 + num2
diff_result <- num1 - num2
prod_result <- num1 * num2
quotient_result <- num1 / num2
```
```R
print(sum_result)
print(diff_result)
print(prod_result)
print(quotient_result)
```

## Data Manipulation
```R
my_vector <- 1:10
```

## Extract elements at specific indices
```R
extracted_elements <- my_vector[c(3, 5, 8)]
```

## Calculate mean and median
```R
mean_result <- mean(my_vector)
median_result <- median(my_vector)
```

## Display results
```R
print(extracted_elements)
print(mean_result)
print(median_result)
```

## Conditional Statements
```R
score <- 75
```
## Check if score is greater than or equal to 60
```R
if (score >= 60) {
  print("Pass")
} else {
  print("Fail")
}
```

## Loops
### For loop
```R
for (i in 1:5) {
  print(i)
}
```
### While loop
```R
counter <- 1
while (counter <= 5) {
  print(counter)
  counter <- counter + 1
}
```

## Functions
### Define square function
```R
square <- function(x) {
  return(x^2)
}
```

### Use square function
```R
result_square <- square(6)
print(result_square)
```
