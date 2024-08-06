<<<<<<< HEAD

# ImaToDicomConverter

ImaToDicomConverter is a Python utility for converting Siemens IMA files to DICOM format. This tool is particularly useful for medical imaging professionals who need to work with DICOM files for analysis, storage, or sharing. The utility ensures a seamless conversion process while preserving essential metadata.

## Features

- Recursively scans directories to find `.ima` files.
- Converts `.ima` files to DICOM format.
- Maintains the original directory structure in the output folder.
- Logs the conversion process for easy tracking and troubleshooting.

## Requirements

- Python 3.6+
- pydicom library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ImaToDicomConverter.git
    cd ImaToDicomConverter
    ```

2. Install the required Python packages:
    ```bash
    pip install pydicom
    ```

## Usage

1. Place your IMA files in a directory named `01_MRI_Data` within the same directory as the script.

2. Run the script:
    ```bash
    python convert_ima_to_dicom.py
    ```

3. The converted DICOM files will be saved in a directory named `DICOM_Output` within the same directory as the script.

## Logging

The script generates a log file named `conversion.log` in the same directory as the script. This log file records detailed information about the conversion process, including successful conversions and any errors encountered.

## Example Directory Structure

```
=======
ImaToDicomConverter
ImaToDicomConverter is a Python utility for converting Siemens IMA files to DICOM format. This tool is particularly useful for medical imaging professionals who need to work with DICOM files for analysis, storage, or sharing. The utility ensures a seamless conversion process while preserving essential metadata.

Features
Recursively scans directories to find .ima files.
Converts .ima files to DICOM format.
Maintains the original directory structure in the output folder.
Logs the conversion process for easy tracking and troubleshooting.
Requirements
Python 3.6+
pydicom library
Installation
Clone the repository:

bash
Kodu kopyala
git clone https://github.com/yourusername/ImaToDicomConverter.git
cd ImaToDicomConverter
Install the required Python packages:

bash
Kodu kopyala
pip install pydicom
Usage
Place your IMA files in a directory named 01_MRI_Data within the same directory as the script.

Run the script:

bash
Kodu kopyala
python convert_ima_to_dicom.py
The converted DICOM files will be saved in a directory named DICOM_Output within the same directory as the script.

Logging
The script generates a log file named conversion.log in the same directory as the script. This log file records detailed information about the conversion process, including successful conversions and any errors encountered.

Example Directory Structure
c
Kodu kopyala
>>>>>>> a65c26d4095d60b778dc44478554a132634c3515
ImaToDicomConverter/
├── convert_ima_to_dicom.py
├── conversion.log
├── 01_MRI_Data/
│   ├── patient1/
│   │   ├── scan1.ima
│   │   ├── scan2.ima
│   └── patient2/
│       ├── scan1.ima
│       ├── scan2.ima
└── DICOM_Output/
    ├── patient1/
    │   ├── scan1.dcm
    │   ├── scan2.dcm
    └── patient2/
        ├── scan1.dcm
        ├── scan2.dcm
<<<<<<< HEAD
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

Special thanks to the developers of the pydicom library for making DICOM file manipulation in Python easy and efficient.
=======
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Special thanks to the developers of the pydicom library for making DICOM file manipulation in Python easy and efficient.

>>>>>>> a65c26d4095d60b778dc44478554a132634c3515
