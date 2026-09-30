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
from asreview.models import classifiers as classifiers_module

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

# models work as steps of a fitted scikit-learn pipeline
from sklearn.exceptions import NotFittedError  # noqa: E402
from sklearn.pipeline import Pipeline  # noqa: E402
from sklearn.utils.validation import check_is_fitted  # noqa: E402

texts = [
    "toxicity of lead in drinking water",
    "lead exposure and neurodevelopment",
    "cancer risk from arsenic in groundwater",
    "arsenic exposure and skin lesions",
    "soccer match results from the weekend",
    "a recipe for chocolate chip cookies",
    "travel guide to mountain hiking trails",
    "review of the latest smartphone release",
]
labels = [1, 1, 1, 1, 0, 0, 0, 0]

pipeline = Pipeline([
    ("tfidf", feature_extraction.get_feature_model("tfidf")),
    ("clf", classifiers_module.get_classifier("logistic")),
])
try:
    check_is_fitted(pipeline)
except NotFittedError:
    pass
else:
    msg = "unfitted pipeline reported as fitted"
    raise AssertionError(msg)
pipeline.fit(texts, labels)
check_is_fitted(pipeline)
proba = pipeline.predict_proba(texts)
assert proba.shape == (len(texts), 2)
assert ((proba >= 0) & (proba <= 1)).all()
assert proba[:4, 1].min() > proba[4:, 1].max()
