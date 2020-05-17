#!/bin/bash
followme_branch="ros2/master"
msg_branch="ros2/develop"
bringup_branch="master"
ydlider_branch="master"
locationreg_branch="master"
turn_branch="master"

cd follow_me
branch=$(git branch --contains=HEAD)
echo ${branch}
if [ "${branch}" = "* ${followme_branch}" ]; then
    echo "pull!"
    git pull origin ${followme_branch}
else
    echo "Switch branches and then pull"
    git checkout ${followme_branch}
    git pull origin ${followme_branch}
fi

cd ../rione_msgs
branch=$(git branch --contains=HEAD)
echo ${branch}
if [ "${branch}" = "* ${msg_branch}" ]; then
    echo "pull!"
    git pull origin ${msg_branch}
else
    echo "Switch branches and then pull"
    git checkout ${msg_branch}
    git pull origin ${msg_branch}
fi

cd ../turtlebot_bringup
branch=$(git branch --contains=HEAD)
echo ${branch}
if [ "${branch}" = "* ${bringup_branch}" ]; then
    echo "pull!"
    git pull origin ${bringup_branch}
else
    echo "Switch branches and then pull"
    git checkout ${bringup_branch}
    git pull origin ${bringup_branch}
fi

cd ../ydlidar_ros2
branch=$(git branch --contains=HEAD)
echo ${branch}
if [ "${branch}" = "* ${ydlider_branch}" ]; then
    echo "pull!"
    git pull origin ${ydlider_branch}
else
    echo "Switch branches and then pull"
    git checkout ${ydlider_branch}
    git pull origin ${ydlider_branch}
fi

cd ../location_register
branch=$(git branch --contains=HEAD)
echo ${branch}
if [ "${branch}" = "* ${locationreg_branch}" ]; then
    echo "pull!"
    git pull origin ${locationreg_branch}
else
    echo "Switch branches and then pull"
    git checkout ${locationreg_branch}
    git pull origin ${locationreg_branch}
fi

cd ../turn_robot
branch=$(git branch --contains=HEAD)
echo ${branch}
if [ "${branch}" = "* ${turn_branch}" ]; then
    echo "pull!"
    git pull origin ${turn_branch}
else
    echo "Switch branches and then pull"
    git checkout ${turn_branch}
    git pull origin ${turn_branch}
fi

cd ..

colcon build

source install/setup.bash
