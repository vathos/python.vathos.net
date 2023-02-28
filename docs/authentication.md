<!-- markdownlint-disable -->

<a href="../vathos/authentication.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `authentication`
Authentication with the cloud REST API. 

To be granted access to its functions, all requests made to the API must include a valid access token in a special HTTP header. This token identifies a user or organization. It cannot be replicated or forged and expires after a certain amount of time. 


---

<a href="../vathos/authentication.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_client_token`

```python
get_client_token(client_id, client_secret, username, password)
```

Gets a user token. 

Users who are natural persons require four different credentials for authentication which are passed as arguments to this function. 



**Args:**
 
 - <b>`client_id`</b> (str):  client id 
 - <b>`client_secret`</b> (str):  client passphrase 
 - <b>`username`</b> (str):  user id 
 - <b>`password`</b>:  (str): user password 



**Returns:**
 
 - <b>`str`</b>:  A bearer token which must be passed in the authorization header with  every request made to the REST API. 


---

<a href="../vathos/authentication.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_service_account_token`

```python
get_service_account_token(client_id, client_secret)
```

Retrieves a service account token. 

A service account is an account not associated with a person but rather a device or organization. It can be obtained with the client id and secret alone.  



**Args:**
 
 - <b>`client_id`</b> (str):  client id 
 - <b>`client_secret`</b> (str):  client passphrase 



**Returns:**
 
 - <b>`str`</b>:  A bearer token which must be passed in the authorization header with  every request made to the REST API. 


