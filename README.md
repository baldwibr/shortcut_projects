# Shortcut Projects
A repo of sharable tools useful to me.

## Bytes Convert
A function that will take a value of bytes and convert them to a more common  
way of representing bytes. This is a base 1024 byte system.

#### Parameters: 
* **bytes**- This is the raw number of bytes

#### Returns:
* The bytes in terms of base 1024 bytes.
* For example: 1,598,722 becomes **1.52 Mb**

## BigQuery Dry run
This function will perform a dry run of a query and return the amount of  
billable bytes processed when the query is executed.

#### Parameters:
* **client**- This is the client configuration for your BigQuery session.
* **sql**- This is the sql/script being passed to BigQuery for evaluation.

#### Returns:
* Billable bytes processed
* If the dry run fails, it will return the error.
