from diagrams import Diagram,Edge,Cluster
from diagrams.aws.database import DB
from diagrams.aws.compute import EC2
from diagrams.aws.network import ALB


graph_attr = {
    "splines": "spline",
    "fontsize": "24",
    "bgcolor": "transparent"
}
ALB_TEXT = "ALB 99.99%"
FRONTEND_TEXT = "Frontend 99.5%"
BACKEND_TEXT = "Backend 99.5%"
DATABASE_TEXT = "DB 99.95%"

with Diagram("Components in Parallel", show=False, direction="LR", graph_attr=graph_attr):
    lb = ALB(ALB_TEXT)
    with Cluster("Cluster 1"):
        frontend1 = EC2(FRONTEND_TEXT)
        backend1 = EC2(BACKEND_TEXT)
        database1 = DB(DATABASE_TEXT)
    with Cluster("Cluster 2"):
        frontend2 = EC2(FRONTEND_TEXT)
        backend2 = EC2(BACKEND_TEXT)
        database2 = DB(DATABASE_TEXT)


    lb >> frontend1 >> backend1 >> database1
    lb >> frontend2 >> backend2 >> database2

with Diagram("Components in Series", show=False, direction="LR", graph_attr=graph_attr):
    lb = ALB(ALB_TEXT)
    frontend = EC2(FRONTEND_TEXT)
    backend = EC2(BACKEND_TEXT)
    database = DB(DATABASE_TEXT)

    lb >> frontend >> backend >> database
