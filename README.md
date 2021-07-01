# Amazon_Vine_Analysis

## Overview
The Amazon Vine program is a service that allows manufacturers and publishers to receive reviews for their products. Companies pay a small fee to Amazon and provide products to Amazon Vine members, who are then required to publish a review.

I analyzed Amazon reviews written by members of the paid Amazon Vine program. 
  - PySpark to perform the ETL process to extract the dataset, transform the data, connect to an AWS RDS instance, and load the transformed data into pgAdmin.
  - PySpark to determine if there is any bias toward favorable reviews from Vine members in the dataset.

To better understand the results, please note the following:
  - Total votes in the orginal dataframe were 1,785,997. 
  - Total five star reviews in the original dataframe were 1,026,924
  - New dataframe created for reviews with votes >= 20 
    - "new_vine_df = vine_df.filter("total_votes>=20")"
  - New dataframe created to reveal helpful votes were 50% or more of total votes.
    - "divided_votes_df = new_vine_df.filter("(helpful_votes/total_votes)>=.5")"
  - divided_votes_df was used to answer questions in results.

## Results
- How many Vine reviews and non-Vine reviews were there?
  - There were 94 Vine reviews that had more than 20 votes and 50% or more of those votes were labeled as helpful.
    - ![paid_df](https://user-images.githubusercontent.com/78178900/124157430-5ef7a100-da5e-11eb-930f-ee6778bc642c.png)
    - ![paid_count](https://user-images.githubusercontent.com/78178900/124157505-759df800-da5e-11eb-9d6e-dfd025670acc.png)
  
  - There 40,471 non-Vine reviews that had more than 20 votes and 50% or more of those votes were labeled as helpful.
    - ![nonpaid_df](https://user-images.githubusercontent.com/78178900/124157618-949c8a00-da5e-11eb-8907-d18b1a863a00.png)
    - ![non_paid_count](https://user-images.githubusercontent.com/78178900/124157727-b39b1c00-da5e-11eb-9120-a52f9e94effb.png)

- How many Vine reviews were 5 stars?
  - There were 48 5-star Vine reviews that had more than 20 votes and 50% or more of those votes were labeled as helpful.
    - ![paid_five_count](https://user-images.githubusercontent.com/78178900/124158226-450a8e00-da5f-11eb-8d31-009f0eb0fb5e.png)


- How man non-Vine reviews were 5 stars?
  - There were 15,663 5-star non-Vine reviews that had more than 20 votes and 50% or more of those votes were labeled as helpful.
    - ![nonpaid_five_count](https://user-images.githubusercontent.com/78178900/124158257-4e93f600-da5f-11eb-9246-edc6f8eb8825.png)


- What percentage of Vine reviews were 5 stars?
  - %51.06 of the Vine reviews that had more than 20 votes and 50% or more of those votes were labeled as helpful, were 5-stars.
    - ![paidfive_percentage](https://user-images.githubusercontent.com/78178900/124158827-05907180-da60-11eb-8c00-04eb3e052513.png)


- What percentage of non-vine reviews were 5 stars?
  - %51.06 of the non-![nonpaid_five_percentage](https://user-images.githubusercontent.com/78178900/124158889-193bd800-da60-11eb-8ef2-86fe55e35f30.png)
    - Vine reviews that had more than 20 votes and 50% or more of those votes were labeled as helpful, were 5-stars.




# Summary
