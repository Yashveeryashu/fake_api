#!/bin/bash
uvicorn fake_credit_api:app --host 0.0.0.0 --port $PORT
