# -*- coding: utf-8 -*-

#  baldwin-shortcuts
# ------------------------
# A library of functions to make Bryan's life easier.

# Author: Bryan Baldwin <bryanabaldwin@gmail.com> (c) 2022
# Website: 

# Shortcut Functions
# Created: 2022-03-11
# Last Edited: 2022-03-11
# ------------------------


import math
from google.cloud import bigquery

# this function converts bytes into a more readable format
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   elif size_bytes == None:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


# this function will dry run a BigQuery query
def bigquery_dryrun(client,sql):
    job_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)
    # Start the query, passing in the extra configuration.
    query_job = client.query(sql,
        job_config=job_config,
    )  # Make an API request.
    if query_job.errors == None:
        return "This query will process {}.".format(convert_size(query_job.total_bytes_processed))
    else:
        raise NotImplementedError(f"Query Error: {query_job.errors}")