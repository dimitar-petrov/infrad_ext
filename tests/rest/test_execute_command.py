import json
import mock
from infrad.shared import response_object as res
from infrad.domain.models import CommandResult
from infrad.shared.consts import JobState


result1_dict = {
    'status': JobState.COMPLETED,
    'message': 'Backend Message',
    'data': {
        'key1': 'value1'
    }
}

result1_domain_model = CommandResult.from_dict(result1_dict)
results = [result1_domain_model]


@mock.patch('infrad.use_cases.command_execute_use_case.CommandExecuteUseCase')
def test_execute(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess(results)

    http_response = client.post('/execute',
                                data=json.dumps({'comm': 'test'}),
                                content_type='application/json')

    assert json.loads(http_response.data.decode('UTF-8')) == [result1_dict]
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'
