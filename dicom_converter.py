import dicom2nifti
import os

class DICOMConverter:
    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory

    def convert_to_nifti(self):
        try:
            if not os.path.exists(self.output_directory):
              os.makedirs(self.output_directory)

            dicom2nifti.convert_directory(self.input_directory, self.output_directory)
            print(f"Conversion successful. NIfTI files saved to {self.output_directory}.")
        except Exception as e:
            print(f"An error occurred during conversion: {e}")
