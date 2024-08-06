import os
import pydicom
from pydicom.dataset import FileDataset
import datetime
import logging

# Loglama için ayarları yap
logging.basicConfig(filename='conversion.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def convert_ima_to_dicom(root_dir, output_dir):
    total_converted = 0
    for subdir, _, files in os.walk(root_dir):
        logging.info(f"Checking directory: {subdir}")
        for file in files:
            if file.endswith(".ima"):
                ima_path = os.path.join(subdir, file)
                
                # Create a parallel directory structure in the output folder
                rel_path = os.path.relpath(subdir, root_dir)
                output_subdir = os.path.join(output_dir, rel_path)
                os.makedirs(output_subdir, exist_ok=True)
                
                dicom_path = os.path.join(output_subdir, os.path.splitext(file)[0] + ".dcm")
                logging.info(f"Converting {ima_path} to DICOM")
                try:
                    # Read IMA file directly with pydicom
                    ds = pydicom.dcmread(ima_path)
                    
                    # Modify necessary attributes
                    ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian
                    ds.is_little_endian = True
                    ds.is_implicit_VR = False
                    
                    # Save as DICOM
                    ds.save_as(dicom_path)
                    
                    total_converted += 1
                    logging.info(f"Successfully converted {ima_path} to {dicom_path}")
                except Exception as e:
                    logging.error(f"Failed to convert {ima_path}: {str(e)}")
    
    logging.info(f"Total IMA files converted to DICOM: {total_converted}")
    print(f"Total IMA files converted to DICOM: {total_converted}")

# Dynamically set the root directory to the same directory as the script
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(script_dir, "01_MRI_Data")
output_dir = os.path.join(script_dir, "DICOM_Output")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

logging.info(f"Starting conversion in root directory: {root_dir}")
logging.info(f"Output directory: {output_dir}")

convert_ima_to_dicom(root_dir, output_dir)