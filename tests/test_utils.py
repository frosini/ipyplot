import sys

import numpy as np
import pytest
import pandas as pd

sys.path.append(".")
sys.path.append("../.")
from ipyplot.utils import get_class_representations


TEST_OUT_IMAGES = ['a', 'b', 'c']
TEST_DATA = [
    # images, labels, ignore_list, labels_order, out_images, out_labels
    # data type tests
    (['c', 'b', 'a', 'd'], ['3', '2', '1', '3'], None, None, TEST_OUT_IMAGES, ['1', '2', '3']),  # NOQA E501
    (np.array(['c', 'b', 'a', 'd']), np.array(['3', '2', '1', '3']), None, None, TEST_OUT_IMAGES, np.array(['1', '2', '3'])),  # NOQA E501
    (pd.Series(['c', 'b', 'a', 'd']), pd.Series(['3', '2', '1', '3']), None, None, TEST_OUT_IMAGES, pd.Series(['1', '2', '3'])),  # NOQA E501
    (['c', 'b', 'a', 'd'], [3, 2, 1, 3], None, None, TEST_OUT_IMAGES, [1, 2, 3]),  # NOQA E501
    # ignore_list tests
    (['e', 'c', 'b', 'a', 'd'], ['4', '3', '2', '1', '3'], ['4'], None, TEST_OUT_IMAGES, ['1', '2', '3']),  # NOQA E501
    (['e', 'c', 'b', 'a', 'd'], [4, 3, 2, 1, 3], [4], None, TEST_OUT_IMAGES, [1, 2, 3]),  # NOQA E501
    # labels_order tests
    (['e', 'c', 'b', 'a', 'd'], ['4', '3', '2', '1', '3'], None, ['2', '1', '3'], ['b', 'a', 'c'], ['2', '1', '3']),  # NOQA E501
    (['c', 'b', 'a', 'd'], ['3', '2', '1', '3'], None, ['2', '1', '4', '3'], ['b', 'a', 'c'], ['2', '1', '3']),  # NOQA E501
    (['e', 'c', 'b', 'a', 'd'], [4, 3, 2, 1, 3], None, [2, 1, 3], ['b', 'a', 'c'], [2, 1, 3]),  # NOQA E501
    (['c', 'b', 'a', 'd'], [3, 2, 1, 3], None, [2, 1, 4, 3], ['b', 'a', 'c'], [2, 1, 3]),  # NOQA E501
    # labels_order + ignore_list tests
    (['e', 'c', 'b', 'a', 'd'], ['4', '3', '2', '1', '3'], ['1'], ['2', '1', '3'], ['b', 'c'], ['2', '3']),  # NOQA E501
    (['c', 'b', 'a', 'd'], ['3', '2', '1', '3'], ['1'], ['2', '1', '4', '3'], ['b', 'c'], ['2', '3']),  # NOQA E501
    (['e', 'c', 'b', 'a', 'd'], [4, 3, 2, 1, 3], [1], [2, 1, 3], ['b', 'c'], [2, 3]),  # NOQA E501
    (['c', 'b', 'a', 'd'], [3, 2, 1, 3], [1], [2, 1, 4, 3], ['b', 'c'], [2, 3]),  # NOQA E501
]


@pytest.mark.parametrize(
    "images, labels, ignore_list, labels_order, out_images, out_labels",
    TEST_DATA)
def test_get_class_representations(
        images, labels, ignore_list, labels_order, out_images, out_labels):
    images, labels = get_class_representations(
        images,
        labels=labels,
        ignore_list=ignore_list,
        labels_order=labels_order)
    assert all(images == out_images)
    assert all(labels == out_labels)