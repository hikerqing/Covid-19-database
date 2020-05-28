#1、选择两个国家、开始、截止日期、现存确诊人数/疑似病例数/死亡人数/治愈人数/累计确诊人数
#!这里不考虑复发的情况，并且认为死亡都是在确诊之后
#第一个国家开始日期的确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’confirmed’ and confirmed_date<=DATE1
Group by city
Having country=’COUNTRY1’
#第一个国家截止日期的确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’confirmed’ and confirmed_date<=DATE2
Group by city
Having country=’COUNTRY1’
#第二个国家开始日期的确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’confirmed’ and confirmed_date<=DATE1
Group by city
Having country=’COUNTRY2’
#第二个国家截止日期的确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’confirmed’ and confirmed_date<=DATE2
Group by city
Having country=’COUNTRY2’

#第一个国家开始日期的确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’suspected’ and suspected_date<=DATE1
Group by city
Having country=’COUNTRY1’
#第一个国家截止日期的确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’suspected’ and suspected_date<=DATE2
Group by city
Having country=’COUNTRY1’
#第二个国家开始日期的确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’suspected’ and suspected_date<=DATE1
Group by city
Having country=’COUNTRY2’
#第二个国家截止日期的确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’suspected’ and suspected_date<=DATE2
Group by city
Having country=’COUNTRY2’

#第一个国家开始日期的死亡人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’dead’ and left_date<=DATE1
Group by city
Having country=’COUNTRY1’
#第一个国家截止日期的死亡人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’dead’ and left_date<=DATE2
Group by city
Having country=’COUNTRY1’
#第二个国家开始日期的死亡人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’dead’ and left_date<=DATE1
Group by city
Having country=’COUNTRY2’
#第二个国家截止日期的死亡人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’dead’ and left_date<=DATE2
Group by city
Having country=’COUNTRY2’

#第一个国家开始日期的治愈人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’cured’ and left_date<=DATE1
Group by city
Having country=’COUNTRY1’
#第一个国家截止日期的治愈人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’cured’ and left_date<=DATE2
Group by city
Having country=’COUNTRY1’
#第二个国家开始日期的治愈人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’cured’ and left_date<=DATE1
Group by city
Having country=’COUNTRY2’
#第二个国家截止日期的治愈人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’cured’ and left_date<=DATE2
Group by city
Having country=’COUNTRY2’

#第一个国家开始日期的累计确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where (situation=’confirmed’ and confirmed_date<=DATE1)
Or (situation=’dead’ and left_date<=DATE1)
Or (situation=’cured’ and left_date<=DATE1)
Group by city
Having country=’COUNTRY1’
#第一个国家截止日期的累计确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where (situation=’confirmed’ and confirmed_date<=DATE2)
Or (situation=’dead’ and left_date<=DATE2)
Or (situation=’cured’ and left_date<=DATE2)
Group by city
Having country=’COUNTRY1’
#第二个国家开始日期的累计确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where (situation=’confirmed’ and confirmed_date<=DATE1)
Or (situation=’dead’ and left_date<=DATE1)
Or (situation=’cured’ and left_date<=DATE1)
Group by city
Having country=’COUNTRY2’
#第二个国家截止日期的累计确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where (situation=’confirmed’ and confirmed_date<=DATE2)
Or (situation=’dead’ and left_date<=DATE2)
Or (situation=’cured’ and left_date<=DATE2)
Group by city
Having country=’COUNTRY2’
