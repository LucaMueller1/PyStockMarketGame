from streamlit.script_request_queue import RerunData
from streamlit.script_runner import RerunException
from streamlit.server.server import Server
import streamlit.report_thread as ReportThread


def rerun():
    """Rerun a Streamlit app from the top!"""
    widget_states = _get_widget_states()
    raise RerunException(RerunData(widget_states))


def _get_widget_states():
    # Hack to get the session object from Streamlit.

    ctx = ReportThread.get_report_ctx()

    session = None
    session_infos = Server.get_current()._session_infos.values()

    for session_info in session_infos:
        if session_info.session.enqueue == ctx.enqueue:
            session = session_info.session

    if session is None:
        raise RuntimeError(
            "Oh noes. Couldn't get your Streamlit Session object"
            "Are you doing something fancy with threads?"
        )
    # Got the session object!

    return session._widget_states