additionalBuildArgs = "--pull"
if (env.BRANCH_NAME == "develop") {
  additionalBuildArgs = "--pull --no-cache"
}

pipeline {
  agent none

  options {
    ansiColor("xterm")
  }

  triggers {
    cron(env.BRANCH_NAME == 'develop' ? '@weekly' : '')
  }

  stages {
    stage("Test") {
      agent {
        dockerfile {
          additionalBuildArgs "${additionalBuildArgs}"
          filename "dockerfiles/ci/Dockerfile"
        }
      }

      steps {
        sh "flake8"
        sh "black --check ."
        sh "pytest --cov=src"
      }

      post {
        always {
          sh "chown -R \$(stat -c '%u' .) \$WORKSPACE"
        }
      }
    }
    stage("Staging deployment") {
    when { branch "master" }

    steps {
      sh "git remote | grep heroku >/dev/null || git remote add heroku git@heroku.com:kb-happiness.git"
      sh "git push heroku HEAD:master"
    }
   }
  }
}
