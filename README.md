# DVP Week 12 - CI/CD Pipeline with Jenkins

A small Python validation app used to demonstrate a Jenkins pipeline triggered by a GitHub webhook.

## Files
- `app.py` - simple user-details validation function
- `tests/test_app.py` - four automated unit tests
- `Jenkinsfile` - Jenkins Declarative Pipeline with Checkout, Build and Test stages

## Run locally (Windows)
```bat
python app.py
python -m unittest discover -s tests -v
```

## Jenkins pipeline
Create a Pipeline job configured to use **Pipeline script from SCM**:
- SCM: Git
- Repository URL: your GitHub repository URL
- Script Path: `Jenkinsfile`

The Jenkins agent must have Python installed and `python` available on PATH.
