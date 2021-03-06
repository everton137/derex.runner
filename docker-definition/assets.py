"""
Bare minimum settings for collecting production assets.
"""

from ..common import *  # type: ignore # noqa: F403,F401
from ..common import COMPREHENSIVE_THEME_DIRS  # type: ignore
from ..common import WEBPACK_LOADER  # type: ignore
from openedx.core.lib.derived import derive_settings
from path import Path as path

import os


COMPREHENSIVE_THEME_DIRS.append("/openedx/themes")  # type: ignore
STATIC_ROOT_BASE = os.environ.get("STATIC_ROOT_LMS", "/openedx/staticfiles")
STATIC_ROOT = {  # type: ignore
    "lms": path(STATIC_ROOT_BASE),
    "cms": path(STATIC_ROOT_BASE) / "studio",
}[
    os.environ.get("SERVICE_VARIANT")  # type: ignore
]
WEBPACK_LOADER["DEFAULT"]["STATS_FILE"] = (  # type: ignore
    STATIC_ROOT / "webpack-stats.json"
)

SECRET_KEY = "secret"
XQUEUE_INTERFACE = {"django_auth": None, "url": None}
DATABASES = {"default": {}}  # type: ignore

# enterprise.views tries to access settings.ECOMMERCE_PUBLIC_URL_ROOT,
ECOMMERCE_PUBLIC_URL_ROOT = None

STATICFILES_STORAGE = "whitenoise_edx.WhitenoiseEdxStorage"
derive_settings(__name__)
