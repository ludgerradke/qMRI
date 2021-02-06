import pydicom
from pydicom.dataset import Dataset, FileMetaDataset, FileDataset
from pydicom.uid import ExplicitVRLittleEndian
import pydicom._storage_sopclass_uids
import numpy as np
import os
import shutil


def create_test_dicom(file: str = r'default.dcm', number_of_pixel: int = 100):
    """
    Function to create a Dicom template file

    :param file: Filename of dicom template
    :param number_of_pixel: Number of pixels of the dicom image along one side.
        The total number of pixels are number_of_pixels^2
    :return:
    """
    # create dicom meta information
    meta = FileMetaDataset()
    meta.MediaStorageSOPClassUID = pydicom._storage_sopclass_uids.MRImageStorage
    meta.MediaStorageSOPInstanceUID = pydicom.uid.generate_uid()
    meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian

    # create dataset and add meta information
    ds = FileDataset(file, {},
                     file_meta=meta, preamble=b"\0" * 128)


    # add some information
    ds.SOPClassUID = pydicom._storage_sopclass_uids.MRImageStorage
    ds.PatientName = "Max Mustermann"
    ds.PatientID = "42"

    ds.Modality = "MR"
    ds.SeriesInstanceUID = pydicom.uid.generate_uid()
    ds.StudyInstanceUID = pydicom.uid.generate_uid()
    ds.FrameOfReferenceUID = pydicom.uid.generate_uid()

    ds.BitsStored = 16
    ds.BitsAllocated = 16
    ds.SamplesPerPixel = 1
    ds.HighBit = 15

    ds.ImagesInAcquisition = "1"
    ds.InstanceNumber = 1

    ds.ImagePositionPatient = r"0\0\1"
    ds.ImageOrientationPatient = r"1\0\0\0\-1\0"
    ds.ImageType = r"ORIGINAL\PRIMARY\AXIAL"

    ds.RescaleIntercept = "0"
    ds.RescaleSlope = "1"
    ds.PixelSpacing = r"1\1"
    ds.PhotometricInterpretation = "MONOCHROME2"
    ds.PixelRepresentation = 1

    pydicom.dataset.validate_file_meta(ds.file_meta, enforce_standard=True)

    # create numpy gray image
    ds.Rows = number_of_pixel
    ds.Columns = number_of_pixel

    pixel_array = np.zeros((number_of_pixel, number_of_pixel))
    pixel_array[int(0.4 * number_of_pixel):int(0.6 * number_of_pixel),
    int(0.4 * number_of_pixel):int(0.6 * number_of_pixel)] = 1000
    pixel_array = pixel_array.astype(np.uint16)

    ds.PixelData = pixel_array.tobytes()
    ds.save_as(file)


def create_dicom_test_folder(folder: str, number: int):
    if os.path.exists(folder):
        return 'FolderExist'
    if not number * 10 == int(number) * 10:
        return 'number must be a positive int'
    if number < 0:
        return 'number must be a positive int'
    os.mkdir(folder)
    for i in range(number):
        create_test_dicom(folder + '/dicom_dyn_{}.dcm'.format(i))


def delete_dicom_test_folder(folder):
    shutil.rmtree(folder)
