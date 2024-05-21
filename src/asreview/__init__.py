# Copyright 2019-2022 The ASReview Authors. All Rights Reserved.
# Copyright 2024 U.S. Federal Government (in countries where recognized)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from importlib.metadata import version

from asreview.utils import asreview_path, get_data_home

__version__ = version("asreview_minimal")

__all__ = [
    "asreview_path",
    "get_data_home",
]

# deprecated in __init__.py, use asreview.models.feature_extraction instead
from asreview._deprecated import _deprecated_func
from asreview.models.feature_extraction.embedding_lstm import (
    load_embedding as _load_embedding,
)
from asreview.models.feature_extraction.embedding_lstm import (
    sample_embedding as _sample_embedding,
)
from asreview.models.feature_extraction.embedding_lstm import (
    text_to_features as _text_to_features,
)


@_deprecated_func(
    "Importing load_embedding from asreview.load_embedding is deprecated, "
    "use asreview.models.feature_extraction.load_embedding instead"
)
def load_embedding(*args, **kwargs):
    return _load_embedding(*args, **kwargs)


@_deprecated_func(
    "Importing sample_embedding from asreview.sample_embedding is deprecated, "
    "use asreview.models.feature_extraction.sample_embedding instead"
)
def sample_embedding(*args, **kwargs):
    return _sample_embedding(*args, **kwargs)


@_deprecated_func(
    "Importing text_to_features from asreview.text_to_features is deprecated, "
    "use asreview.models.feature_extraction.text_to_features instead"
)
def text_to_features(*args, **kwargs):
    return _text_to_features(*args, **kwargs)
