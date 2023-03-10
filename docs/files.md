<!-- markdownlint-disable -->

<a href="../vathos/files.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `files`
File operations. 

**Global Variables**
---------------
- **BASE_URL**

---

<a href="../vathos/files.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `upload_files`

```python
upload_files(file_list, token, sync=False, device=None)
```

Uploads one or multiple files. 



**Args:**
 
 - <b>`file_list`</b> (list):  list of paths of files on disk to upload 



**Returns:**
 
 - <b>`list`</b>:  meta data objects of uploaded files 


---

<a href="../vathos/files.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_file`

```python
get_file(file_id, token)
```

Downloads a file from the REST API. 



**Args:**
 file_id (str): id of the file to get 



**Returns:**
 
 - <b>`BytesIO`</b>:  byte representation of the file 


