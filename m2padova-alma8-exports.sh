# Default from master branch
# export MARTe2_DIR=~/Projects/MARTe2-dev
# m2padova-alma8 branch : already provided in the reference container

# Default from master branch
# export MARTe2_Components_DIR=~/Projects/MARTe2-components
# m2padova-alma8 branch : already provided in the reference container

# Default from master branch
# export OPEN62541_LIB=~/Projects/open62541/build/bin
# m2padova-alma8 branch : already provided in the reference container

# Default from master branch
# export OPEN62541_INCLUDE=~/Projects/open62541/build
# m2padova-alma8 branch : already provided in the reference container

# Default from master branch
# export EPICS_BASE=~/Projects/epics-base-7.0.2
# m2padova-alma8 branch : already provided in the reference container

# Default from master branch
# export EPICSPVA=~/Projects/EPICS/base-7.0.2
# m2padova-alma8 branch : already provided in the reference container

# Default from master branch
# export EPICS_HOST_ARCH=linux-x86_64
# m2padova-alma8 branch : already provided in the reference container

# Default from master branch : still applies
export PATH=$PATH:$EPICS_BASE/bin/$EPICS_HOST_ARCH

# Default from master branch
# export SDN_CORE_INCLUDE_DIR=~/Projects/SDN_1.0.12_nonCCS/src/main/c++/include/
# m2padova-alma8 branch : already provided in the reference container

# Default from master branch
# export SDN_CORE_LIBRARY_DIR=~/Projects/SDN_1.0.12_nonCCS/target/lib/
# m2padova-alma8 branch : already provided in the reference container

# Default from master branch : applies
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MARTe2_DIR/Build/x86-linux/Core/:$EPICS_BASE/lib/$EPICS_HOST_ARCH:$SDN_CORE_LIBRARY_DIR
 
