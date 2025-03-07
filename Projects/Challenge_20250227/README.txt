The task is to predict labels for users, store the predictions and serve 
them out via a REST API. You should use at most 4 hours to complete the 
assignment. The team mostly uses Python based tooling, so this is where 
we can give best feedback, but you are free to use any programming 
languages and tools you want.
 

DATA

x_train.csv Independent variables as CSV, the last column being the user id.
y_train.csv Labels for the users in x_train.csv. There are 6 possible labels,
            expressed as integers in the data.
x_test.csv  Use your model to predict labels for these users and to serve 
	    them out via a REST API.

All data is synthetic and generated for this occasion only, so you need not
worry about privacy or security.


DELIVERABLES AND REQUIREMENTS

Part 1) Predictions

Predict a label for each user in "x_test.csv" and store the predictions as a
separate csv called "predictions.csv". It should contain each user id along 
with a predicted label. Please also include the files/notebooks/scripts that
you used to create your predictions.


Part 2) REST API

Build a REST API which serves the prediction for a single user given her or 
his user id. When queried from an end-point with a user id, e.g. 

<api-url>/predictions/e554b320-0ab6-489e-bc40-eb132946b85a

the API should respond with a JSON like 

}
  "class": 2
}


Include brief instructions for running your program. It is sufficient to be able to run 
the API locally.

Part 3) Questions

In an addition to these, also briefly(!) answer the following questions:

1) What were the most important technical decisions and on what grounds did
   you make them?
2) How would you communicate your model's prediction quality to a business stakeholder?
   Assume limited knowledge of statistics or machine learning on their part.
3) If time and/or interest had permitted, how would you have improved on your
   solution?


RETURN

Please note:
- Do not worry excessively about prediction quality. If it's good, that's nice,
  but if not, try to finish the rest anyway. 
- Also don't worry if you can't finish all parts or if you get stuck somewhere, 
  just try to get the rest working and send it. 
- As mentioned, please return all your files, including analysis notebooks etc.
  so that we understand your thought process better. Again no need to clean up,
  we understand time is very limited 

Return your solution by email to marek.matusiak@sanoma.com, preferably 
in a single compressed file.
