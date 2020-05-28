#1、选择两个国家、开始、截止日期、现存确诊人数/疑似病例数/死亡人数/治愈人数/累计确诊人数
#!这里不考虑复发的情况，并且认为死亡都是在确诊之后
#第一个国家的确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’confirmed’ and confirmed_date<=DATE1
Group by city
Having country=’COUNTRY1’
Where DATE in (select *
From generate_series(‘DATE1’::timestamp,’DATE2’,’24 hours’))
#第二个国家的确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’confirmed’ and confirmed_date<=DATE1
Group by city
Having country=’COUNTRY2’
Where DATE in (select *
From generate_series(‘DATE1’::timestamp,’DATE2’,’24 hours’))

#第一个国家的疑似人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’suspected’ and suspected_date<=DATE1
Group by city
Having country=’COUNTRY1’
Where DATE in (select *
From generate_series(‘DATE1’::timestamp,’DATE2’,’24 hours’))
#第二个国家的疑似人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’suspected’ and suspected_date<=DATE1
Group by city
Having country=’COUNTRY2’
Where DATE in (select *
From generate_series(‘DATE1’::timestamp,’DATE2’,’24 hours’))

#第一个国家日期的死亡人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’dead’ and left_date<=DATE1
Group by city
Having country=’COUNTRY1’
Where DATE in (select *
From generate_series(‘DATE1’::timestamp,’DATE2’,’24 hours’))
#第二个国家的死亡人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’dead’ and left_date<=DATE1
Group by city
Having country=’COUNTRY2’
Where DATE in (select *
From generate_series(‘DATE1’::timestamp,’DATE2’,’24 hours’))

#第一个国家的治愈人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’cured’ and left_date<=DATE1
Group by city
Having country=’COUNTRY1’
Where DATE in (select *
From generate_series(‘DATE1’::timestamp,’DATE2’,’24 hours’))
#第二个国家的治愈人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where situation=’cured’ and left_date<=DATE1
Group by city
Having country=’COUNTRY2’
Where DATE in (select *
From generate_series(‘DATE1’::timestamp,’DATE2’,’24 hours’))

#第一个国家的累计确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where (situation=’confirmed’ and confirmed_date<=DATE1)
Or (situation=’dead’ and left_date<=DATE1)
Or (situation=’cured’ and left_date<=DATE1)
Group by city
Having country=’COUNTRY1’
Where DATE in (select *
From generate_series(‘DATE1’::timestamp,’DATE2’,’24 hours’))
#第二个国家的累计确诊人数
Select count(case_id),city
From cases,SITE
Where cases.site_id=SITE.site_id
Where (situation=’confirmed’ and confirmed_date<=DATE1)
Or (situation=’dead’ and left_date<=DATE1)
Or (situation=’cured’ and left_date<=DATE1)
Group by city
Having country=’COUNTRY2’
Where DATE in (select *
From generate_series(‘DATE1’::timestamp,’DATE2’,’24 hours’))

#某个国家某类药物、开始、截止日期、药物研发情况
With researcher_institution(researcher_id,trial_id,institution_id,institution_location)
As (select researcher_id,trial_id,institution_id,institution_location
From researcher_experiment natural join institution natural join institution_researcher natural join experiment
Where start_date<=DATE and end_date>=DATE),
Drug_trial(trial_id,drug_id,drug_type)
As (select trial_id,drug_id,drug_type
From trial_drug natural join drug)
Select institution_loction,count(drug_id)
From researcher_institution natural join trial_drug
Where drug_type=’TYPE’
Group by institution_location
Where DATE in (select *
From generate_series(‘DATA1’’::timestamp,’DATE2’,’24hours’))
