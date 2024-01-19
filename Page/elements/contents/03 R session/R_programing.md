![](./img/R_logo.png)

# **Basic R programing**

## **What is R?**

    R is a programming language and software environment designed for statistical computing and graphics. It is widely used among statisticians, data scientists, and researchers for data analysis, visualization, and statistical modeling. Although R is a popular language used by many programmers, it is especially effective when used for:
    	- Statistical Computing: R provides a wide range of statistical techniques, making it suitable for tasks such as hypothesis testing, regression analysis, and data manipulation.
        - Graphics and Visualization: R excels in creating high-quality graphs and visualizations, allowing users to represent data in various formats like scatter plots, histograms, and more.
        - Data Analysis: R is particularly well-suited for handling and analyzing large datasets. Its extensive set of packages and libraries make it versatile for different types of data-related tasks.
        - Machine learning: R is commonly used for machine learning algorithms due to its rich ecosystem of libraries and packages tailored for data analysis and statistics. Being able to do Machine Learning in many tasks such as Classification, Regression, Clustering, Feature Selection, Image Processing, etc.
    In summary, R is widely used in data analysis, visualization, statistical modeling and Machine learning. With a focus on statistical techniques, high-quality graphics, and a vast collection of packages, R is open source, has a supportive community, and is suitable for handling large datasets. Its syntax is beginner-friendly, and it promotes reproducible research through code documentation. Overall, R is a powerful tool for statisticians, data scientists, and researchers.

## **Data type**
    In R, there are several data types that you can use to represent and manipulate different kinds of information. Here are some of the commonly used data types in R:
        - Numeric (Double): Numeric data types represent real numbers, including integers and floating-point numbers. Example: 34, 35, 100.25, 1500
        - Integer (Integer): Represents whole numbers without decimal points. Example: 10L
        - Character (String): Character data types represent text or strings. Example: "hello world", "data science", "R programming", "John"
        - Logical (Boolean): Logical data types represent binary values, either TRUE or FALSE. Example: TRUE, FALSE
    Note. Use the function to check the Data type of the variable. If you want to delete a variable, use the function.
    Example:
    ```R
    X <- "KKUPC"
    ```
    ```R
    Class(X)
    ```
    Output: 'Character'

    Here is the data type to help more understand the R program:
        - Factor: Factors are used to represent categorical data. They can have predefined levels. It is used for variables that can take on a limited, fixed number of values, such as levels of a factor.
    Example:
    ```R
    gender <- factor(c("Male", "Female"))
    Movie <- factor(c("Forrest_Gump", "Green Book"))
    ```
    
    - List: A collection of objects (which can be of different data types) organized in a specific order.
    Example:
    ```R
    my_list <- list(1, "a", TRUE, 1 + 4i)
    ```   
       - Vector: A one-dimensional array that can hold elements of the same data type.
      Example:
    ```R
    my_vector <- c(1, 2, 3, 4, 5)
    ```
    - Matrix: A two-dimensional array that can hold elements of the same data type.
    Example:
    ```R
    my_matrix <- matrix(c(1, 2, 3, 4, 5, 6), nrow = 2, ncol = 3)
    ```
    - Data frame: A two-dimensional array that can hold elements of different data types.
    Example:
    ```R
    my_data_frame <- data.frame(
      emp_id = c(1, 2, 3),
      emp_name = c("John Doe", "Jane Doe", "Mary Jane"),
      salary = c(21000, 23400, 26800),
      stringsAsFactors = FALSE
    )
    ```




