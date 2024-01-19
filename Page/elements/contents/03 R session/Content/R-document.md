# Basic R programing

---

1. **Interactive Environment**:
   - R provides an interactive environment where you can enter commands and immediately see the results. You can use the R console or integrated development environments (IDEs) like RStudio for this purpose.

2. **Data Structures**:
   - R supports various data structures, including vectors, matrices, data frames, lists, and more. These data structures allow you to organize and manipulate data efficiently.

3. **Functions**:
   - Functions are a fundamental part of R. R comes with a vast set of built-in functions, and you can create your own functions as well. Functions in R are defined using the `function()` keyword and can take arguments and return values.

4. **Packages**:
   - R's functionality can be extended through packages. Packages are collections of functions, data sets, and documentation. You can install and load packages using commands like `install.packages()` and `library()`.

5. **Data Analysis and Manipulation**:
   - R provides powerful tools for data analysis and manipulation. Libraries like `dplyr` and `tidyr` make it easy to filter, transform, and reshape data.

6. **Statistical Analysis**:
   - R is renowned for its statistical capabilities. You can perform a wide range of statistical tests, regression analysis, hypothesis testing, and more using built-in functions and packages like `stats`.

7. **Data Visualization**:
   - R offers excellent data visualization capabilities. The `ggplot2` package, in particular, is widely used for creating complex and customized data visualizations.

8. **Scripting and Programming**:
   - While R is often used interactively, you can also write scripts and programs in R. R scripts are plain text files containing a series of R commands. You can execute scripts line by line or all at once.

9. **Data Import and Export**:
   - R can import and export data from various file formats, such as CSV, Excel, JSON, and databases. Functions like `read.csv()` and `write.csv()` are commonly used for this purpose.

10. **Error Handling and Debugging**:
    - R provides tools for error handling and debugging, including the `tryCatch()` function for handling errors and debugging functions like `debug()` and `trace()`.

11. **Vectorized Operations**:
    - R is known for its vectorized operations, which allow you to perform operations on entire vectors or matrices without explicit loops.

12. **Graphics and Plotting**:
    - R has extensive capabilities for creating static and interactive plots and charts. The `base` package provides basic plotting functions, while packages like `ggplot2` offer more advanced options.

13. **Community and Resources**:
    - R has a vibrant community of users and developers, and there are numerous online resources, forums, and documentation available to help you learn and solve problems.

In summary, R is a powerful and versatile language for data analysis and statistical computing. It offers a wide range of tools and libraries, making it a popular choice for data scientists, statisticians, and analysts. To get started with R, you can download it from the official R Project website and explore online tutorials and documentation to build your skills.

---
## Rstudio
### Download and install R and Rstudio
Download R and Rstudio: https://posit.co/download/rstudio-desktop/

Install R and Rstudio

---

## Data type

1. **Numeric (Double)**:
   - Numeric data types represent real numbers, including integers and floating-point numbers.
   - Example: `x <- 42.5`

2. **Integer**:
   - Integers are whole numbers without a decimal point.
   - Example: `y <- 10L` (L is used to indicate it's an integer)

3. **Character (String)**:
   - Character data types represent text or strings.
   - Example: `name <- "Alice"`

4. **Logical (Boolean)**:
   - Logical data types represent binary values, either `TRUE` or `FALSE`.
   - Example: `is_valid <- TRUE`

5. **Factor**:
   - Factors are used to represent categorical data. They can have predefined levels.
   - Example: `gender <- factor(c("Male", "Female", "Male"))`

6. **Date and Time**:
   - R provides various data types for date and time, including `Date`, `POSIXct`, and `POSIXlt`.
   - Example: `birth_date <- as.Date("1990-05-15")`

7. **Complex**:
   - Complex data types represent complex numbers with both real and imaginary parts.
   - Example: `z <- 3 + 2i`

8. **List**:
   - Lists are versatile data structures that can hold elements of different types, including other lists.
   - Example: `my_list <- list(name = "John", age = 25, scores = c(90, 85, 78))`

9. **Vector**:
   - Vectors are one-dimensional arrays that can contain elements of the same data type.
   - Example: `numeric_vector <- c(1, 2, 3, 4, 5)`

10. **Matrix**:
    - Matrices are two-dimensional arrays with rows and columns.
    - Example: `my_matrix <- matrix(1:9, nrow = 3, ncol = 3)`

11. **Data Frame**:
    - Data frames are two-dimensional data structures that resemble tables in a database, and they can hold different data types.
    - Example: `my_df <- data.frame(Name = c("Alice", "Bob"), Age = c(30, 25))`

12. **Array**:
    - Arrays are multi-dimensional data structures that can hold elements of the same data type.
    - Example: `my_array <- array(1:12, dim = c(3, 2, 2))`

13. **Function**:
    - Functions are objects that can be assigned to variables and called like regular functions.
    - Example: `square <- function(x) x^2`

14. **Environment**:
    - Environments are used to store variables and their values.
    - Example: `my_env <- new.env()`
---
## Basic R syntax

1. **Assigning Values**:
   - Assign a value to a variable using `<-` or `=`:
     ```R
     x <- 10
     y = 5
     ```

2. **Basic Arithmetic Operations**:
   - R supports basic arithmetic operations like addition, subtraction, multiplication, and division:
     ```R
     addition_result <- 3 + 2
     subtraction_result <- 7 - 4
     multiplication_result <- 5 * 6
     division_result <- 10 / 2
     ```

3. **Data Types**:
   - R has various data types, including numeric, character, logical, and more. You don't need to explicitly declare types.
     ```R
     num_var <- 42
     char_var <- "Hello, R!"
     logical_var <- TRUE
     ```

4. **Vectors**:
   - Vectors are one-dimensional arrays in R.
     ```R
     numeric_vector <- c(1, 2, 3, 4, 5)
     character_vector <- c("apple", "banana", "cherry")
     ```

5. **Data Frames**:
   - Data frames are two-dimensional data structures that can hold different types of data.
     ```R
     data_frame <- data.frame(Name=c("Alice", "Bob", "Charlie"), Age=c(25, 30, 22))
     ```

6. **Functions**:
   - Define and call functions using `function() {}`:
     ```R
     square <- function(x) {
       return(x^2)
     }
     result <- square(4)
     ```

7. **Conditional Statements**:
   - Use `if`, `else if`, and `else` for conditional logic:
     ```R
     if (x > 5) {
       print("x is greater than 5")
     } else {
       print("x is less than or equal to 5")
     }
     ```

8. **Loops**:
   - Use `for` and `while` loops for iterative tasks:
     ```R
     for (i in 1:5) {
       print(i)
     }

     j <- 1
     while (j <= 5) {
       print(j)
       j <- j + 1
     }
     ```

9. **Packages**:
   - R has a rich ecosystem of packages. You can install and load packages to extend R's functionality:
     ```R
     install.packages("package_name")
     library(package_name)
     ```

10. **Data Import/Export**:
    - Read and write data from/to files like CSV, Excel, or databases using functions like `read.csv()` and `write.csv()`.

---

1. **Data Manipulation**:
   - **dplyr**: The `dplyr` package provides a powerful set of functions for data manipulation tasks like filtering, selecting, grouping, and summarizing data.

   ```R
   library(dplyr)

   # Filter rows
   filtered_data <- data %>%
     filter(column_name > 10)

   # Group and summarize data
   summarized_data <- data %>%
     group_by(group_column) %>%
     summarise(mean_value = mean(value))
   ```

2. **Data Visualization**:
   - **ggplot2**: This package allows you to create sophisticated and customizable data visualizations.

   ```R
   library(ggplot2)

   ggplot(data, aes(x = x_column, y = y_column)) +
     geom_point() +
     geom_line() +
     labs(title = "Scatterplot with Line")
   ```

3. **Statistical Analysis**:
   - R provides numerous packages for statistical analysis, including hypothesis testing, regression analysis, and time series analysis.
   - **lm()**: Fit linear regression models.
   - **t.test()**: Perform t-tests for hypothesis testing.
   - **forecast**: For time series analysis and forecasting.

4. **Functional Programming**:
   - R supports functional programming concepts like anonymous functions (lambdas) and higher-order functions.

   ```R
   square <- function(x) x^2

   # Apply function to each element in a vector
   result <- sapply(1:5, square)
   ```

5. **Object-Oriented Programming (OOP)**:
   - R supports OOP with S3 and S4 classes. You can create your own classes and methods.

   ```R
   setClass("Person", representation(name = "character", age = "numeric"))
   person <- new("Person", name = "Alice", age = 30)
   ```

6. **Parallel and Multithreaded Computing**:
   - R supports parallel computing for tasks that can be split into smaller parts.

   ```R
   library(parallel)

   # Parallelize a loop
   result <- mclapply(1:10, function(x) x^2)
   ```

7. **Error Handling**:
   - Use `tryCatch()` for robust error handling and debugging.

   ```R
   tryCatch({
     # Code that may produce an error
     error_prone_function()
   }, error = function(e) {
     # Handle the error
     cat("An error occurred:", conditionMessage(e))
   })
   ```

8. **Advanced Data Structures**:
   - R supports more complex data structures like lists, matrices, and arrays.

   ```R
   my_list <- list(name = "John", age = 25)
   my_matrix <- matrix(1:9, nrow = 3, ncol = 3)
   ```
---

## Graph visualisation

```R
# Sample data for a bar chart
categories <- c("Category A", "Category B", "Category C", "Category D")
values <- c(25, 40, 15, 30)


# Sample data for a box plot
group1 <- rnorm(100, mean = 0, sd = 1)
group2 <- rnorm(100, mean = 2, sd = 1)
data <- list(Group1 = group1, Group2 = group2)


# Sample data for a line plot
time <- 1:10
values <- c(3, 5, 7, 4, 8, 9, 6, 10, 12, 11)


# Sample data for a scatter plot
x <- c(1, 2, 3, 4, 5)
y <- c(2, 4, 1, 6, 3)


# Sample data for a pie chart
categories <- c("Category A", "Category B", "Category C")
values <- c(30, 40, 15)



# Load the ggplot2 package
library(ggplot2)

# Sample data for all plots
# You can replace this with your own data
set.seed(123)
# Create a data frame with consistent vector lengths
data <- data.frame(
  Category = c("A", "B", "C", "D"),
  Value = c(25, 40, 15, 30),
  Group1 = c(rnorm(100, mean = 0, sd = 1)),
  Group2 = c(rnorm(100, mean = 2, sd = 1)),
  Time = 1:10,
  Values = c(3, 5, 7, 4, 8, 9, 6, 10, 12, 11),
  X = c(1, 2, 3, 4, 5),
  Y = c(2, 4, 1, 6, 3),
  Label = c("Category A", "Category B", "Category C", NA, NA),
  Percentage = c(30, 40, 15, NA, NA)
)

# Replace NA values or adjust vector lengths as needed

# Create a bar chart using ggplot2
bar_plot <- ggplot(data, aes(x = Category, y = Value, fill = Category)) +
  geom_bar(stat = "identity") +
  labs(title = "Bar Chart Example")

# Create a box plot using ggplot2
box_plot <- ggplot(data, aes(x = factor(1), y = Group1)) +
  geom_boxplot() +
  labs(title = "Box Plot Example")

# Create a line plot using ggplot2
line_plot <- ggplot(data, aes(x = Time, y = Values)) +
  geom_line() +
  labs(title = "Line Plot Example")

# Create a scatter plot using ggplot2
scatter_plot <- ggplot(data, aes(x = X, y = Y)) +
  geom_point() +
  labs(title = "Scatter Plot Example")

# Create pie_chart_data using dplyr
# Install and load the dplyr package
# Your code for creating the pie chart
library(dplyr)
pie_chart_data <- data %>%
  group_by(Label) %>%
  summarise(Percentage = sum(Percentage))
pie_chart <- ggplot(pie_chart_data, aes(x = "", y = Percentage, fill = Label)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y") +
  labs(title = "Pie Chart Example") +
  theme_void()


# Display the plots
print(bar_plot)
print(box_plot)
print(line_plot)
print(scatter_plot)
print(pie_chart)
```

---


**Assignment: Basic R Syntax**

**Instructions:**

1. **Variables and Data Types**:

   a. Create three variables: `age`, `name`, and `is_student`. Assign appropriate values to these variables (e.g., your age, your name, and a boolean value indicating whether you are a student).

   b. Display the values of these variables using the `print()` function.

3. **Basic Operations**:

    a. Create two variables, `num1` and `num2`, and assign them numeric values of your choice.

    b. Calculate the sum, difference, product, and quotient of `num1` and `num2`.

    c. Display the results using the `print()` function.

5. **Data Manipulation**:

   a. Create a vector `my_vector` containing the numbers from 1 to 10.

   b. Extract the elements at indices 3, 5, and 8 from `my_vector`.

   c. Calculate the mean and median of `my_vector`.

   d. Display the results using the `print()` function.

7. **Conditional Statements**:

   a. Create a variable `score` and assign it a numeric value between 0 and 100.

   b. Write an if-else statement to check if the `score` is greater than or equal to 60. If it is, print "Pass," otherwise print "Fail."

9. **Loops**:

   a. Create a for loop to print the numbers from 1 to 5.

   b. Create a while loop to print the numbers from 1 to 5.

11. **Functions**:

   a. Write a function called `square` that takes one argument (a number) and returns its square.
   
   b. Use the `square()` function to calculate the square of a number of your choice and print the result.

