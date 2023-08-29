# Diabetes-T2-Classification
## Summary
[Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) provide a type 2 Diabetes dataset in the form of three (3) Behavioral Risk Factor Surveillance System (BRFSS) telephone surveys which are run annually by the Centre for Disease Control (CDC) in the USA. The surveys have a total of 400,000 respondents. 

In this repository, I answer these four (4) questions:
1. Can survey questions from the BRFSS provide accurate predictions of whether an individual has diabetes?
2. What risk factors are most predictive of diabetes risk?
3. Can we use a subset of the risk factors to accurately predict whether an individual has diabetes?
4. Can we create a short form of questions from the BRFSS using feature selection to accurately predict if someone might have diabetes or is at high risk of diabetes?

## Notable Methods/Considerations
- The point biseral test.
- Pearson's R test.
- Cramers V test.
- QQ plot and Shapiro-Wilk test for normality.
- Z Score vs Isolation forrest for outlier detection.
- SelectKbest with mutual information.
- Hyperparameter tuning with self-made gridsearchcv like function.
- Decision tree and Random forest algorithms.
- SHAP (SHapley Additive exPlanation) to explain the contribution of each feature to outcomes. 
