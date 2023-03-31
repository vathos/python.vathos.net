<!-- markdownlint-disable -->

<a href="../vathos/io/packing.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `io.packing`
Various byte packing algorithms. 


---

<a href="../vathos/io/packing.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `pack_short`

```python
pack_short(short_array)
```

Packs two bytes of a single short channel into RG channels of an RGB image.  




---

<a href="../vathos/io/packing.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `unpack_short`

```python
unpack_short(rgb)
```

Unpack two byte channels into a single channel of type short. 


---

<a href="../vathos/io/packing.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `pack_float`

```python
pack_float(float_array)
```

Packs four bytes of a single float channel into an RGBA image. 


---

<a href="../vathos/io/packing.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `unpack_float`

```python
unpack_float(rgba)
```

Unpacks four byte channels into a single channel of type float. 


