#!/bin/bash

skaffold build -d us-central1-docker.pkg.dev/shingo-new-proto/myrepo --interactive=false --file-output=test.json
