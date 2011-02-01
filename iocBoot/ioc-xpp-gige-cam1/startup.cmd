#!/bin/bash

# Setup the IOC user environment
# TODO: Change xxx as needed for your hutch
source /reg/d/iocCommon/All/xpp_env.sh
export IOC="ioc-xpp-gige-cam1"

# Make sure the IOC's data directories are ready for use
$RUNUSER "mkdir -p $IOC_DATA/$IOC/autosave"
$RUNUSER "mkdir -p $IOC_DATA/$IOC/archive"
$RUNUSER "mkdir -p $IOC_DATA/$IOC/iocInfo"

# Make sure permissions are correct
$RUNUSER "chmod ug+w -R $IOC_DATA/$IOC"

# For release
#cd $EPICS_SITE_TOP/ioc/xxx/gige/R0.1.0/iocBoot/ioc-xpp-gige-cam1

# For development
cd ~pstoffel/repo/epics/trunk/ioc/common/gigECam/current/iocBoot/ioc-xpp-gige-cam1

# Copy the archive file to iocData
$RUNUSER "cp ../../archive/$IOC.archive $IOC_DATA/$IOC/archive"

# Launch the IOC
$RUNUSER "$PROCSERV --logfile $IOC_DATA/$IOC/iocInfo/ioc.log --name $IOC 30001 ../../bin/linux-x86_64/gige st.cmd"
