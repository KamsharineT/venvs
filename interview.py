''' The Question from the interviewer '''

import json
# You are tasked with analyzing health insurance claims data represented in a JSON format. The data includes information about patients and their associated claims. You need to perform several tasks to extract insights and analyze patterns in the claims data.


# # Task 1: Extract Related Claims
# extactAllClaims(C003): [C003]
# # Part A: Write a function to extract all claims related to a given claim ID from the provided JSON data. Return a list of related claim IDs.

# # Part B: Using the same JSON data, write a function to find the maximum claim amount in the last 'n' days for a given patient ID.

class Solution:
    def solution(self,s,jsons):
        
        cllist = []
        cllist.append(s)
        claims = jsons['patients'][0]['claims']
        bid, amn, date = None, None, None  # Initialize these variables
        for i in range(len(claims)):
            cl = claims[i]
            print(cl["id"],"alias  ",s)
            if (cl["id"] == s):
              bid = cl["billingCodeId"]
              amn = cl["amount"]
              date = cl["date"]
              continue
            
            if bid == cl["billingCodeId"] or amn == cl["amount"] or date == cl["amount"]:
              print(cl["id"])
              cllist.append(cl["id"])
        
        return cllist

    def maxclaim(self,p,jsons):
      maxam = 0
      patients = jsons['patients']

      for j in range(len(patients)):
        # print(patients[j]["id"])
        if(patients[j]["id"] == p):
          for l in range(len((patients[j]["claims"]))):
            if (patients[j]["claims"][l]["amount"]) > maxam:
              maxam = (patients[j]["claims"][l]["amount"])
      
      return maxam

def main():
    jsons = {
  "patients": [
    {
      "id": "P002",
      "claims": [
        {
          "id": "C001",
          "amount": 1000,
          "billingCodeId": "B001",
          "date": "2024-01-01"
        },
        {
          "id": "C002",
          "amount": 200,
          "billingCodeId": "B001",
          "date": "2024-01-05"
        },
        {
          "id": "C003",
          "amount": 1500,
          "billingCodeId": "B002",
          "date": "2024-01-10"
        }
      ]
    },
    {
      "id": "P001",
      "claims": [
        {
          "id": "C004",
          "amount": 1000,
          "billingCodeId": "B001",
          "date": "2024-01-01"
        },
        {
          "id": "C005",
          "amount": 2000,
          "billingCodeId": "B001",
          "date": "2024-01-05"
        },
        {
          "id": "C006",
          "amount": 150,
          "billingCodeId": "B002",
          "date": "2024-01-10"
        }
      ]
    }
  ],
  "billingCodes": [
    {
      "id": "B001",
      "description": "Billing code description for B001"
    },
    {
      "id": "B002",
      "description": "Billing code description for B002"
    }
  ]
}
    
    
    line = input()
    ret = Solution().solution(line,jsons)
    print(ret)

    patid = input()
    maxclaimamn = Solution().maxclaim(patid,jsons)
    print(maxclaimamn)

if __name__ == '__main__':
    main()

''' These were the theory questions I faced during the interview'''
# memory management
# heap and stack memory
# garbage colelction
# asyncio
# Describe how asynchronous programming in Python achieves concurrency. How does it differ from using threading or multiprocessing?
''' The End'''

