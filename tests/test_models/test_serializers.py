import shutil

from racket.models.base import MLModel
from racket.models.serializers.k import KerasSerializer
from racket.models.serializers.meta import MetadataSerializer


def test_keras_serializer(instantiated_learner):
    k = KerasSerializer(instantiated_learner.path,
                        instantiated_learner.version_dir,
                        instantiated_learner.model,
                        instantiated_learner.model_name)

    assert isinstance(instantiated_learner.sql, MLModel)

    p = k.path
    assert k.keras_json == p + '_2.json'
    assert k.keras_h5 == p + '_2.h5'
    assert p in k.tf_path
    shutil.rmtree('serialized')


def test_metadata_serializer():
    scores = {'auc': 0.9, 'accuracy': 1}
    # noinspection PyArgumentList
    model = MLModel(model_id=45, model_name='test', major=1, minor=1, patch=1, version_dir=3,
                    model_type='regression')
    md = MetadataSerializer('tests/sample_project', 'test')
    md.store(scores, model)
