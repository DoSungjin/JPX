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
- ![image](https://user-images.githubusercontent.com/100894816/177026494-45513b09-709e-4b2e-aab9-433ceb353a61.png)
![image](https://user-images.githubusercontent.com/100894816/177026500-d7de21f3-c6b2-459c-b285-06aa27066cdf.png)
![image](https://user-images.githubusercontent.com/100894816/177026505-95000ad1-ff6a-4f43-b25e-5c2b6a815515.png)
![image](https://user-images.githubusercontent.com/100894816/177026506-59d7ba68-a2d6-4150-a99b-c2e9c62ba657.png)
![image](https://user-images.githubusercontent.com/100894816/177026509-3a301c61-7291-438e-bd61-f3ab5a7b6482.png)

- ![image](https://user-images.githubusercontent.com/100894816/177026513-1a0ce619-120c-4875-97a4-0a5c7babac3c.png)
- ![image](https://user-images.githubusercontent.com/100894816/177026516-ccfa8687-35d8-4f79-abc8-3c4e8f284c04.png)

- ![image](https://user-images.githubusercontent.com/100894816/177026521-b0430131-edc2-40a9-8ed4-6a2ce18df105.png)
![image](https://user-images.githubusercontent.com/100894816/177026524-2ce8f6c7-75f0-4f45-813d-61c1946e4020.png)
![image](https://user-images.githubusercontent.com/100894816/177026526-42211fc6-3dc9-4f14-a491-f6e4fb79a620.png)
![image](https://user-images.githubusercontent.com/100894816/177026530-a29b21f2-5338-41e2-b8c7-629514bd4a7e.png)
![image](https://user-images.githubusercontent.com/100894816/177026534-1c963d1d-1573-4e8a-b2c2-a61fa610f206.png)

- ![image](https://user-images.githubusercontent.com/100894816/177026535-c9a7d6ae-d0e4-40d1-8a7a-ef7dce305d61.png)
- ![image](https://user-images.githubusercontent.com/100894816/177026538-4736f83b-82f8-4b99-9af0-522d209a1233.png)
 
- ![image](https://user-images.githubusercontent.com/100894816/177026546-790a64b0-5d4e-4a8c-9003-de1aded2cc35.png)
![image](https://user-images.githubusercontent.com/100894816/177026549-cf68d732-6260-42ac-8716-a9694cab8ea1.png)
![image](https://user-images.githubusercontent.com/100894816/177026552-3b34f550-8f46-4300-ba30-d3b7307e8c20.png)
![image](https://user-images.githubusercontent.com/100894816/177026554-2e39f9ff-74af-4b99-a246-45fbdbd57bd9.png)
![image](https://user-images.githubusercontent.com/100894816/177026560-44df3bd0-04c2-495d-9d39-aa119f06ae5e.png)

- ![image](https://user-images.githubusercontent.com/100894816/177026566-c7ed4ce4-d845-4ae3-a2e5-69607efe4049.png)
![image](https://user-images.githubusercontent.com/100894816/177026568-d66db66f-9427-4c56-93ec-b82bb85ebd6c.png)
![image](https://user-images.githubusercontent.com/100894816/177026571-eec107a7-3161-4f12-8e9e-723a8640d1ab.png)
![image](https://user-images.githubusercontent.com/100894816/177026572-f5cb4f70-fa94-47e5-a32b-d6edf18f673f.png)
![image](https://user-images.githubusercontent.com/100894816/177026574-0325566a-1c1b-482a-a8f2-b165ec437999.png)

- ![image](https://user-images.githubusercontent.com/100894816/177026576-e112c4f3-8706-4dce-9c5f-291cb6825088.png)
![image](https://user-images.githubusercontent.com/100894816/177026578-50b6f1de-2fd4-4192-a9ab-e7057503b72d.png)
![image](https://user-images.githubusercontent.com/100894816/177026580-dbec26c9-bbf8-4e19-95a2-5fde8e8c8842.png)
![image](https://user-images.githubusercontent.com/100894816/177026581-cadf60cc-51f3-4d28-bbee-683d0af0fd88.png)
![image](https://user-images.githubusercontent.com/100894816/177026583-26033472-41f1-4aff-993f-a6c896051318.png)

- ![image](https://user-images.githubusercontent.com/100894816/177026589-3c66ef2d-1685-4b2a-bdf8-2537ccb0d042.png)

- ![image](https://user-images.githubusercontent.com/100894816/177026593-72e4f5b3-ff66-4003-95e6-5f00b5e92413.png)
![image](https://user-images.githubusercontent.com/100894816/177026594-69aa826e-a2fa-4b2a-b1b8-06af873f0a6d.png)
![image](https://user-images.githubusercontent.com/100894816/177026596-7b2e1db4-bcd2-4dbc-bbeb-5544ae6b056d.png)
![image](https://user-images.githubusercontent.com/100894816/177026598-78f08038-d9ba-483d-87ed-555c117f793f.png)
![image](https://user-images.githubusercontent.com/100894816/177026600-638b4c57-75e5-4ac2-a711-3c7bb8545e61.png)

<<< _predictor_model >>>
 - score -> 4.320905037331315
 - mean  -> 13.720639712154265
 - std   -> 3.1754087612692437


<<< _predictor_model_with_adjuster >>>
  - score -> 5.714972425326807
  - mean  -> 7.820889127307698
  - std   -> 1.368491139633183

<<< _predictor_target >>>
  - score -> 4.854775476521634
  - mean  -> 15.221062190989013
  - std   -> 3.135276237716899

<<< _predictor_target_with_adjuster >>>
  - score -> 7.28977612836715
  - mean  -> 10.915641043635977
  - std   -> 1.4973904344139293

