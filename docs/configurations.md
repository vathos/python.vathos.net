<!-- markdownlint-disable -->

<a href="../vathos/configurations.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `configurations`




**Global Variables**
---------------
- **BASE_URL**

---

<a href="../vathos/configurations.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_configuration`

```python
get_configuration(product_id, service, token)
```

Gets the most recent inference configuration. 



**Args:**
 
 - <b>`product_id`</b> (str):  id of the product for which the configuration was created 
 - <b>`service`</b> (str):  name of the inference service for which the configuraton was  created 
 - <b>`token`</b> (str):  API access token 



**Returns:**
 
 - <b>`dict`</b>:  configuration data 


