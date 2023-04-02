# Exercise 01

The sample code contains the python application that expects a Redis instance to connect to.
When we deploy the example deployment.yaml and the respective service, we can curl at the Service endpoint (ClusterIP)
to get a response like this:

```
$> curl http://10.43.189.56
You reached simpleapp-deploy-597dd5457c-rk847 so far 16 times
$> curl http://10.43.189.56
You reached simpleapp-deploy-597dd5457c-hsdq2 so far 29 times
```

So we can see that calling the same service we get different responses because there are different 
Redis instances running in each pod of this deployment.

This indicates a problem in our design.

Can we change this deployment so we could have a consistent response each time we call the web service?

Feel free to add deployments, services or change existing to satisfy the requirement.

**Note: Please branch this repo to submit your solution.**
