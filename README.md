# JPX

![image](https://user-images.githubusercontent.com/100894816/173004184-5bcfbd26-b92d-44f9-9257-ed6fb318e73b.png)

JPX markets are closed on Saturdays, Sundays, national holidays, and on the dates indicated below.


In this competition, we have to predict the target and then make the folmula about sharp ratio.
Target is a stock price and Target is changed with PER. Finally, with sharp ratio we submit the file as they want.

Metric Definition is written here:
https://www.kaggle.com/code/smeitoma/jpx-competition-metric-definition?scriptVersionId=92117258&cellId=1

* JPX Competition Metric
 - In this competition, the following conditions set will be used to compete for scores.

- The model will use the closing price ( C(k,t) ) until that business day ( t ) and other data every business day as input data for a stock ( k ), and predict rate of change ( r(k,t) ) of closing price of the top 200 stocks and bottom 200 stocks on the following business day ( C(k,t+1) ) to next following business day ( C(k,t+2) )

* r(k,t)=C(k,t+2)−C(k,t+1)C(k,t+1)
 
- Within top 200 stock predicted ( upi(i=1,2,…,200) ), multiply by their respective rate of change with linear weights of 2-1 for rank 1-200 and denote their sum as  Sup .

* Sup=∑200i=1(r(upi,t)∗linearfunction(2,1)i))Average(linearfunction(2,1))
 
Within bottom 200 stocks predicted ( downi(i=1,2,…,200) ), multiply by their respective rate of change with linear weights of 2-1 for bottom rank 1-200 and denote their sum as  Sdown .

* Sdown=∑200i=1(r(downi,t)∗linearfunction(2,1)i)Average(linearfunction(2,1))
 
- The result of subtracting  Sdown  from  Sup  is  Rday  and is called "daily spread return".

* Rday=Sup−Sdown
 
- The daily spread return is calculated every business day during the public/private period and obtained as a time series for that period. The mean/standard deviation of the time series of daily spread returns is used as the score. Score calculation formula (x is the business day of public/private period)

* Score=Average(Rday1−dayx)STD(Rday1−dayx)
 
- The Kagger with the largest score for the private period wins.

- The following rules are used to determine which stocks are available for investment.

* The top 2,000 common stocks by market capitalization that have been listed for at least one year as of 2021-12-31 are eligible for investment.

- If a stock is designated as Securities Under Supervision or Securities to Be Delisted during the private period, it will be excluded from investment after the date of designation.

- When calculating the score, the adjusted stock price is used.


* EDA
- Target value composition
- ![image](https://user-images.githubusercontent.com/100894816/177025325-a720bb14-589a-48c9-85c2-2b0ba4744e6a.png)
- ![image](https://user-images.githubusercontent.com/100894816/177025355-50eaa679-29b7-4981-a135-06b08fa5cfa1.png)
- ![image](https://user-images.githubusercontent.com/100894816/177025366-51e11a27-ed81-49fb-bec1-4f7813363e27.png)
- ![image](https://user-images.githubusercontent.com/100894816/177025383-ae25ffeb-49bc-415c-a057-4501c594ac97.png)
- ![image](https://user-images.githubusercontent.com/100894816/177025391-2f0e4ab4-9930-4c47-aa13-63d51668b2af.png)
- ![image](https://user-images.githubusercontent.com/100894816/177025394-cb776b4f-3a08-434e-ba30-af18601a0691.png)
- ![image](https://user-images.githubusercontent.com/100894816/177025398-a28be0f5-8791-45fd-851b-78f174501f22.png)
- ![image](https://user-images.githubusercontent.com/100894816/177025803-ba782444-9c80-4ed3-a217-9a5cd6c43b7a.png)
- ![image](https://user-images.githubusercontent.com/100894816/177025811-72fd86b1-8e07-424b-bcce-3b8297d20a29.png)
- ![image](https://user-images.githubusercontent.com/100894816/177025817-323497af-adef-46dc-9595-7ab8a71c7b56.png)
- ![image](https://user-images.githubusercontent.com/100894816/177025821-20a46a90-bae4-467e-a4b3-83b12c1f078f.png)
- ![image](https://user-images.githubusercontent.com/100894816/177025823-3a69ce71-26da-442e-a046-415e029fb8ac.png)


<<< _predictor_model >>>
score -> 4.320905037331315
mean  -> 13.720639712154265
std   -> 3.1754087612692437


<<< _predictor_model_with_adjuster >>>
score -> 5.714972425326807
mean  -> 7.820889127307698
std   -> 1.368491139633183

<<< _predictor_target >>>
score -> 4.854775476521634
mean  -> 15.221062190989013
std   -> 3.135276237716899

<<< _predictor_target_with_adjuster >>>
score -> 7.28977612836715
mean  -> 10.915641043635977
std   -> 1.4973904344139293

