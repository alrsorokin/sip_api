import io
import os

from flask import abort, make_response, request, send_file
from flask.views import MethodView
from yadisk.exceptions import PathNotFoundError

from sip_api.app import app, disk, token_auth

EXTANSION = '.wav'


class RecordingView(MethodView):

    @token_auth.login_required
    def get(self):
        call_id = request.args.get('call_id')
        if not call_id:
            return abort(404)

        output = io.BytesIO()
        try:
            disk.download(os.path.join(app.config['UPLOAD_DIR'], f'{call_id}{EXTANSION}'), output)
        except PathNotFoundError:
            abort(400)

        output.seek(0)

        return send_file(output,
                         mimetype="audio/wav",
                         as_attachment=True,
                         attachment_filename=f"{call_id}{EXTANSION}")
