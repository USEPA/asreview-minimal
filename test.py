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
"""Ensure that that the modules import correctly."""

from asreview.models import balance, classifiers, feature_extraction, query

# get balancers
balancers = balance.utils.list_balance_strategies()
assert len(balancers)

# get classifiers
classifiers = classifiers.utils.list_classifiers()
assert len(classifiers)

# get vectorizers
balancers = feature_extraction.utils.list_feature_extraction()
assert len(balancers)

# get queries
balancers = query.utils.list_query_strategies()
assert len(balancers)
