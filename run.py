#!/usr/bin/env python
from app import app, init_application
from config import DebugConfiguration as config

if __name__ == "__main__":
    init_application(app, config)
    app.debug = True
    app.run(host='0.0.0.0')
