
echo "Start building Docker images"

EXECUTOR_IMAGE_NAME="executor-image"
CONTROLLER_IMAGE_NAME="controller-image"
LB_IMAGE_NAME="lb-image"


EXECUTOR_REPO_PATH="C:\Users\Kacper\CLionProjects\ExecutorApp"
CONTROLLER_REPO_PATH="C:\Users\Kacper\Desktop\inz\Controller\ControllerApp"
LB_REPO_PATH="C:\Users\Kacper\Desktop\inz\TestingSetup\load-balancer"

cd $LB_REPO_PATH
docker build -t $LB_IMAGE_NAME .

cd $EXECUTOR_REPO_PATH
docker build -t $EXECUTOR_IMAGE_NAME .

cd $CONTROLLER_REPO_PATH
docker build -t $CONTROLLER_IMAGE_NAME .

