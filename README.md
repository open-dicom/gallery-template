# Vendor Model PROTOCOL

Sample PROTOCOL acquisition from a Vendor Model.

* Generate DICOM preview:
  
  Update *preview.py* with the absolute path to your local directory and run using [MRIcroGL](https://www.nitrc.org/projects/mricrogl) (*Scripting ⇾ Open*). Validate that *preview.png* was created and remove *preview.py*.

* Generate NIfTI preview:
  
  \[View NIfTI in NiiVue\](https://niivue.github.io/niivue/features/view.html?url=https://<user>.github.io/<repo>/nii/converted.nii.gz)


## General Information

This table may be extended with other modality or institution information.

|      Tag     | Name                      | Value                 |
|:------------:|---------------------------|-----------------------|
| (0008, 0060) | Modality                  | "MODALITY"            |
| (0008, 0070) | Manufacturer              | "MANUFACTURER"        |
| (0008, 0080) | Institution Name          | "Some Institution"    |
| (0008, 1090) | Manufacturer's Model Name | "Model"               |
| (0018, 1020) | Software Versions         | "Ver. Info E01"       |

Other vendor/modality/encoding-specific information should be included here.

## Patient Information

Any comments regarding the patient should be included here.

|      Tag     | Name                 | Value      |
|:------------:|----------------------|------------|
| (0010, 0010) | Patient's Name       | "Doe^John" |
| (0010, 0020) | Patient ID           | "0123"     |
| (0010, 0030) | Patient's Birth Date | "19500101" |
| (0010, 0040) | Patient's Sex        | "M"        |
| (0010, 1010) | Patient's Age        | "070Y"     |
| (0010, 1020) | Patient's Size       | "1.80"     |
| (0010, 1030) | Patient's Weight     | "70.0"     |

## Series Information

Any comments regarding series acquisition should be included here.

|      Tag     | Name               | Value                          |
|:------------:|--------------------|--------------------------------|
| (0008, 0021) | Series Date        | "20200101"                     |
| (0008, 0031) | Series Time        | "100000.000000"                |
| (0008, 103E) | Series Description | "series_description"           |

### Acquisition Parameters

Modality-specific acquisition parameters should be included here, e.g. for MR sequences the following may be included:

|      Tag     | Name                              | Value              |
|:------------:|-----------------------------------|--------------------|
| (0018, 0015) | Body Part Examined                | "BRAIN"            |
| (0018, 0020) | Scanning Sequence                 | ["AB", "CD"]       |
| (0018, 0021) | Sequence Variant                  | ["EF", "GH", "IJ"] |
| (0018, 0022) | Scan Options                      | "KL"               |
| (0018, 0023) | MR Acquisition Type               | "3D"               |
| (0018, 0024) | Sequence Name                     | "name"             |
| (0018, 0025) | Angio Flag                        | "N"                |
| (0018, 0050) | Slice Thickness                   | "1.0"              |
| (0018, 0080) | Repetition Time                   | "1000.0"           |
| (0018, 0081) | Echo Time                         | "1.0"              |
| (0018, 0082) | Inversion Time                    | "50.0"             |
| (0018, 0091) | Echo Train Length                 | "1"                |
| (0018, 0093) | Percent Sampling                  | "100.0"            |
| (0018, 0094) | Percent Phase Field of View       | "100.0"            |
| (0018, 0095) | Pixel Bandwidth                   | "100.0"            |
| (0018, 1310) | Acquisition Matrix                | [100, 0, 0, 100]   |
| (0018, 1312) | In-plane Phase Encoding Direction | "COL"              |
| (0018, 1314) | Flip Angle                        | "1.0"              |
| (0018, 5100) | Patient Position                  | "HFS"              |
| (0028, 0010) | Rows                              | 100                |
| (0028, 0011) | Columns                           | 100                |
| (0028, 0030) | Pixel Spacing                     | [1, 1]             |
