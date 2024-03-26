from dicom_converter import DICOMConverter

def pipeline():
    dicom_path = input("Enter the path to the DICOM directory: ")
    nifti_path = input("Enter the path for the output NIfTI files: ")
    converter = DICOMConverter(dicom_path, nifti_path)
    converter.convert_to_nifti()

if __name__ == "__main__":
    pipeline()
