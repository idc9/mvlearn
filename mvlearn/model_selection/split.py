# Copyright 2019 NeuroData (http://neurodata.io)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Authors: Alexander Chang, Gavin Mischler

import numpy as np
from sklearn import model_selection as ms


def train_test_split(*inputs, **options):
    r'''
    Splits multi-view data into random train and test subsets. This
    utility wraps the train_test_split function from
    sklearn.model_selection for ease of use.

    Parameters
    ----------
    inputs : sequence of indexables
        Allowed inputs are lists of numpy arrays, numpy arrays, lists,
        scipy-sparse matrices or pandas dataframes.

    test_size : float or int, default=None
        If float, should be between 0.0 and 1.0 and represent the
        proportion of the dataset to include in the test split. If
        int, represents the absolute number of test samples. If None,
        the value is set to the complement of the train size. If
        train_size is also None, it will be set to 0.25.

    train_size: float or int, default=None
        If float, should be between 0.0 and 1.0 and represent the
        proportion of the dataset to include in the train split. If
        int, represents the absolute number of train samples. If None,
        the value is automatically set to the complement of the test
        size.

    random_state: int or RandomState instance, default=None
        Controls the shuffling applied to the data before applying the
        split. Pass an int for reproducible output across multiple
        function calls.

    shuffle: bool, default=True
        Whether or not to shuffle the data before splitting. If
        shuffle=False then stratify must be None.

    stratify: array-like, default=None
        If not None, data is split in a stratified fashion, using
        this as the class labels.

    Returns
    -------
    splitting : list, length=2*len(arrays)
        List containing the train-test splits of each of the inputs. If
        a list of arrays or 3D array is one of the inputs, train_test_split
        operates on each subarray and puts them together into a list
        of arrays or 3D array for training and one for testing.

    Examples
    --------
    >>> from mvlearn.preprocessing import train_test_split
    >>> import numpy as np
    >>> Xs = np.arange(18).reshape((3, 3, 2))
    >>> y = np.arange(3)
    >>> # Print the data
    >>> for i in range(len(data)):
    ...     print('Xs[%d]' % i, Xs[i], sep='\n')
    >>> print('y', y, sep='\n')
    Xs[0]
    [[0 1]
     [2 3]
     [4 5]]
    Xs[1]
    [[ 6  7]
     [ 8  9]
     [10 11]]
    Xs[2]
    [[12 13]
     [14 15]
     [16 17]]
    y
    [0 1 2]
    >>> Xs_train, Xs_test, y_train, y_test = train_test_split(Xs, y,
    ...                                            test_size=0.33,
    ...                                            random_state=10)
    >>> # Print train set
    >>> for i in range(len(Xs_train)):
    ...     print('Xs_train[%d]' % i, Xs_train[i], sep='\n')
    Xs_train[0]
    [[4 5]
    [2 3]]
    Xs_train[1]
    [[10 11]
    [ 8  9]]
    Xs_train[2]
    [[16 17]
    [14 15]]
    # Print test set
    >>> for i in range(len(Xs_test)):
    ...     print('Xs_test[%d]' % i, Xs_test[i], sep='\n')

    Xs_test[0]
    [[0 1]]
    Xs_test[1]
    [[6 7]]
    Xs_test[2]
    [[12 1]]
    >>> print(y_train)
    [2 1]
    >>> print(y_test)
    [0]
    '''

    splitting = []
    for a in inputs:
        splits = None
        if isinstance(a, list) or (isinstance(a, np.ndarray) and
                                   a.ndim == 3):
            splits = ms.train_test_split(*a, **options)
            splits = (splits[::2], splits[1::2])
        else:
            splits = ms.train_test_split(a, **options)

        for split in splits:
            splitting.append(split)

    return splitting
