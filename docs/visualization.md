<!-- markdownlint-disable -->

<a href="../vathos/visualization.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `visualization`
Visualization. 

**Global Variables**
---------------
- **VISUALIZATION_ENABLED**

---

<a href="../vathos/visualization.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `unpack_short`

```python
unpack_short(rgb)
```

Unpacks two byte channels into a single channel of type short. 


---

<a href="../vathos/visualization.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `backproject`

```python
backproject(depth, K)
```

Backprojects a depth image into a point cloud. 


---

<a href="../vathos/visualization.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `visualize_detections`

```python
visualize_detections(
    mesh_path,
    scale,
    test_image_path,
    projection_matrix,
    detections
)
```

Visualizes a point cloud and detections. 


