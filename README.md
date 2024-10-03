# Project-04-Group-TBD
This is the repository for Project 4


This project looks at a dataset posted by the National Highway Traffic Safety Administration (NHTSA) on crashes involving vehicles with automation. These functions are still in development with many unknown outcomes of real world impacts on traffic and safety. We aim to answer some basic questions including:


1. Will certain weather conditions cause accidents resulting in whether someone gets injured or not? Is this predictable?
2. Will different vehicle conditions impact the result of an accident?
3. When do these accidents happen the most?
4. What are other environmental conditions that impact the outcome of an accident?


The machine learning model was not great due to the heavy imbalance to the outcome of "No Injuries." The best performing model ended up being the XGBoost classifier which had an 83% weighted average F1 Score.


The data shows certain manufacturers have more occurences of crashes than others. There is also a huge number of crashes involved with automated vehicles manufactured in 2021. This could be when a large number of vehicles were readily available to purchase in this year making that year look worse due to the increased number available. Wearing a seatbelt did not seem to have much of an impact on injury outcome because a majority of the crashes involved people wearing seatbelts. Interestingly enough, the no seatbelt category had no major or serious injury outcomes.


August is notorious for having the most crashes compared to other months and is no exception in this dataset. There is no surprise people around 1 pm are more likely to experience a car crash. People are rushing back to work after lunch and may make riskier maneuvers to quickly return. What is interesting is the uptick of crashes in the middle of the night. Is there an issue with automation in lower light settings? Are people using automation as a crutch to drive when they are not in the best condition to do so?


Environmentally, clear conditions are when these crashes occur the most. There could be a distrust in using these systems in inclement weather or the fact most of the crashes are occurring in California which is known for the mild weather. Most of the crashes are occuring while the vehicle is stopped or going straight, leaving out any risky maneuvers being an indication of the automation system failures. The locations are also at intersections and streets with the largest occurrence rates. Overall, the huge majority of the crashes involve no injuries and only a few serious injuries within the dataset.


The data provided is not good at indicating what other vehicle was involved and where the fault lies. These would be critical to know if automation has more of a future due to the safety and convenience they provide or if there is more development required prior to employing these systems in a more mainstream sense.
