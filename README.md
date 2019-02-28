### a hello-world style excercise to demo kubernetes' autoscaling capability for celery workers.

* files used here are based off below link:
    
    https://github.com/fabric8io/gitcontroller/tree/master/vendor/k8s.io/kubernetes/examples/celery-rabbitmq

* below tested with a physical machine with ubuntu 18.04 installed.
* enable VT-X/AMD-v enabled. Enabling it in the BIOS is mandatory.
* install virtualbox (for physical machine), docker, minikube.
    
    for physical machine: see below links for installation steps:
    https://docs.docker.com/install/linux/docker-ce/ubuntu/
    https://kubernetes.io/docs/tasks/tools/install-minikube/
    https://askubuntu.com/questions/367248/how-to-install-virtualbox-from-command-line
    https://github.com/aws-samples/aws-workshop-for-kubernetes/blob/master/03-path-application-development/301-local-development/readme.adoc#setup-on-ec2-if-you-do-not-virtualbox-on-your-laptop
    https://www.radishlogic.com/kubernetes/running-minikube-in-aws-ec2-ubuntu/
     
* setup minikube
    
    optional: sudo -i
    
    FOR Physical Machine:
    minikube stop && minikube start --memory 8192 --insecure-registry localhost:5000
    
    FOR EC2:
    sudo minikube start --vm-driver=none --memory 8192 --insecure-registry localhost:5000 

    install cpu monitor pulugin (https://github.com/kubernetes/minikube/issues/1095)
    minikube addons enable heapster 

    Run below for each shell that will be executing kubectl,minikube,docker commands.
    eval $(minikube docker-env)

* build images using docker daemon within minikube

    cd examples/celery-rabbitmq/task
    
    docker build -t celery-task .
    
    cd examples/celery-rabbitmq/worker
    
    docker build -t celery-worker .

    cd ../../..

* verify docker images within minikube (different than `sudo docker images`)
       
    docker images 
 
* start up pods/services
    
    
    kubectl create -f examples/celery-rabbitmq/rabbitmq-service.yaml
 
    kubectl create -f examples/celery-rabbitmq/rabbitmq-controller.yaml

    kubectl create -f examples/celery-rabbitmq/flower-service.yaml
 
    kubectl create -f examples/celery-rabbitmq/flower-controller.yaml
    
    kubectl create -f examples/celery-rabbitmq/celery-deployment.yaml 

    kubectl create -f examples/celery-rabbitmq/hpa.yaml

    kubectl create -f examples/celery-rabbitmq/celery-task-controller.yaml
    
    
    kubectl delete -f examples/celery-rabbitmq/rabbitmq-service.yaml
 
    kubectl delete -f examples/celery-rabbitmq/rabbitmq-controller.yaml

    kubectl delete -f examples/celery-rabbitmq/flower-service.yaml
 
    kubectl delete -f examples/celery-rabbitmq/flower-controller.yaml
    
    kubectl delete -f examples/celery-rabbitmq/celery-deployment.yaml 

    kubectl delete -f examples/celery-rabbitmq/hpa.yaml

    kubectl delete -f examples/celery-rabbitmq/celery-task-controller.yaml


* monitor minikube, rabbit, flower via web interface via port forwarding.
     
    HOST:
    
    kubectl proxy
    
    minikube dashboard --url
    
    kubectl port-forward svc/flower-service 5555:5555
    
    kubectl port-forward pod/rabbitmq-controller-p5btj 15672:15672
    
    CLIENT:
    
    export myurl=user@hostname
    
    ssh -L 8001:127.0.0.1:8001 $myurl -v -v
    
    ssh -L 8002:127.0.0.1:15672 $myurl -v -v
    
    ssh -L 8003:127.0.0.1:5555 $myurl -v -v
    
    open chrome and goto:
    http://localhost:8001/api/v1/namespaces/kube-system/services/http:kubernetes-dashboard:/proxy



* if docker container fails running, run docker container by itself to debug.
   
   docker run -t celery-worker
   
   docker run -t celery-task
   
   
* misc
   
   kubectl exec -it shell-demo -- /bin/bash
   
   python -m celery inspect active -b amqp://$RABBITMQ_SERVICE_SERVICE_HOST


* autoscale misc

    kubectl get hpa

    watch kubectl get hpa

    https://medium.com/google-cloud/kubernetes-horizontal-pod-scaling-190e95c258f5
    
### ref. 

https://stackoverflow.com/a/48999680/868736
kubectl autoscale deployment celery --cpu-percent=50 --min=1 --max=10
kubectl get pods
kubectl get svc flower-service
kubectl port-forward svc/flower-service 5555:5555
kubectl delete pods,services flower-service
kubectl exec worker-controller-5dfd669d5f-28vlk env | grep RABBITMQ
kubectl get deployments

https://kubernetes.io/docs/concepts/workloads/controllers/


--


WIP.
https://kubernetes.io/blog/2016/07/autoscaling-in-kubernetes/
https://github.com/kubernetes/minikube/issues/604

https://plugaru.org/2018/01/03/rabbitmq-celery-kubernetes-ha/
https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/
