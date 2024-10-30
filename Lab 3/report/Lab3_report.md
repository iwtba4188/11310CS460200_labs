## 11310CS460200 Intro 2 ML Lab 3
|Name|Date|
|:-:|:-:|
|110020007 施淙綸|2024/10/18|

### State the possible reason why the accuracy or F1-score change between Perceptron and LDA?
- The Perceptron method may not converge if the data is not linearly separable. In this case, the Perceptron cannot reach a decent model, leading to lower accuracy and F1-score.
- On the other hand, LDA tries to find the best separation between classes. Thus, LDA still works when data isn't linearly separable.
- Also, data distribution affects Perceptron and LDA differently, as does their sensitivity to outliers. This results in different behavior of models trained by these methods.

### Does MAP help? Why?
- In general, MAP helps LDA achieve better performance because MAP considers prior knowledge (probabilities). If the data is imbalanced, MAP can make adjustments using this prior information.

### Difficulty I encountered
- Calculation of $S_W$: The summation of $S_W$ wasn't intuitive for me to translate into code.
    - How I solved it: I wrote the formula on paper and tried to write the matrix version of the summation.
- Normalize the vector: It took a while to figure out how to normalize the vector using `np.linalg.norm`.
    - How I solved it: It just took some time to search for the normalization method using norm.

### My reflections
- This lab gives a clearer explanation and description than before. The progress of this lab is very smooth. Nice!
