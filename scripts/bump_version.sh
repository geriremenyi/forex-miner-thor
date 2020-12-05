#!/bin/bash

# Parameters to named parameters
version_type=$1

# Parameter checks
if [ "$version_type" = "" ]
then
    echo "[WARNING] Version type was not given. Setting version type to 'patch'"
    version_type="patch"
else
    if [ "$version_type" != "patch" ] && [ "$version_type" != "minor" ] && [ "$version_type" != "major" ]
    then
        echo "[ERROR] The first parameter is the version type which should be either 'patch', 'minor' or 'major'."
        exit 1
    fi
fi

# Get current version
semver_regex='[^0-9]*\([0-9]*\)[.]\([0-9]*\)[.]\([0-9]*\)\([0-9A-Za-z-]*\)'
setup_file="$(dirname "$0")/../setup.py"
current_version="$(grep -oPm1 '(?<=version\=\")[^\",]+' <<< $(cat $setup_file))"
major=`echo $current_version | sed -e "s#$semver_regex#\1#"`
minor=`echo $current_version | sed -e "s#$semver_regex#\2#"`
patch=`echo $current_version | sed -e "s#$semver_regex#\3#"`

# Calculate next version
if [ "$version_type" = "patch" ]
then
    let patch+=1
else
    if [ "$version_type" = "minor" ]
    then
        let minor+=1
    else
        let major+=1
    fi
fi
next_version="$major.$minor.$patch"

# Bumping version
root_folder="$(dirname "$0")/.."
sed -i "s/version=\".*\",/version=\"$next_version\",/g" "$root_folder/setup.py"
sed -i "s/ghcr.io\/geriremenyi\/forex-miner-thor\:.*/ghcr.io\/geriremenyi\/forex-miner-thor\:$next_version/g" "$root_folder/k8s/app.yaml"