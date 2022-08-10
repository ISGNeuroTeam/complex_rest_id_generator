from rest.views import APIView
from rest.response import status, SuccessResponse, ErrorResponse, Response
from rest.permissions import AllowAny
import logging
from ..utils.unique_id_generator import UniqueIdGenerator

logger = logging.getLogger('dtcd_utils')


class IdGenerator(APIView):
    permission_classes = (AllowAny,)
    http_method_names = ['get']

    def get(self, request):
        try:
            unique_id_generator = UniqueIdGenerator.create_unique_id_generator(dict(request.GET))
        except Exception as e:
            return ErrorResponse(error_message=str(e))
        return Response(unique_id_generator.generate_ids(), status.HTTP_200_OK)


