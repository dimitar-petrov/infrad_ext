import json
from flask import Blueprint, request, Response

from infrad.use_cases import request_objects as req
from infrad.use_cases import command_execute_use_case as uc
from infrad.shared import response_object as res
from infrad.serializers import command_result_serializer as ser
from infrad.endpoints.plugin_endpoint import PluginEndpoint

blueprint = Blueprint('command_result', __name__)

STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500,
}


@blueprint.route('/execute', methods=['POST'])
def command_result():
    request_data = json.loads(request.data)
    request_object = req.CommandExecuteRequestObject.from_dict(request_data)
    endpoint = PluginEndpoint()

    use_case = uc.CommandExecuteUseCase(endpoint)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.CommandResultEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])
