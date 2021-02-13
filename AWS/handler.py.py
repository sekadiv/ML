#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
import json


# In[3]:


def lamda_handle(event,context):
    client=boto3.client("rekognition")
    response=client.recognize_celebrities(
    Image={
        'S3Object': {
            'Bucket': event['bucket'],
            'Name': event['object_name']
        }
    }
)
    return (response['CelebrityFaces'][0]['Name'])


# In[ ]:




