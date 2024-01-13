readme file

Files submitted are classified into :
-'recommendation_system(G12).ipynb' which is the recommendation system script where we preprocessed the data and exported CSV file which is fixed to be used in recommendation which is the "movies_df(G12).csv"

-Clust_class(G12).ipynb which is the script that contains the classification and clustering models

-finally we have the "flask(G12).py"  which is the script that contain the flask code and must be run 24/7 on a dedicated terminal to allow you to connect with the chatbot with the help of "ngrok" that is the simplified API that allows the connectivity , in addition to the recommendation functions that is necessary for the task.

-"movies_df.csv" that is the data preprocessed by the recommendation script and given to the flask script to use it in recommendation 

Steps for using the chatbot :
1-You must have a dialogflow access
2-Run the ngrok and type "ngrok.exe http 5000"
3- take the ip that will show in the ngrok and type it in the fulfillment section in the dialogflow and write "/webhook" at the end which reflect to our webhook inside the flask script
4-run the flask script 
5-open dialogflow and enjoy it
