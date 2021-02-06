import numpy as np


def transform_dicom_ds_list_to_array(ds_list: list, information=False):
    array_list = [ds.pixel_array for ds in ds_list]
    array_np = np.array(array_list)
    if information:
        return array_np, transform_dicom_information_to_dict(ds_list[0])
    return array_np, None


def transform_dicom_information_to_dict(ds):
    information = {}
    keys = ds.dir()
    for key in keys:
        information[key] = ds.data_element(key).value
    return information
