from pathlib import Path

import gl

path = Path("/path/to/here")
nii = str(path / "nii/converted")

gl.resetdefaults()
gl.bmpzoom(1)
gl.loadimage(nii)
gl.extract(0, 1, 5)
gl.mosaic(
    "A L- H -0.1 V -0.1 0.125 0.25 0.375 0.5; 0.625 0.75 0.875 S X R 0.5"
)
gl.savebmp(str(path / "preview.png"))
