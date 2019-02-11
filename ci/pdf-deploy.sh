#!/bin/bash
# Push a new commit to the `pdf' branch with the resulting pdfs

# To return a failure if any commands inside fail
set -e

# Define variables
REPO=${TRAVIS_REPO_SLUG}
BRANCH=pdf
CLONE_DIR=${HOME}/deploy
CLONE_ARGS="--quiet --branch=${BRANCH} --single-branch"
REPO_URL=https://${GH_TOKEN}@github.com/${REPO}.git
PDFS_DIR=_output
PDFS_PATH=${TRAVIS_BUILD_DIR}/${PDFS_DIR}

echo -e "DEPLOYING PDF TO A DEPLOY BRANCH:"
echo -e "Target: branch ${BRANCH} of ${REPO}"

# Clone the project, using the secret token.
# Uses /dev/null to avoid leaking decrypted key.
echo -e "Cloning ${REPO}"
git clone ${CLONE_ARGS} ${REPO_URL} ${CLONE_DIR} 2>&1 >/dev/null

# Configure git to a dummy Travis user
git config user.email "travis@nothing.com"
git config user.name "TravisCI"

# Delete all the files and replace with our new set
echo -e "Remove old files from previous builds"
cd ${CLONE_DIR}
git rm -rf .
cp -Rf ${PDFS_PATH}/*.pdf ${CLONE_DIR}/

# Commit new changes and push
echo -e "Add and commit changes"
git add -A .
git status

echo -e "Making a new commit"
git commit -m "Push from Travis Build Number ${TRAVIS_BUILD_NUMBER}"

echo -e "Pushing..."
git push -fq origin ${BRANCH} 2>&1 >/dev/null

# Workaround for https://github.com/travis-ci/travis-ci/issues/6522
# Turn off exit on failure.
set +e
