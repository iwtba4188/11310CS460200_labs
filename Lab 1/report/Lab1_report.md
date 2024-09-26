## 11310CS460200 Intro 2 ML Lab 1
|Name|Date|
|:-:|:-:|
|110020007 施淙綸|2024/09/26|

### Regression equation in basic part
$y=w_0+w_1 \cdot weight+w_2 \cdot weight^2$, where $w_0=0.02648253$, $w_1=0.59029589$, and $w_2=0.00108035$.

### The variables and the regression equation in the advanced part
In the advanced part, I used all 7 features to fit a fifth-degree polynomial regression with an additional logarithmic term for each feature. The equation, excluding coefficients, is: $\hat{y} = 1 + \sum_{i=0}^6 \ln(1+x_i) + \sum_{p=1}^{5} \sum_{i=0}^{6} x_i^p$, where $w = [w_0\ w_1 \cdots w_{49}]$ are the coefficients for each term, assigned in order. The features $x_0$ to $x_6$ represent age, gender, height, weight, body fat, diastolic, and systolic pressure, respectively.

※ For the explicit coefficients, refer to the final output in the last code block.

### Difficulty I encountered
- **Large data values with higher degrees**: Fitting raw data resulted in large values for higher powers like $height^5$, requiring more computational resources and leads to large effect of the higher-degree terms. Also a very low learning rate was needed.
- **Fixed learning rate causing oscillation**: A large learning rate led to oscillation near the global minimum instead of smooth convergence.

### How I solved difficulties and my reflections
- **Large data values**: I applied normalization to map data points closer to zero, reducing the term magnitudes and correcting dataset imbalance.
- **Not fixed learning rate**: I switched to the Adam optimizer, which uses a decreasing learning rate, improving MAEP scores.
- **Reflection**: Fine-tuning hyperparameters was challenging, and it was hard to pinpoint whether issues were due to hyperparameters or other code parts. Still, implementing traditional ML algorithms was a valuable experience, even if performance wasn't ideal.
