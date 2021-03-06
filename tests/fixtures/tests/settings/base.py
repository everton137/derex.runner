import os


SERVICE_VARIANT = os.environ["SERVICE_VARIANT"]
assert SERVICE_VARIANT in ("lms", "cms")
exec("from {}.envs.derex.base import *".format(SERVICE_VARIANT), globals(), locals())

SITE_NAME = "{}.edx.localhost".format(SERVICE_VARIANT)
HTTPS = "on"
CMS_BASE = "cms.edx.localhost"
LMS_BASE = "lms.edx.localhost"
