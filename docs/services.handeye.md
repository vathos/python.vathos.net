<!-- markdownlint-disable -->

<a href="../vathos/services/handeye.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `services.handeye`




**Global Variables**
---------------
- **BASE_URL**

---

<a href="../vathos/services/handeye.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `upload_data`

```python
upload_data(csv_file_name, session, token)
```

Uploads images and poses for hand-eye calibration. 


---

<a href="../vathos/services/handeye.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `handeye_calibration`

```python
handeye_calibration(
    poses,
    projection_matrix,
    pattern_sidelength,
    pattern_size,
    eye_in_hand,
    token,
    session=None
)
```

Runs a hand-eye calibration. 



**Args:**
 
 - <b>`poses`</b> (str):  path to a CSV file containing the poses and a reference to the  associated image. Each row consists of 17 columns. The first column  contains the path of the image on disk. The following 16 columns store  the pose of the robot when the image was captured as homogenous  $4\times4$ matrix in colum-major ordering. 
 - <b>`projection_matrix`</b> (numpy.ndarray):  a $3\times 3$ projection matrix of the   used camera 
 - <b>`pattern_sidelength`</b> (float):  length of squares in ther pattern in meters 
 - <b>`pattern_size`</b> (tuple):  numer of inner corners of the patterns in horizontal  and vertical direction 
 - <b>`eye_in_hand`</b>:  True if the camera is mounted on the end-effector of the robot,  False for static cameras. 
 - <b>`token`</b> (str):  API access token 
 - <b>`session`</b> (str):  optional session id under which all calibration images are  stored 



**Returns:**
 
 - <b>`numpy.ndarray`</b>:  homogenous $4\times 4$ matrix of the transformation between  the camera and flange coordinate system (if `eye_in_hand==True`), or the  camera coordinate system and a fixed robot base (if `eye_in_hand==False`) 


